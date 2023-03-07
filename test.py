from tinydb import TinyDB

db = TinyDB('db.json')

tables = ['apple', 'vivo', 'samsung', 'xiaomi', 'huawei']

table1 = db.table(tables[1])
print(table1.all()[0])