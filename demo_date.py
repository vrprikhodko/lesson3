from datetime import *
now = datetime.today() #текущая дата
print(now)
print(now.strftime("%d.%m.%y")) #печатаем тек дату в формате дд.мм.гггг
old_date = datetime(2022,12,31) #какая то дата
print(now - old_date) #количество дней времени от текущей даты до старой
print(now.year) #вывести текущий год
