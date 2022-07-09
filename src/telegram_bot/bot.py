import telebot
import time
# Токен, который выдает @botfather
bot = telebot.TeleBot('5463575495:AAEgouiBhQUo_Ie776_akq5gemfjVkoa7cw')
# Адрес телеграм-канала, начинается с @
CHANNEL_NAME = '-671436631'
# Загружаем список шуток
# f = open('data/fun.txt', 'r', encoding='UTF-8')
# jokes = f.read().split('\n')
# f.close()
jokes = [1, 2]
# Пока не закончатся шутки, посылаем их в канал
for joke in jokes:
    bot.send_message(CHANNEL_NAME, joke)
    # Делаем паузу в один час
    time.sleep(5)
bot.send_message(CHANNEL_NAME, "Анекдоты закончились :-(")

# https://cms3.ru/kak-poluchit-chat-id-telegram/
# https://pythonist.ru/telegram-bot-na-python-dlya-generaczii-sluchajnyh-czitat/