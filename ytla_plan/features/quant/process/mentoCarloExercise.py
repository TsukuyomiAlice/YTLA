import numba
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'  # 设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
from scipy import stats
import seaborn as sns
from datetime import datetime, timedelta

# 设置随机种子确保结果可复现
np.random.seed(42)


class MonteCarloReturnSimulator:
    """
    蒙特卡洛模拟收益率分析器
    用于模拟投资组合的未来收益率分布
    """

    def __init__(self, initial_investment=100000, annual_return=0.08, annual_volatility=0.15,
                 risk_free_rate=0.02):
        """
        初始化模拟参数

        参数:
        ----------
        initial_investment : float
            初始投资金额
        annual_return : float
            预期年化收益率
        annual_volatility : float
            年化波动率
        risk_free_rate : float
            无风险利率
        """
        self.initial_investment = initial_investment
        self.annual_return = annual_return
        self.annual_volatility = annual_volatility
        self.risk_free_rate = risk_free_rate

        # 转换为日参数（假设252个交易日）
        self.daily_return = annual_return / 252
        self.daily_volatility = annual_volatility / np.sqrt(252)

    def simulate_geometric_brownian_motion(self, days=252, n_simulations=10000):
        """
        使用几何布朗运动模拟股价/净值路径

        参数:
        ----------
        days : int
            模拟天数（默认1年=252个交易日）
        n_simulations : int
            模拟次数

        返回:
        ----------
        simulation_paths : ndarray
            形状为 (n_simulations, days) 的模拟路径
        """
        # 初始化价格路径数组
        price_paths = np.zeros((n_simulations, days + 1))
        price_paths[:, 0] = self.initial_investment

        # 生成随机数（使用正态分布）
        random_shocks = np.random.normal(
            loc=self.daily_return,
            scale=self.daily_volatility,
            size=(n_simulations, days)
        )

        # 计算每日收益率
        daily_returns = np.exp(random_shocks) - 1

        # 计算累计收益路径
        for t in range(1, days + 1):
            price_paths[:, t] = price_paths[:, t - 1] * (1 + daily_returns[:, t - 1])

        return price_paths

    def simulate_with_garch(self, days=252, n_simulations=10000,
                            omega=0.000001, alpha=0.1, beta=0.85):
        """
        使用GARCH(1,1)模型模拟收益率（考虑波动率聚类效应）

        参数:
        ----------
        days : int
            模拟天数
        n_simulations : int
            模拟次数
        omega, alpha, beta : float
            GARCH模型参数

        返回:
        ----------
        simulation_paths : ndarray
            模拟路径
        """
        price_paths = np.zeros((n_simulations, days + 1))
        price_paths[:, 0] = self.initial_investment

        # 初始化条件方差
        conditional_variance = np.ones(n_simulations) * (self.daily_volatility ** 2)

        for t in range(1, days + 1):
            # 生成带有时变波动率的随机冲击
            random_shocks = np.random.normal(
                loc=self.daily_return,
                scale=np.sqrt(conditional_variance),
                size=n_simulations
            )

            # 更新价格
            price_paths[:, t] = price_paths[:, t - 1] * np.exp(random_shocks)

            # 更新GARCH条件方差（使用模拟的收益率）
            returns = np.log(price_paths[:, t] / price_paths[:, t - 1])
            epsilon = returns - self.daily_return
            conditional_variance = omega + alpha * epsilon ** 2 + beta * conditional_variance

        return price_paths

    def analyze_simulation_results(self, final_values, confidence_levels=[0.05, 0.5, 0.95]):
        """
        分析模拟结果

        参数:
        ----------
        final_values : ndarray
            模拟结束时的价值数组
        confidence_levels : list
            要计算的置信水平

        返回:
        ----------
        analysis_dict : dict
            包含各种分析指标的字典
        """
        analysis = {}

        # 计算年化收益率
        total_return = (final_values - self.initial_investment) / self.initial_investment
        analysis['annualized_return'] = (1 + total_return.mean()) ** (252 / len(final_values)) - 1

        # 计算波动率
        analysis['annualized_volatility'] = total_return.std() * np.sqrt(252)

        # 计算夏普比率
        excess_return = analysis['annualized_return'] - self.risk_free_rate
        analysis['sharpe_ratio'] = excess_return / analysis['annualized_volatility']

        # 计算最大回撤（模拟版）
        analysis['max_drawdown'] = np.min(total_return)

        # 计算VaR（风险价值）
        analysis['var_95'] = np.percentile(total_return, 5) * self.initial_investment
        analysis['cvar_95'] = total_return[
                                  total_return <= np.percentile(total_return, 5)].mean() * self.initial_investment

        # 计算分位数
        for conf in confidence_levels:
            percentile = np.percentile(final_values, conf * 100)
            analysis[f'percentile_{int(conf * 100)}'] = percentile

        # 计算正收益概率
        analysis['prob_positive_return'] = np.mean(final_values > self.initial_investment)

        # 计算期望收益
        analysis['expected_final_value'] = np.mean(final_values)

        return analysis

    def plot_simulation_results(self, price_paths, n_paths_to_plot=50):
        """
        可视化模拟结果

        参数:
        ----------
        price_paths : ndarray
            价格路径数组
        n_paths_to_plot : int
            要绘制的路径数量
        """
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))

        # 1. 绘制部分模拟路径
        axes[0, 0].plot(price_paths[:n_paths_to_plot, :].T, alpha=0.3, linewidth=0.5)
        axes[0, 0].axhline(y=self.initial_investment, color='r', linestyle='--', label='初始投资')
        axes[0, 0].set_title(f'{n_paths_to_plot}条模拟路径')
        axes[0, 0].set_xlabel('交易日')
        axes[0, 0].set_ylabel('投资组合价值')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)

        # 2. 绘制最终价值的直方图
        final_values = price_paths[:, -1]
        axes[0, 1].hist(final_values, bins=50, edgecolor='black', alpha=0.7)
        axes[0, 1].axvline(x=self.initial_investment, color='r', linestyle='--', label='初始投资')
        axes[0, 1].axvline(x=np.mean(final_values), color='g', linestyle='--', label='期望值')
        axes[0, 1].set_title('最终价值分布')
        axes[0, 1].set_xlabel('最终价值')
        axes[0, 1].set_ylabel('频数')
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)

        # 3. 绘制累计收益率分布
        returns = (final_values - self.initial_investment) / self.initial_investment
        axes[1, 0].hist(returns * 100, bins=50, edgecolor='black', alpha=0.7)
        axes[1, 0].axvline(x=0, color='r', linestyle='--', label='盈亏平衡')
        axes[1, 0].set_title('总收益率分布 (%)')
        axes[1, 0].set_xlabel('收益率 (%)')
        axes[1, 0].set_ylabel('频数')
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)

        # 4. 绘制VaR分析
        var_95 = np.percentile(returns, 5)
        cvar_95 = returns[returns <= var_95].mean()

        axes[1, 1].hist(returns * 100, bins=50, edgecolor='black', alpha=0.7, density=True)
        axes[1, 1].axvline(x=var_95 * 100, color='r', linestyle='--',
                           label=f'95% VaR: {var_95 * 100:.2f}%')
        axes[1, 1].axvline(x=cvar_95 * 100, color='orange', linestyle='--',
                           label=f'95% CVaR: {cvar_95 * 100:.2f}%')
        axes[1, 1].axvspan(var_95 * 100, returns.min() * 100, alpha=0.3, color='red',
                           label='最坏5%的损失')
        axes[1, 1].set_title('风险价值(VaR)分析')
        axes[1, 1].set_xlabel('收益率 (%)')
        axes[1, 1].set_ylabel('概率密度')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

        return final_values, returns

    def run_comprehensive_analysis(self, simulation_method='gbm', **kwargs):
        """
        运行完整的蒙特卡洛分析

        参数:
        ----------
        simulation_method : str
            模拟方法 ('gbm' 或 'garch')
        **kwargs : dict
            传递给模拟方法的参数

        返回:
        ----------
        results : dict
            包含所有分析结果的字典
        """
        print("=" * 60)
        print("蒙特卡洛模拟分析报告")
        print("=" * 60)

        # 选择模拟方法
        if simulation_method == 'gbm':
            price_paths = self.simulate_geometric_brownian_motion(**kwargs)
            method_name = "几何布朗运动"
        elif simulation_method == 'garch':
            price_paths = self.simulate_with_garch(**kwargs)
            method_name = "GARCH(1,1)模型"
        else:
            raise ValueError("模拟方法必须是 'gbm' 或 'garch'")

        print(f"模拟方法: {method_name}")
        print(f"模拟次数: {price_paths.shape[0]}")
        print(f"模拟天数: {price_paths.shape[1] - 1}")
        print(f"初始投资: ${self.initial_investment:,.2f}")
        print(f"预期年化收益率: {self.annual_return * 100:.2f}%")
        print(f"年化波动率: {self.annual_volatility * 100:.2f}%")

        # 可视化
        final_values, returns = self.plot_simulation_results(price_paths)

        # 详细分析
        analysis = self.analyze_simulation_results(final_values)

        print("\n" + "-" * 60)
        print("关键分析指标:")
        print("-" * 60)
        print(f"期望最终价值: ${analysis['expected_final_value']:,.2f}")
        print(f"年化收益率: {analysis['annualized_return'] * 100:.2f}%")
        print(f"年化波动率: {analysis['annualized_volatility'] * 100:.2f}%")
        print(f"夏普比率: {analysis['sharpe_ratio']:.3f}")
        print(f"正收益概率: {analysis['prob_positive_return'] * 100:.2f}%")
        print(f"最大回撤: {analysis['max_drawdown'] * 100:.2f}%")
        print(f"95% VaR: ${analysis['var_95']:,.2f} (最坏5%情况下的平均损失)")
        print(f"95% CVaR: ${analysis['cvar_95']:,.2f} (尾部风险)")
        print(f"5%分位数: ${analysis['percentile_5']:,.2f} (95%置信度下的最低价值)")
        print(f"50%分位数: ${analysis['percentile_50']:,.2f} (中位数)")
        print(f"95%分位数: ${analysis['percentile_95']:,.2f} (5%置信度下的最高价值)")

        # 计算置信区间
        confidence_interval = (analysis['percentile_5'], analysis['percentile_95'])
        print(f"90%置信区间: [${confidence_interval[0]:,.2f}, ${confidence_interval[1]:,.2f}]")

        return {
            'price_paths': price_paths,
            'final_values': final_values,
            'returns': returns,
            'analysis': analysis,
            'confidence_interval': confidence_interval
        }


# ============================================================================
# 示例使用
# ============================================================================

def launcher():
    """主函数：演示如何使用蒙特卡洛模拟器"""

    # 1. 创建模拟器实例
    print("创建蒙特卡洛模拟器...")
    simulator = MonteCarloReturnSimulator(
        initial_investment=100000,  # 初始投资10万美元
        annual_return=0.26,  # 预期年化收益率10%
        annual_volatility=0.05,  # 年化波动率20%
        risk_free_rate=0.03  # 无风险利率3%
    )

    # 2. 运行基本GBM模拟
    print("\n运行几何布朗运动模拟...")
    results_gbm = simulator.run_comprehensive_analysis(
        simulation_method='gbm',
        days=252,  # 模拟1年（252个交易日）
        n_simulations=10000  # 10000次模拟
    )

    # 3. 运行GARCH模拟（考虑波动率聚类）
    print("\n\n运行GARCH模型模拟（考虑波动率聚类）...")
    simulator_garch = MonteCarloReturnSimulator(
        initial_investment=100000,
        annual_return=0.26,  # 预期年化收益率10%
        annual_volatility=0.05,  # 年化波动率20%
        risk_free_rate=0.03
    )

    results_garch = simulator_garch.run_comprehensive_analysis(
        simulation_method='garch',
        days=252,
        n_simulations=10000,
        omega=0.000001,  # GARCH参数
        alpha=0.1,
        beta=0.85
    )

    # 4. 比较两种方法的结果
    print("\n" + "=" * 60)
    print("两种模拟方法比较:")
    print("=" * 60)

    comparison_data = {
        '指标': ['期望最终价值', '年化收益率', '年化波动率', '夏普比率', '正收益概率', '95% VaR'],
        'GBM模型': [
            f"${results_gbm['analysis']['expected_final_value']:,.2f}",
            f"{results_gbm['analysis']['annualized_return'] * 100:.2f}%",
            f"{results_gbm['analysis']['annualized_volatility'] * 100:.2f}%",
            f"{results_gbm['analysis']['sharpe_ratio']:.3f}",
            f"{results_gbm['analysis']['prob_positive_return'] * 100:.2f}%",
            f"${results_gbm['analysis']['var_95']:,.2f}"
        ],
        'GARCH模型': [
            f"${results_garch['analysis']['expected_final_value']:,.2f}",
            f"{results_garch['analysis']['annualized_return'] * 100:.2f}%",
            f"{results_garch['analysis']['annualized_volatility'] * 100:.2f}%",
            f"{results_garch['analysis']['sharpe_ratio']:.3f}",
            f"{results_garch['analysis']['prob_positive_return'] * 100:.2f}%",
            f"${results_garch['analysis']['var_95']:,.2f}"
        ]
    }

    comparison_df = pd.DataFrame(comparison_data)
    print(comparison_df.to_string(index=False))

    # 5. 生成投资建议
    print("\n" + "=" * 60)
    print("投资建议摘要:")
    print("=" * 60)

    analysis = results_gbm['analysis']

    if analysis['sharpe_ratio'] > 0.5:
        sharpe_rating = "良好"
    elif analysis['sharpe_ratio'] > 0:
        sharpe_rating = "一般"
    else:
        sharpe_rating = "较差"

    if analysis['prob_positive_return'] > 0.7:
        prob_rating = "高"
    elif analysis['prob_positive_return'] > 0.5:
        prob_rating = "中等"
    else:
        prob_rating = "低"

    print(f"1. 夏普比率: {analysis['sharpe_ratio']:.3f} ({sharpe_rating})")
    print(f"2. 正收益概率: {analysis['prob_positive_return'] * 100:.1f}% ({prob_rating})")
    print(
        f"3. 90%置信区间最终价值: [${results_gbm['confidence_interval'][0]:,.0f}, ${results_gbm['confidence_interval'][1]:,.0f}]")
    print(f"4. 最大可能损失(95% VaR): ${analysis['var_95']:,.0f}")
    print(f"5. 尾部风险(95% CVaR): ${analysis['cvar_95']:,.0f}")

    # 根据结果给出建议
    if analysis['sharpe_ratio'] > 0.3 and analysis['prob_positive_return'] > 0.6:
        print("\n✅ 投资建议: 考虑投资，风险回报比相对合理")
    else:
        print("\n⚠️  投资建议: 谨慎投资，风险较高或回报不足")

    return results_gbm, results_garch


# 运行主函数
if __name__ == "__main__":
    results_gbm, results_garch = launcher()