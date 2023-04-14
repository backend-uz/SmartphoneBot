from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackContext
from cartdb import Cart
cart = Cart('cartdb.json')
from db import DB
db = DB('db.json')

def start(update: Update, context: CallbackContext) -> None:
    bot = context.bot
    chat_id = update.message.chat.id
    btn1 = InlineKeyboardButton(text='🛍 View Products', callback_data="view_product_data")
    btn2 = InlineKeyboardButton(text='📦 View Cart', callback_data="view_cart_data")
    btn3 = InlineKeyboardButton(text='📞 Contact Us', callback_data="contact_us_data")
    btn4 = InlineKeyboardButton(text='📝 About Us', callback_data="about_us_data")
    keyboard = InlineKeyboardMarkup([[btn1, btn2], [btn3, btn4]])
    bot.sendMessage(chat_id, "Assalomu alaykum! Xush kelipsiz.\nQuyidagi menyudan kerakli tugmani bosing!", reply_markup=keyboard)

def menu(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    btn1 = InlineKeyboardButton(text='🛍 View Products', callback_data="view_product_data")
    btn2 = InlineKeyboardButton(text='📦 View Cart', callback_data="view_cart_data")
    btn3 = InlineKeyboardButton(text='📞 Contact Us', callback_data="contact_us_data")
    btn4 = InlineKeyboardButton(text='📝 About Us', callback_data="about_us_data")
    keyboard = InlineKeyboardMarkup([[btn1, btn2], [btn3, btn4]])
    query.edit_message_text("Bosh Menu", reply_markup=keyboard)

def view_products(update: Update, context: CallbackContext)-> None:
    query = update.callback_query

    brends = db.get_tables()
    keyboard = []
    for brend in brends:
        btn = InlineKeyboardButton(
            text = brend.capitalize(),
            callback_data=f"brend_{brend}"
        )
        keyboard.append([btn])
    btn1 = InlineKeyboardButton(text="🏘 Bosh Menu", callback_data="bosh_menu")
    keyboard.append([btn1])

    keyboard = InlineKeyboardMarkup(keyboard)
    query.edit_message_text("Quyidagi brandlardan birini tanlang!", reply_markup=keyboard)

def get_product(update: Update, context: CallbackContext) -> None:
    bot = context.bot
    query = update.callback_query

    chat_id = query.message.chat.id
    data = query.data
    brand = data.split('_')[-1]

    products = db.get_phone_list(brand)
    # create keyboard
    keyboard = [[], []]
    phone_text = f"1-10/{len(products)}\n\n"
    pr_range = 10

    for i, phone in enumerate(products[:pr_range], 1):
        phone_text += f"{i}. {phone['name']} {phone['memory']}\n"
        # create button
        btn = InlineKeyboardButton(
            text = str(i),
            callback_data=f"product_{brand}_{phone.doc_id}"
        )
        if i < 6:
            # 1 2 3 4 5
            keyboard[0].append(btn)
        else:
            # 6 7 8 9 10
            keyboard[1].append(btn)
    
    # btn1 = InlineKeyboardButton(text="⬅️", callback_data=f'nextleft_{brend}_{pr_range}')
    btn2 = InlineKeyboardButton(text="➡️", callback_data=f'nextright_{brand}_{pr_range}')
    keyboard.append([btn2])

    btn3 = InlineKeyboardButton(text="Brend", callback_data="view_product_data")
    keyboard.append([btn3])

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(phone_text, reply_markup=reply_markup)

def next_product(update, context):
    query = update.callback_query
    data = query.data.split('_')
    text, brand, pr_range = data

    pr_range = int(pr_range)
    products = db.get_phone_list(brand)

    if len(products) < pr_range:
        pr_range = 0

    print(len(products), pr_range)
    keyboard = [[], []]
    phone_text = f"{pr_range}-{pr_range+10}/{len(products)}\n\n"

    for i, phone in enumerate(products[pr_range:pr_range+10], 1):
        phone_text += f"{i}. {phone['name']} {phone['memory']}\n"
        # create button
        btn = InlineKeyboardButton(
            text = str(i),
            callback_data=f"product_{brand}_{phone.doc_id}"
        )
        if i < 6:
            # 1 2 3 4 5
            keyboard[0].append(btn)
        else:
            # 6 7 8 9 10
            keyboard[1].append(btn)
    pr_range += 10
    # btn1 = InlineKeyboardButton(text="⬅️", callback_data=f'nextleft_{brend}_{pr_range}')
    btn2 = InlineKeyboardButton(text="➡️", callback_data=f'nextright_{brand}_{pr_range}')
    keyboard.append([btn2])
    btn3 = InlineKeyboardButton(text="Brend", callback_data="view_product_data")
    keyboard.append([btn3])
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(phone_text, reply_markup=reply_markup)
    query.answer("Next")

def get_phone(update, context):
    bot  = context.bot
    query = update.callback_query
    data = query.data.split('_')
    text, brand, doc_id = data
    # text
    phone = db.getPhone(brand, int(doc_id))
    price = phone['price']
    ram = phone['RAM']
    memory = phone['memory']
    name = phone['name']
    color = phone['color']
    img = phone['img_url']
    text = f"📲{name}\n\n🎨{color}\n💾{ram}/{memory}\n💰{price}\n\n@telefonBozor"
    # text
    btn1 = InlineKeyboardButton(text="🛒 Add Card", callback_data=f'addcart_{brand}_{doc_id}')
    btn2 = InlineKeyboardButton(text="❌", callback_data='removemessage')
    keyboard = InlineKeyboardMarkup([
        [btn1, btn2]
    ])
    bot.send_photo(chat_id=query.message.chat.id, photo=img, caption=text, reply_markup=keyboard)

def addcart(update, context):
    # bot = context.bot
    query = update.callback_query
    data = query.data.split('_')
    callback, brand, doc_id = data
    chat_id = query.message.chat.id
    add_cart = cart.add(brand=brand, doc_id=doc_id, chat_id=chat_id)
    btn1 = InlineKeyboardButton(text="🛒 Savatni bo'shatish", callback_data=f'clearcart_{brand}_{doc_id}')
    btn2 = InlineKeyboardButton(text='❌', callback_data='removemessage')
    keyboard = InlineKeyboardMarkup([[btn1, btn2]])
    query.edit_message_reply_markup(reply_markup=keyboard)
    query.answer("Qo'shildi✅")

def clear_cart(update, context):
    query = update.callback_query
    chat_id = query.message.chat.id
    data = query.data.split('_')
    callback, brand, doc_id = data
    clear_cart = cart.remove(chat_id=chat_id)
    btn1 = InlineKeyboardButton(text="🛒 Add Card", callback_data=f'addcart_{brand}_{doc_id}')
    btn2 = InlineKeyboardButton(text="❌", callback_data="removemessage")
    keyboard = InlineKeyboardMarkup([[btn1, btn2]])
    query.edit_message_reply_markup(reply_markup=keyboard)
    query.answer("🛒 Cart Is Empty Now")

def remove_message(update, context):
    query = update.callback_query
    bot = context.bot
    chat_id = query.message.chat.id
    bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
    query.answer('deleted')

def view_cart(update, context):
    bot = context.bot
    query = update.callback_query
    chat_id = query.message.chat.id
    view = cart.get_cart(chat_id=chat_id)
    total = 0

    text = '1'
    for i in view:
        view_cart = cart.get_cart(chat_id=chat_id)
        brand = view_cart[0]['brand']
        doc_id = view_cart[0]['doc_id']
        chat_id2 = view_cart[0]['chat_id']
        phone = db.getPhone(brand=brand, idx=int(doc_id))
        # text
        brand = phone['company']
        name = phone['name']
        ram = phone['RAM']
        memory = phone['memory']
        price = phone['price']
        total = + price
        text + f'\nSiz tanlagan maxsulotlar quyidagilar👇\n📱 {brand} — {name}\n💾 {ram}/{memory}\n💰 {price}'
        print(total)
    bot.send_message(chat_id, text)

def contact_us(update, context):
    bot = context.bot
    chat_id = update.message.chat.id
    btn1 = InlineKeyboardButton(text="Phone Number", callback_data="phone_number")
    btn2 = InlineKeyboardButton(text="Adress", callback_data="adress")
    btn3 = InlineKeyboardButton(text="Location", callback_data="location")
    btn4 = InlineKeyboardButton(text="Email", callback_data="email")
    keybpoard = InlineKeyboardMarkup([[btn1, btn2], [btn3, btn4]])
