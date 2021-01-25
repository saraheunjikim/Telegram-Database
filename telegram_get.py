import token_id
import telegram
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

token = token_id.token

bot = telegram.Bot(token=token)
print(bot.get_me())

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi!')


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Do you need help?')


def file_handler(Update, context: CallbackContext):
    file = context.bot.getFile(Update.message.document.file_id)
    print("file_id: " + str(Update.message.document.file_id))
    file.download()
    # Call file_organizer.py and organize files into sub folder based on its usage.


def main():
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.document, file_handler))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()