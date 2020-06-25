'''2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.'''

user_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# user_list = [100, 3, 23, 41, 55, 43, 2, 56]
new_list = []

def my_func(func, data):
    for itm in data:
        yield func(itm)

res = my_func((lambda x: x), user_list[1:])

for itm in user_list:
    try:
        result = next(res)
        if result > itm:
            new_list.append(result)
    except StopIteration:
        break

print(f'Исходный список: {user_list}')
print(f'Результат: {new_list}')