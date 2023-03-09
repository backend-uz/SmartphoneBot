from tinydb import TinyDB, Query

db = TinyDB('db.json')

tables = ['apple', 'vivo', 'samsung', 'xiaomi', 'huawei']

table1 = db.table('apple')
print(table1.get(doc_id = 4))