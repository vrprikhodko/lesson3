# +7(9NN)-NNN-NN-NN

from re import *
rule = "^\+7\(9[0-9]{2}\)-[0-9]{3}-[0-9]{2}-[0-9]{2}$"
if fullmatch(rule,"+7(999)-991-99-11"):
    print("Номер корректный")
else:
    print("Номер не корректный")