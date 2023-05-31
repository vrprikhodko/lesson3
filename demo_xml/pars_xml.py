import xml.etree.ElementTree as parser #as parser это псевдоним, что бы не писать везде xml.etree.ElementTree
tree = parser.parse('store.xml') #Объект tree получает всю информацию о файле store.xml
root = tree.getroot()
print(root)

for item in root:
    print(item.tag, ': ', item.text, sep=" ")
    for i in item:
        print(i.tag, ': ', i.text, sep=" ")
