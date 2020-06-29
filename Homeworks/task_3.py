'''3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.'''

def salarys(data):
    sal = 0
    quantity = len(data)
    for value in data.values():
        sal += int(value)
    return sal // quantity

with open('task_3_data.txt') as file:
    dic = {}
    for line in file.readlines():
        lst = line.split(',')
        dic[lst[0]] = lst[1]
    for key, value in dic.items():
        if int(value) < 20000:
            print(f'У сотрудника с фамилией {key} оклад менее 20000.')
    avg_sal = salarys(dic)
    print(f'Средняя величина дохода сотрудников: {avg_sal}')