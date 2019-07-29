print("Зад1. Есть два словаря. Один - рецепт, второй - список продуктов в холодильнике. Сравнить два словаря. "
      "Составить список покупок.")
co = {"meat": 3, "onion": 1, "pesto": 100, "pasta": 200}
ref = {"milk": 100, "bread": 1, "meat": 4, "pasta": 100, "pesto": 100}
sp = {}
print("Рецепт: {0}".format(co))
print("Продукты в холодильнике: {0}".format(ref))
for i in co.keys():
    if i not in ref.keys():
       str = i
       sp[str] = co[str]
    elif ref[i] < co[i]:
        sp[i] = co[i] - ref[i]
if sp == {}:
    print("В вашем холодильнике есть все нужное для приготовления блюда!")
else:
    print("Необходимый список покупок: {0}".format(sp))


