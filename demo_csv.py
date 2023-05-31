# import csv
# from csv import *
# persons = [
#     ["Иван",800],
#     ["Петр",900],
#     ["Федор",1000]
# ]
# cars = [
#     {
#         "title":"Audi",
#         "price":100,
#         "color":"red"
#     },
#     {
#         "title": "BMW",
#         "price": 200,
#         "color": "green"
#     }
#
# ]
# # запись в файл csv
# with open('persons.csv','w',newline='') as file: #newline='' что бы не было пустых строк
#     obj = csv.writer(file,delimiter=';') #объект через который обращаемся к методам delimiter=';' - меняет стандатную запятую как разделитель на точку_с_запятой
#     obj.writerows(persons)
# добавить в файл csv
# with open('persons.csv','a',newline='') as file: #newline='' что бы не было пустых строк
#     obj = csv.writer(file) #объект через который обращаемся к методам
#     obj.writerow(["Анна",587])
# # чтение из файла csv
# with open('persons.csv','r') as file: #newline='' что бы не было пустых строк
#     obj = csv.reader(file) #объект через который обращаемся к методам
#     for line in obj:    #line списко полученный из строки нашего файла
#         print(f"Имя {line[0]} - Оклад {line[1]} руб.")
# # запись списка словарей в файл csv
# with open('cars.csv','w',newline='') as file: #newline='' что бы не было пустых строк
#     columns = ['title','price','color']
#     obj = csv.DictWriter(file,fieldnames=columns) #объект через который обращаемся к методам
#     obj.writeheader() #Записываем заголовок
#     obj.writerows(cars)

