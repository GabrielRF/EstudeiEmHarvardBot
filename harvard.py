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
    bot.reply_to(message, "Digite um nome",parse_mode='HTML')

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
        curso = '@EstudeiEmHarvardBot'

    nome = nome.lower().title()
    curso = curso.title()

    text = ('{}')
    text = text.format(nome, curso)
    text_wrap = text

    fonte = ImageFont.truetype('eb-garamond.ttf', 70)
    img = Image.open('Certificate.jpg')

    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(text_wrap, font = fonte)
    draw.text(((1650-w)/2,600), text_wrap, (0,0,0), font = fonte)

    img.save(str(message.from_user.id) + '.jpg')
    photo = open(str(message.from_user.id) + '.jpg', 'rb')
    bot.send_photo(message.from_user.id, photo)
    os.remove(str(message.from_user.id) + '.jpg')
bot.polling(none_stop=True)

