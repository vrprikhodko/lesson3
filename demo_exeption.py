# Обработка ошибок try/except
#     где возможны ошибки вносим в try например деление на ноль
#

# пример 1
# from random import randint
# num1 = 10
# num2 = randint(0,2)
# try:
#     print(num1 / num2)
#     print("num2 !=0")
# except ZeroDivisionError as e: #В e записываем текст ошибки. по желанию
#     print(f"На ноль делить нельзя {e.__doc__}") # В e.__doc__ выводим стандартный текст ошибки заложенной в python

# пример 2
# while True: # бесконечный цикл
#     first_num = input("Введите первое число")
#     if first_num == "q":
#         break
#     second_num = input("Введите второе число")
#     if second_num == "q":
#         break
#     try:
#         res = int(first_num) / int(second_num)
#     except ZeroDivisionError:
#         print(f"На ноль делить нельзя")
#     except ValueError: # ошибка если ввели не число и не q
#         print(f"Не число")
#     except: #любая ошибка кроме перечисленных выше
#         print("Возникла непредвиденная ошибка")
#     else: #данный блок выполнится если не было ошибки
#         print(f"Деление {res}")

# пример 3
# my_file = 'test.txt'
# try:
#     file = open(my_file,"r")
#     content = file.readlines()
#     file.close()
# except FileNotFoundError: #Если такого файла нет
#     print("Файл не найден")

# пример 4
# Блок finally может находиться после trt или except. Все что в finally выполнится обязательно
# my_file = 'test.txt'
# file = None
# try:
#     file = open(my_file,"r")
#     content = file.readlines()
#     x = 2 / 0
# except Exception as e: #Если возникла любая ошибка, то запишем текст ошибки в е
#     print(f"{e.__doc__}")
# finally: #данный блок выполняется всегда
#     if file != None:
#         file.close()
#         print("Файл закрыт")
#     print("Файл не существует")


# пример 5
#
# step = 0
# while True:
#     number = int(input("Введите целое число\n"))
#     if 20 <= number <= 40:
#         print("Принимается")
#         break
#     else:
#         step += 1
#         if step == 3:
#             raise Exception("Вы ввели некорректное значение 3 раза") #красыем цветом будет эта ошибка
#         else:
#             print("Попробуйт еще раз")
