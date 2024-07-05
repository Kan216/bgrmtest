import os
from PIL import Image
from io import BytesIO
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
from rembg import remove
from dotenv import load_dotenv

load_dotenv()

# Set your Telegram bot token as an environment variable
TELEGRAM_BOT_TOKEN = os.getenv(
    "T7461438988:AAG7L5qHUCFiwIYGIYrv-Uo3rZL9BnA5plw")


def start(update: Updater, context: CallbackContext) -> None:
    update.message.reply_text(
        'Hi! Send me a photo and I will remove the background.')


def handle_photo(update: Updater, context: CallbackContext) -> None:
    photo = update.message.photo[-1].get_file()
    photo.download('input.png')
    with Image.open('input.png') as img:
        output = remove(img)
        output.save('output.png')

    with open('output.png', 'rb') as output_file:
        update.message.reply_photo(output_file)


    def main():
        updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(MessageHandler(filters.photo, handle_photo))

        updater.start_polling()
        updater.idle()

    if __name__ == '__main__':
        main()
