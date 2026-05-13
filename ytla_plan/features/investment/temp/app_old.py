# encode = utf-8

from flask import Flask, render_template, request
from script import scriptFundInfo, scriptTransactionHistory
from schedule import scheduleAutoDailyTask

app = Flask(__name__, template_folder='./templates')


# 主页
@app.route('/')
def main_page():
    return render_template("/index.html")


# 基金 - 基金名称
@app.route('/fundInfo')
def fund_name():
    code = request.args.get('code')
    name = scriptFundInfo.get_name(code)
    return name


# 基金 - 快速登录交易
@app.route("/transactionLogOn", methods=['POST'])
def transaction_log_on():
    res = {}
    if request.method == "POST":
        code = request.form.get('code')
        transaction_date = request.form.get('transactionDate')
        transaction_type = request.form.get('transactionType')
        amount = request.form.get('amount')
        share = request.form.get('share')
        price = request.form.get('price')
        transaction_fee = request.form.get('transactionFee')
        transaction_id = scriptTransactionHistory.log_on(
            code, transaction_date, transaction_type, amount, share, price, transaction_fee)
        res = f"登录ID: {str(transaction_id)}"
    return res


# 自动化执行清算
@app.route("/auto")
def auto_calculation():
    scheduleAutoDailyTask.execute()
    return "自动执行完成！"


if __name__ == '__main__':
    app.run(debug=True, port=34567)
