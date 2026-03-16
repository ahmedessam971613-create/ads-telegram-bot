import telebot
from telebot import types

TOKEN = "8023863490:AAHnNltKqNhA-gKKUvxdbg4Ajxz0yeK7-so"
bot = telebot.TeleBot(TOKEN)

users = {}
referrals = {}

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📺 مشاهدة إعلان")
    markup.add("💰 رصيدي", "👥 دعوة الأصدقاء")
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if user_id not in users:
        users[user_id] = 0

    args = message.text.split()
    if len(args) > 1:
        ref = args[1]
        if ref != str(user_id):
            referrals.setdefault(ref, 0)
            referrals[ref] += 1
            users[int(ref)] += 10

    bot.send_message(message.chat.id,
                     "اهلا بيك 👋\nاختر من القائمة",
                     reply_markup=main_menu())

@bot.message_handler(func=lambda m: m.text == "📺 مشاهدة إعلان")
def ads(message):
    bot.send_message(message.chat.id,
                     "📢 إعلان:\nhttps://example.com\n\nبعد المشاهدة اكتب /done")

@bot.message_handler(commands=['done'])
def done(message):
    user_id = message.from_user.id
    users[user_id] += 5
    bot.send_message(message.chat.id, "✅ تم إضافة 5 نقاط")

@bot.message_handler(func=lambda m: m.text == "💰 رصيدي")
def balance(message):
    user_id = message.from_user.id
    points = users.get(user_id, 0)
    bot.send_message(message.chat.id, f"رصيدك: {points} نقطة")

@bot.message_handler(func=lambda m: m.text == "👥 دعوة الأصدقاء")
def refer(message):
link = f"https://t.me/ads_telegram_bot?start={message.from_user.id}""
    bot.send_message(message.chat.id,
                     f"رابط الدعوة الخاص بك:\n{link}\n\nكل صديق = 10 نقاط")

print("Bot running...")
bot.infinity_polling()
