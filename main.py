from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
import os
from db import DB
TOKEN=os.environ.get("TOKEN")

db = DB('db.json')

def start(update: Update, context: CallbackContext) -> None:
    bot = context.bot
    chat_id = update.message.chat.id
    btn1 = InlineKeyboardButton(text='🛍 View Products', callback_data="view_product_data")
    btn2 = InlineKeyboardButton(text='📦 View Cart', callback_data="viec_cart_data")
    btn3 = InlineKeyboardButton(text='📞 Contact Us', callback_data="contact_us_data")
    btn4 = InlineKeyboardButton(text='📝 About Us', callback_data="about_us_data")
    keyboard = InlineKeyboardMarkup([[btn1, btn2], [btn3, btn4]])
    bot.sendMessage(chat_id, "Assalomu alaykum! Xush kelipsiz.\nQuyidagi menyudan kerakli tugmani bosing!", reply_markup=keyboard)

def menu(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    btn1 = InlineKeyboardButton(text='🛍 View Products', callback_data="view_product_data")
    btn2 = InlineKeyboardButton(text='📦 View Cart', callback_data="viec_cart_data")
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
    brend = data.split('_')[-1]

    products = db.get_phone_list(brend)
    # create keyboard
    keyboard = [[], []]
    phone_text = f"1-10/{len(products)}\n\n"
    pr_range = 10

    for i, phone in enumerate(products[:pr_range], 1):
        phone_text += f"{i}. {phone['name']} {phone['memory']}\n"
        # create button
        btn = InlineKeyboardButton(
            text = str(i),
            callback_data=f"product_{brend}_{phone.doc_id}"
        )
        if i < 6:
            # 1 2 3 4 5
            keyboard[0].append(btn)
        else:
            # 6 7 8 9 10
            keyboard[1].append(btn)
    
    # btn1 = InlineKeyboardButton(text="⬅️", callback_data=f'nextleft_{brend}_{pr_range}')
    btn2 = InlineKeyboardButton(text="➡️", callback_data=f'nextright_{brend}_{pr_range}')
    keyboard.append([btn2])

    btn3 = InlineKeyboardButton(text="Brend", callback_data="view_product_data")
    keyboard.append([btn3])

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(phone_text, reply_markup=reply_markup)

def next_product(update, context):
    query = update.callback_query
    data = query.data.split('_')
    text, brend, pr_range = data

    pr_range = int(pr_range)
    products = db.get_phone_list(brend)

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
            callback_data=f"product_{brend}_{phone.doc_id}"
        )
        if i < 6:
            # 1 2 3 4 5
            keyboard[0].append(btn)
        else:
            # 6 7 8 9 10
            keyboard[1].append(btn)
    pr_range += 10
    # btn1 = InlineKeyboardButton(text="⬅️", callback_data=f'nextleft_{brend}_{pr_range}')
    btn2 = InlineKeyboardButton(text="➡️", callback_data=f'nextright_{brend}_{pr_range}')
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
    text, brend, doc_id = data

    phone = db.getPhone(brend, doc_id)
    price = phone['price']
    ram = phone['RAM']
    memory = phone['memory']
    name = phone['name']
    color = phone['color']
    img = phone['img_url']
    text = f"📲{name}\n\n🎨{color}\n💾{ram}/{memory}\n💰{price}\n\n@telefonBozor"
    btn1 = InlineKeyboardButton(text="Add Card", callback_data='add_card')
    btn2 = InlineKeyboardButton(text="❌", callback_data='removeproduct')
    keyboard = InlineKeyboardMarkup([
        [btn1, btn2]
    ])

    bot.send_photo(chat_id=query.message.chat.id, photo=img, caption=text, reply_markup=keyboard)
    

def add_card(update, context):
    query = update.callback_query
    query.answer("Done")

def remove_product(update, context):
    query = update.callback_query
    query.answer("Removed")

updater = Updater(token=TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CallbackQueryHandler(view_products, pattern="view_product_data"))
dp.add_handler(CallbackQueryHandler(menu, pattern="bosh_menu"))
dp.add_handler(CallbackQueryHandler(get_product, pattern="brend"))
dp.add_handler(CallbackQueryHandler(next_product, pattern="next"))
dp.add_handler(CallbackQueryHandler(get_phone, pattern="product"))
dp.add_handler(CallbackQueryHandler(add_card, pattern="add_card"))
dp.add_handler(CallbackQueryHandler(remove_product, pattern="removeproduct"))
updater.start_polling()
updater.idle()