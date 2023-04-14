import telegram

TOKEN="5068535219:AAGpTjbeJuI4k7Y_suzILFEQqJHwgT6ZhM8"
url = "https://bacefap.pythonanywhere.com/webhook"
bot = telegram.Bot(TOKEN)

# print(bot.delete_webhook())

print(bot.set_webhook(url))
# print(bot.get_webhook_info())