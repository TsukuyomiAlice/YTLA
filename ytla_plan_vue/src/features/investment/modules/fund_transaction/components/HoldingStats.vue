<template>
  <div class="holding-stats">
    <div v-if="brief" class="stats-content">
      <h3 class="section-title">持仓统计</h3>

      <div class="stats-grid">
        <div class="stats-column">
          <div class="stat-item">
            <span class="label">最新净值</span>
            <span class="value">{{ brief.latest_price?.toFixed(4) || '--' }}</span>
          </div>
          <div class="stat-item">
            <span class="label">当前实际持有份额</span>
            <span class="value">{{ brief.holding_share?.toFixed(4) || '--' }}</span>
          </div>
          <div class="stat-item">
            <span class="label">显示持有份额</span>
            <span class="value">{{ brief.shown_share?.toFixed(4) || '--' }}</span>
          </div>
          <div class="stat-item">
            <span class="label">买仓标的金额</span>
            <span class="value">¥{{ brief.long_position_amount?.toFixed(2) || '--' }}</span>
          </div>
          <div class="stat-item">
            <span class="label">买仓持有份额</span>
            <span class="value">{{ brief.long_position_share?.toFixed(4) || '--' }}</span>
          </div>
          <div class="stat-item">
            <span class="label">获利金额</span>
            <span class="value" :class="{ profit: brief.profit_in_amount > 0, loss: brief.profit_in_amount < 0, zero: brief.profit_in_amount === 0 }">
              ¥{{ brief.profit_in_amount?.toFixed(2) || '--' }}
            </span>
          </div>
        </div>
        <div class="stats-column">
          <div class="stat-item">
            <span class="label">基金运行天数</span>
            <span class="value">{{ fundDays || 0 }} 天</span>
          </div>
          <div class="stat-item">
            <span class="label">当前实际持有金额</span>
            <span class="value">¥{{ brief.holding_amount?.toFixed(2) || '--' }}</span>
          </div>
          <div class="stat-item">
            <span class="label">显示持有金额</span>
            <span class="value">¥{{ brief.shown_amount?.toFixed(2) || '--' }}</span>
          </div>
          <div class="stat-item">
            <span class="label">卖仓标的份额</span>
            <span class="value">{{ brief.short_position_share?.toFixed(4) || '--' }}</span>
          </div>
          <div class="stat-item">
            <span class="label">卖仓持有金额</span>
            <span class="value">¥{{ brief.short_position_amount?.toFixed(2) || '--' }}</span>
          </div>
          <div class="stat-item">
            <span class="label">获利份额</span>
            <span class="value" :class="{ profit: brief.profit_in_share > 0, loss: brief.profit_in_share < 0, zero: brief.profit_in_share === 0 }">
              {{ brief.profit_in_share?.toFixed(4) || '--' }}
            </span>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="empty-state">
      暂无数据
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  brief: {
    code: string
    fund_name: string
    last_transaction_date: string
    latest_price: number
    holding_amount: number
    holding_share: number
    holding_average_price: number
    shown_amount: number
    shown_share: number
    profit_in_amount: number
    profit_in_share: number
    long_position_amount: number
    long_position_share: number
    short_position_share: number
    short_position_amount: number
  } | null | undefined
  fundDays?: number
}

defineProps<Props>()
</script>

<style scoped lang="scss">
.holding-stats {
  background: white;
  border-radius: 12px;
  padding: 4px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  flex-shrink: 0;

  .stats-content {
    .section-title {
      font-size: 18px;
      color: #333;
      margin: 0 0 20px 0;
    }

    .stats-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;

      .stats-column {
        display: flex;
        flex-direction: column;
        gap: 12px;
      }

      .stat-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 16px;
        background: #f5f5f5;
        border-radius: 8px;

        .label {
          font-size: 13px;
          color: #666;
        }

        .value {
          font-size: 16px;
          font-weight: 600;
          color: #333;

          &.profit {
            color: #f44336;
          }

          &.loss {
            color: #4caf50;
          }

          &.zero {
            color: #333;
          }
        }
      }
    }
  }

  .empty-state {
    text-align: center;
    color: #999;
    padding: 40px;
  }
}
</style>
