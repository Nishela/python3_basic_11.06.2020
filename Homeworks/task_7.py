'''7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Итоговый список сохранить в виде json-объекта в соответствующий файл.'''

import json

dict = {}
av_prof = {}
result_list = []
prof = 0
counter = 0

with open('task_7_data.txt') as file:
    for line in file:
        firm, own, proceeds, costs = line.split()
        profit = float(proceeds) - float(costs)
        dict[firm] = profit
        if dict[firm] >= 0:
            prof += dict[firm]
            counter += 1
    if counter > 0:
        avg_profit = prof / counter
        av_prof['Средняя прибыль'] = avg_profit
    else:
        print('Средняя прибыль отсутствует. Все фирмы работают в убыток!')
        av_prof['Средняя прибыль'] = 'отсутствует!'
    result_list.append(dict)
    result_list.append(av_prof)

with open('task_7_result.json', 'w') as file_j:
    json.dump(result_list, file_j, ensure_ascii=False)
    print(f'Результат записан в файл: {file_j.name}')

print(f'Итоговый список: {result_list}')
