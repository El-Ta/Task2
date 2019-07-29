print("Зад1. Вывести список продуктов в виде нумерованного списка, выравненного по правой стороне.")
lst = ['яблоко', 'апельсин', 'ананас', 'виногрaд']
for i in range(len(lst)):
    print('{0:>20}.{1}'.format(i+1, lst[i]))

print("Зад2. Удалить из первого списка элементы, присутствующие во втором списке.")
lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [2, 10, 4, 6]
res = []
for i in lst1:
    if i not in lst2:
        res.append(i)
print('Первый список: {0}'.format(lst1))
print('Второй список: {0}'.format(lst2))
print('Итоговый список: {0}'.format(res))

print("Зад3. Если в списке элемент кратен 2, то делим его на 4. Если не кратен, то умножаем на 2")
import random
n = random.randint(5, 10)
lst = []
for i in range(n):
    lst.append(random.randint(1, 28))
print("Исходный список: {0}".format(lst))
res = []
for i in lst:
    if i % 2 == 0:
        res.append(i/4)
    else:
        res.append(i*2)
print("Итоговый список: {0}".format(res))