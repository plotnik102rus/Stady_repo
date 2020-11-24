#Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.....

import json

firm_dict = {}
average_profit = []
with open('task5_7.txt') as f:
    lines = f.readlines()
    for line in lines:
        name, form, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firm_dict[name] = profit
        if profit > 0:
            average_profit.append(profit)

average_profit = sum(average_profit) / len(average_profit)
out_info = [firm_dict, {'average_profit': average_profit}]

with open('7.json', 'w') as f_json:
    json.dump(out_info, f_json)

with open('7.json') as f_json:
    print(json.load(f_json))