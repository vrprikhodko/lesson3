# Создать json строку с сотрудниками компании. У каждого есть
# имя и оклад.
# 1) Вывести информацию о каждом сотруднике
# 2) Найти сотрудника с максимальным окладом

import json

stafs_info = """{
    "stafs":[
        {
           "tab_id":112311,
           "fio":"Иванов Иван Иванович",
           "salary":100000
        },
        {
           "tab_id":115611,
           "fio":"Петров Иван Иванович",
           "salary":500000
        },
        {
           "tab_id":112431,
           "fio":"Сидоров Иван Иванович",
           "salary":120000
        }
    ] 
}"""
max_salary = 0
salary = 0
my_dict = json.loads(stafs_info)
for stafs in my_dict['stafs']:
    print(f"Сотрудник: {stafs['fio']} , Табельный номер: {stafs['tab_id']}, Оклад: {stafs['salary']}")
    salary = stafs['salary']
    if salary > max_salary:
        max_salary = salary
        staf_max_salary = stafs['fio']
print(f"Максимальный оклад {max_salary} у {staf_max_salary}")
