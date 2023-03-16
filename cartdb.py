from tinydb import TinyDB

class Cart:
    def __init__(self,cart_path:str):
        self.db = TinyDB(cart_path)
        self.table = self.db.table('cart')


    def add(self, brand, doc_id, chat_id):
        """
        add card

        data = {
            'brand':brand,
            'doc_id': doc_id,
            chat_id: chat_id
            }
        """
        data = {
            'brand':brand,
            'doc_id': doc_id,
            'chat_id': chat_id
        }
        self.table.insert(data)

    def get_cart(self, chat_id):
        return self.table.get(chat_id=chat_id)
    
    def remove(self, chat_id):
        self.table.remove(chat_id=chat_id)
