import telebot
import random
API_TOKEN="6906730477:AAEVU6vQNTTH0jKqBUM-w5lcdK3dyKJFWIY"
bot=telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def knopka(message):
    markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton("Мотивация"))
    bot.send_message(message.chat.id,"Привет! У тебя что пропало желание что-либо делать? Я помогу тебе с мотивацией!.",reply_markup=markup)

@bot.message_handler(content_types=["text"])
def any_msg(message):
    if message.text == "Мотивация":
        with open("Мотивация.txt", "r", encoding="utf-8") as file:
            mot = file.read().split("\n")
        moti = random.choice(mot)
        bot.send_message(message.chat.id, text=moti)


bot.infinity_polling()
