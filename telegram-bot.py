print("123")
from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
print("hellowrolds")
updater = Updater(token='787331724:AAHevwMH4qKxRhwMCqbzaONnu6bzp_cnMRI', use_context=True)

dispatcher = updater.dispatcher
print("hellowrold")
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
print("hellowrold2")
def update():
    updater.start_polling()
print("hellowrold3")
update()
print("hellowrold")
