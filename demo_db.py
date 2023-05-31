from pprint import pprint

import pymysql.cursors
from pymysql import *

connect = connect(host="localhost",
                  user="user",
                  password="user123",
                  database="lesson03",
                  cursorclass=pymysql.cursors.DictCursor #для возможно работ с табл из словоря
                  )
def update(cur):
    info = input("Введитеqqqqw11 наименование товара и новую стоимость через пробел\n").split(" ")
    sql = f"UPDATE goods SET price = {int(info[1])} WHERE title = '{info[0]}'"
    if cur.execute(sql) > 0:
        print("Обновлено")
def select(cur):
    cur.execute("select * from goods")
    rows = cur.fetchall()
    pprint(rows)
    # for item in rows:
with connect:
    cur = connect.cursor() #объект с помощью которого можно выполнять любы sql запросы на сервере
    select(cur)
    update(cur)
    select(cur)
    connect.commit() #Запись update

