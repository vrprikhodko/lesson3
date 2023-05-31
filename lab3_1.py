from random import randint
list1 = [randint(0, 9) for item in range(3)]
list2 = [randint(0, 9) for item in range(3)]
# print(list1)
try:
    for i in range(3):
        res = list1[i] / list2[i]
        print(f"Деление {list1[i]} / {list2[i]} = {res}")
except ZeroDivisionError:
    print(f"На ноль делить нельзя")
