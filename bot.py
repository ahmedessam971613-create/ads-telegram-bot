import telebot

TOKEN = "8023863490:AAHnNltKqNhA-gKKUvxdbg4Ajxz0yeK7-so"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "اهلا بيك 👋\nاضغط /ads لمشاهدة اعلان")

@bot.message_handler(commands=['ads'])
def ads(message):
    bot.send_message(message.chat.id, "📢 اعلان:\nhttps://example.com")

print("Bot is running...")
bot.infinity_polling()
