import telebot
import random
API_TOKEN="6906730477:AAEVU6vQNTTH0jKqBUM-w5lcdK3dyKJFWIY"
bot=telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda _: True)
def knopka(message: telebot.types.Message):
    markup=telebot.types.ReplyKeyboardMarkup()
    markup.add(telebot.types.KeyboardButton("Мотивация"))
    bot.reply_to(message,"привет",reply_markup=markup)
@bot.message_handler(content_types=['text'])
def otv(message: telebot.types.Message):
    if message.text == "Мотивация":
        with open("мотивация.txt", "r", encoding="utf-8") as file:
            mot = file.read().split("\n")
        moti = random.choice(mot)
        bot.send_message(message.chat.id, text=moti)


bot.infinity_polling()
