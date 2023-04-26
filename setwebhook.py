import telegram

TOKEN="5068535219:AAGjGSqbhPQZqI2YKFYbXzMuE1csb1LCdlo"
url = "https://lorotar.pythonanywhere.com/webhook"
bot = telegram.Bot(TOKEN)

# print(bot.delete_webhook())

print(bot.set_webhook(url))
# print(bot.get_webhook_info())