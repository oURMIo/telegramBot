import telebot
import conf
#import datetime
import time

bot = telebot.TeleBot(conf.TOKEN)


@bot.message_handler(commands=['help', 'loli'])
def helping(message):
    bot.reply_to(message, "NOOOOOOO")


# #REPID
# @bot.message_handler(content_types=['text'])
# def repid(message):
#     bot.send_message(message.chat.id, message.text)


#write in file INFA.txt
@bot.message_handler(commands=['start'])
def filesave(message):
    # iduser = message.from_user.id
    # bot.reply_to(message, iduser)
    bot.reply_to(message, "Hello (〃￣︶￣)人(￣︶￣〃)")
    file = open('INFA.txt', 'a+')
    file.write(str(message.from_user.id) + " || " + str(time.ctime()) + '\n')
    file.close()


# START
bot.polling(none_stop=True)
