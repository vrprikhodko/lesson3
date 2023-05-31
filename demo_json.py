import json
info = """{
    "cars":[
        {
            "id":1,
            "title":"Audi",
            "price":100
        },
        {
            "id":2,
            "title":"Audi2",
            "price":120
        },
        {
            "id":3,
            "title":"Audi3",
            "price":130
        }   
    ]
    "shop":{
        "title":"Имя магазина",
        "address":"Адрес"
    }
}"""
# print(info)
my_dict = json.loads(info)
print(my_dict['cars'][1]['price'])
# s = 0
# for car in my_dict['cars']:
#     print(f"Автомобиль {car['title']} стоит {car['price']}")
#     s += car['price']
# print(f"сумма стоимости всех авто {s}")