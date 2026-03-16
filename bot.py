import telebot
from telebot import types

TOKEN = "8023863490:AAEfSffHWQv4F3XHQubG2TkerW_t4WDuWvY"

bot = telebot.TeleBot(TOKEN)

BOT_USERNAME = "EarnnAds_bot"

ADMIN_ID = 123456789

users = {}
ads_text = "https://example.com"


def menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📺 مشاهدة إعلان")
    markup.add("💰 رصيدي")
    markup.add("👥 دعوة الأصدقاء")
    markup.add("💵 سحب الأرباح")
    return markup


@bot.message_handler(commands=['start'])
def start(message):

    user_id = message.from_user.id

    if user_id not in users:
        users[user_id] = 0

    bot.send_message(
        message.chat.id,
        "👋 اهلا بك في بوت الربح\n\nاختر من القائمة",
        reply_markup=menu()
    )


@bot.message_handler(func=lambda m: m.text == "📺 مشاهدة إعلان")
def ads(message):

    bot.send_message(
        message.chat.id,
        f"📢 إعلان\n\n{ads_text}\n\nبعد        f"💰 طلب سحب جديد\n\nUser ID: {user_id}\nWallet: {wallet}"
    )


print("Bot is running...")

bot.infinity_polling()
