import telebot
import random
random_nums = ['69', '29', '21', '375', '64', '12', '03', '812']

token = "************************************"

bot = telebot.TeleBot(token)

HELP = """
/help - напечатать справку
/book - добавить бронь
(в формате "номер стола"_"дата дд.мм.гг.")
/asap - добавить бронь на случайный стол на сегодня
/mytime - отбразить информацию о моей брони """


@bot.message_handler(commands=["help","HELP"])
def help(message):
    bot.send_message(message.chat.id, HELP)

books = {}

def add_todo(data, num):
  if data in books:
    books[data].append(num)
  else:
    books[data] = []
    books[data].append(num)

@bot.message_handler(commands=["book","BOOK"])
def book(message):
    command = message.text.split(maxsplit=2)
    num = command[1]
    data = command[2].lower()
    add_todo(data, books)
    text = "Бронь принята на стол № " + num + ", на дату " + data + "."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["asap", "ASAP"])
def ramdom_add(message):
    num = random.choice(random_nums)
    data = "сегодня"
    add_todo(data, books)
    text = "Бронь принята на стол № " + num + ", на " + data + "."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["mytime","MYTIME"])
def mytime(message): # message.text = /print <data>
    command = message.text.split(maxsplit=1)
    data = command[1].lower()
    text = ""
    if data in books:
        text = data.upper() + "\n"
        for num in books[data]:
            text = text + "[]" + "забронирован стол № " + str(num) + "\n"
    else:
        text = "Бронирований на дату нет"
    bot.send_message(message.chat.id, text)



bot.polling(none_stop=True)
