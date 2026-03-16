import telebot
from telebot import types

TOKEN = "8023863490:AAEfSffHWQv4F3XHQubG2TkerW_t4WDuWvY"

bot = telebot.TeleBot(TOKEN)

users = {}

BOT_USERNAME = "EarnnAds_bot"

ADMIN_ID = 1541770886  # حط هنا Telegram ID بتاعك


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
        "👋 أهلا بك في بوت الربح\nWelcome\n\nاختر من القائمة",
        reply_markup=menu()
    )


@bot.message_handler(func=lambda m: m.text == "📺 مشاهدة إعلان")
def ads(message):

    bot.send_message(
        message.chat.id,
        "📢 إعلان\n\nhttps://example.com\n\nبعد المشاهدة اكتب /done"
    )


@bot.message_handler(commands=['done'])
def done(message):

    user_id = message.from_user.id

    users[user_id] += 5

    bot.send_message(message.chat.id, "✅ تم إضافة 5 نقاط")


@bot.message_handler(func=lambda m: m.text == "💰 رصيدي")
def balance(message):

    user_id = message.from_user.id

    points = users.get(user_id, 0)

    bot.send_message(
        message.chat.id,
        f"💰 رصيدك: {points} نقطة"
    )


@bot.message_handler(func=lambda m: m.text == "👥 دعوة الأصدقاء")
def refer(message):

    link = f"https://t.me/{BOT_USERNAME}?start={message.from_user.id}"

    bot.send_message(
        message.chat.id,
        f"👥 رابط الدعوة الخاص بك:\n\n{link}\n\nكل صديق = 10 نقاط"
    )


@bot.message_handler(func=lambda m: m.text == "💵 سحب الأرباح")
def withdraw(message):

    user_id = message.from_user.id
    points = users.get(user_id, 0)

    if points < 1000:
        bot.send_message(message.chat.id, "❌ الحد الأدنى للسحب 1000 نقطة")
    else:
        msg = bot.send_message(
            message.chat.id,
            "💳 ارسل عنوان محفظة TON الخاصة بك"
        )
        bot.register_next_step_handler(msg, process_wallet)


def process_wallet(message):

    wallet = message.text
    user_id = message.from_user.id

    bot.send_message(
        message.chat.id,
        "✅ تم إرسال طلب السحب للإدارة"
    )

    bot.send_message(
        ADMIN_ID,
        f"💰 طلب سحب جديد\n\nUser ID: {user_id}\nWallet: {wallet}"
    )


print("Bot is running...")

bot.infinity_polling()
