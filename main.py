import telegram

import Constants as keys
from telegram.ext import *
import Responses as R

print("Bot Iniciado...")

def start_command(update,context ):
    update.message.reply_text('Hola Humano, Soy un bot')

def help_command(update,context ):
    update.message.reply_text('Utiliza los comandos /start y /bot tambien puedes saludarme o preguntar por la hora')

def infoBot_command(update,context ):
    update.message.reply_text('Aqui esta la informacion de este Bot')

def handle_message(update,context):
    text=str(update.message.text).lower()
    response=R.sample_respondes(text)

    update.message.reply_text(response)

def error(update,context):
    print(f"update {update} cause error {context.error}")


def main():
    #obtener la informacion del bot
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("Bot", infoBot_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling() #pregunta por los mensajes entrantes
    updater.idle() #terminar el comando con ctrl+c

main()

print(f"update {update} cause error {context.error}")