'''6. * Реализовать структуру данных «Товары».'''

products = [
(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
(2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
(3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]
new_dict = {}

for item in products:
    dic = item[1]
    for key in dic:
        if key not in new_dict:
            new_dict[key] = [dic[key]]
        else:
            new_dict[key].append(dic[key])
print(new_dict)
