from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
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

    brend_data = db.get_phone_list(brend)
    phone = brend_data[0]
    price = phone['price']
    ram = phone['ram']
    memory = phone['memory']
    name = phone['brend']
    color = phone['color']
    img = phone['img_url']

    text = f"📲{name}\n\n🎨{color}\n💾{ram}/{memory}GB\n💰{price}\n\n@telefonBozor"
    print(chat_id)
    bot.sendPhoto(chat_id, photo=img, caption=text)
    query.answer('Done!')

updater = Updater(token=TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CallbackQueryHandler(view_products, pattern="view_product_data"))
dp.add_handler(CallbackQueryHandler(menu, pattern="bosh_menu"))
dp.add_handler(CallbackQueryHandler(get_product, pattern="brend"))
updater.start_polling()
updater.idle()