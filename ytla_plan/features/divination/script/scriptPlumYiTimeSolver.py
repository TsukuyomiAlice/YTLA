# encode = utf-8
from ytla_plan.core.basic.func import timeFormat
from ytla_plan.features.divination.dataset import hexagram_data
from ytla_plan.features.divination.process import processModulePlumYi

def time_solver(day:str):
    print(day)
    hour_schema = ['00', '01', '03', '05', '07', '09', '11', '13', '15', '17', '19', '21', '23']
    for hour in hour_schema:
        time_str = f"{day} {hour}时01分"

        date = processModulePlumYi.trigram_generator_by_datetime(time_str)
        hexagram = processModulePlumYi.hexagram_generator(date[6], date[7], date[8])

        print(
            f"{hour}时 {hexagram[0]}({hexagram_data.hexagram_table.get(hexagram[5])[1]}) {hexagram[1]}({hexagram_data.hexagram_table.get(hexagram[6])[1]}) {hexagram[2]}({hexagram_data.hexagram_table.get(hexagram[7])[1]})(*{date[8]}) {hexagram[3]}({hexagram_data.hexagram_table.get(hexagram[8])[1]}) {hexagram[4]}({hexagram_data.hexagram_table.get(hexagram[9])[1]})")


date = timeFormat.get_current_time_cn().split(' ')[0].replace('年0','年').replace('月0','月')
time_solver(date)
