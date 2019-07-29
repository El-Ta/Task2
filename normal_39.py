print("Зад1. Получить список с произвольными числами. Из каждого элемента взять квадратный корень, если это возможно")
import random
import math
n = random.randint(5, 10)
lst = []
for i in range(n):
    lst.append(random.randint(-28, 50))
print("Исходный список: {0}".format(lst))
res = []
for i in lst:
    if i <= 0:
        continue
    n = math.sqrt(i)
    if (n).is_integer():
        res.append(n)
print("Итоговый список: {0}".format(res))

print("Зад2. Вывести введенную дату в текстовом виде.")
c = input("Введите дату в формате dd/mm/yyyy:")
v = True
if len(c) != 10:
    print("Неверный формат")
    v = False
else:
    for i in range(len(c)):
        if i == 2 or i == 5:
            continue
        else:
            try:
                a = int(c[i])
            except ValueError:
                print("Неверный формат")
                v = False
                break
if v:
    d = int(c[0:2])
    m = int(c[3:5])
    y = int(c[6:10])
    import datetime

    if (d > 0 and d<32 and m > 0 and m < 13):
        now = datetime.date(y, m, d)
        date = ["первое", "второе", "третье", "четвертое", "пятое", "шестое", "седьмое", "восьмое", "девятое", "десятое",
            "одиннадцатое", "двенадцатое", "тринадцатое", "четырнадцатое", "пятнадцатое", "шестнадцатое", "семнадцатое",
            "восемнадцатое", "девятнадцатое", "двадцатое", "двадцать первое", "двадцать второе", "двадцать третье",
            "двадцать четвертое", "двадцать пятое", "двадцать шестое", "двадцать седьмое", "двадцать восьмое",
            "двадцать девятое", "тридцатое", "тридцать первое"]
        mon = ["января", "февраля","марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября",
           "декабря"]
        print('{0} {1} {2} года, {3}'.format(date[d-1], now.strftime("%B"), y, now.strftime("%A")))
        print('{0} {1} {2} года'.format(date[d - 1], mon[m-1], y))
    else:
        print("Неверный формат")
