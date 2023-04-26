from flask import Flask, request
from telegram import Update
from telegram.ext import Dispatcher, CommandHandler, CallbackQueryHandler
import telegram
from handlers import start, menu, view_products, get_product, next_product,  get_phone, addcart, clear_cart, remove_message, view_cart, contact_us
TOKEN = "5068535219:AAGjGSqbhPQZqI2YKFYbXzMuE1csb1LCdlo"

bot = telegram.Bot(TOKEN)

app = Flask(__name__)

@app.route("/webhook", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        dp = Dispatcher(bot, None, workers=0)

        data = request.get_json(force=True)
        update = Update.de_json(data, bot)

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CallbackQueryHandler(view_products, pattern="view_product_data"))
        dp.add_handler(CallbackQueryHandler(menu, pattern="bosh_menu"))
        dp.add_handler(CallbackQueryHandler(get_product, pattern="brend"))
        dp.add_handler(CallbackQueryHandler(next_product, pattern="next"))
        dp.add_handler(CallbackQueryHandler(get_phone, pattern="product"))
        dp.add_handler(CallbackQueryHandler(addcart, pattern="addcart"))
        dp.add_handler(CallbackQueryHandler(clear_cart, pattern="clearcart"))
        dp.add_handler(CallbackQueryHandler(remove_message, pattern="removemessage"))
        dp.add_handler(CallbackQueryHandler(view_cart, pattern="view_cart_data"))
        dp.add_handler(CallbackQueryHandler(contact_us, pattern="contact_us_data"))

        dp.process_update(update)

        return "ok"
    else:
        return "Not allowed get request"
    
if __name__ == "__main__":
    app.run(debug=True)