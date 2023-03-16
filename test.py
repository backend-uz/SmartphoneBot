from tinydb import TinyDB, Query
from cartdb import Cart

cart = Cart('cartdb.json')

# data = {
#     'brand': 'samsung',
#     'doc_id': 1,
#     'chat_id': 123
# }

# cart.add("samsung", 3, 234)
# print(cart.get_cart(234))
cart.remove(234)