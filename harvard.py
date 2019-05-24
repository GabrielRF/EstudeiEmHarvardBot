import sys
import configparser
import textwrap
import telebot
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

config = configparser.ConfigParser()
config.sections()
config.read('bot.conf')

TOKEN = config['BOT']['TOKEN']

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Digite um nome e um curso.\n\nExemplo:\n<code>Tício, Medicina</code>",parse_mode='HTML')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message.from_user.id)
    Create_Image(message)

def Create_Image(message):
    bot.send_chat_action(message.from_user.id, 'upload_document')
    try:
        nome, curso = message.text.split(',')
    except ValueError:
        nome = message.text
        curso = 'Medicine'

    nome = nome.lower().title()
    curso = curso.title()

    text = ('{}')
    text = text.format(nome)
    text_wrap = text
    text2 = ('{}')
    text2 = text2.format(curso)
    text_wrap2 = text2


    fonte = ImageFont.truetype('eb-garamond.ttf', 70)
    fonte2 = ImageFont.truetype('eb-garamond.ttf', 50)
    img = Image.open('Certificate.jpg')

    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(text_wrap, font = fonte)
    w2, h2 = draw.textsize(text_wrap2, font = fonte2)
    draw.text(((1650-w)/2,600), text_wrap, (0,0,0), font = fonte)
    draw.text(((1650-w2)/2,780), text_wrap2, (163,31,45), font = fonte2)

    img.save(str(message.from_user.id) + '.jpg')
    photo = open(str(message.from_user.id) + '.jpg', 'rb')
    bot.send_photo(message.from_user.id, photo)
    os.remove(str(message.from_user.id) + '.jpg')
bot.polling(none_stop=True)

