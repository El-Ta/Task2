print("Зад1. Пользователь водит текст. Необходимо выдать статистику.")
import string
L = input("Введите любую строку:")
str = []
j = 0
m = 0
for i in range(len(L)):
    if L[i] == ' ':
        str.append(L[m:i])
        m = i+1
if L[len(L)-1] != ' ':
    str.append(L[m:len(L)])
for i in L:
    if i in string.ascii_letters:
        j+=1
print('Количество слов в строке: {0}, количество английских букв: {1}'.format(len(str), j))

print("Зад2. Пользователь вводит два текста. Необходимо выписать слова, содержащиеся в обоих списках")
A = input("Введите первую строку:")
B = input("Введите вторую строку:")
a = 0
b = 0
strA = []
strB = []
strC = []
for i in range(len(A)):
    if A[i] == ' ':
        strA.append(A[a:i])
        a = i+1
if A[len(A)-1] != ' ':
    strA.append(A[a:len(A)])
for i in range(len(B)):
    if B[i] == ' ':
        strB.append(B[b:i])
        b = i+1
if B[len(B)-1] != ' ':
    strB.append(B[b:len(B)])
for i in strA:
    if i in strB:
        strC.append(i)
print("Итоговая строка: {0}".format(strC))