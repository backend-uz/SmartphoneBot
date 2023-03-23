from tinydb import TinyDB, Query
from cartdb import Cart
from db import DB 

db = Cart("cartdb.json")

print(db.remove(1380674728))