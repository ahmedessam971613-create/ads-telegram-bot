import telebot
from telebot import types

TOKEN = "8023863490:AAGHTmckgSlJOv17oE8NfAFrrAgQaA9tc4g"

bot = telebot.TeleBot(TOKEN)

users = {}

BOT_USERNAME = "EarnnAds_bot"


def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📺 مشاهدة إعلان / Watch Ad")
    markup.add("💰 رصيدي / Balance")
    markup.add("👥 دعوة الأصدقاء / Invite Friends")
    return markup


@bot.message_handler(commands=['start'])
def start(message):

    user_id = message.from_user.id

    if user_id not in users:
        users[user_id] = 0

    bot.send_message(
        message.chat.id,
        "👋 اهلا بك\nWelcome\n\nاختر من القائمة",
        reply_markup=main_menu()
    )


@bot.message_handler(func=lambda m: m.text == "📺 مشاهدة إعلان / Watch Ad")
def ads(message):

    bot.send_message(
        message.chat.id,
        "📢 إعلان\n\nhttps://example.com\n\nبعد المشاهدة اكتب /done"
    )


@bot.message_handler(commands=['done'])
def done(message):

    user_id = message.from_user.id

    users[user_id] += 5

    bot.send_message(message.chat.id, "تم إضافة 5 نقاط")


@bot.message_handler(func=lambda m: m.text == "💰 رصيدي / Balance")
def balance(message):

    user_id = message.from_user.id

    points = users.get(user_id, 0)

    bot.send_message(
        message.chat.id,
        f"رصيدك: {points} نقطة"
    )


@bot.message_handler(func=lambda m: m.text == "👥 دعوة الأصدقاء / Invite Friends")
def refer(message):

    link = f"https://t.me/{BOT_USERNAME}?start={message.from_user.id}"

    bot.send_message(
        message.chat.id,
        f"رابط الدعوة الخاص بك:\n{link}\n\nكل صديق = 10 نقاط"
    )


print("Bot is running...")

bot.infinity_polling()
