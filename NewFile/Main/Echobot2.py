import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Enable Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError
def start(update, context):
    """ Send a Message when the command /start is issued."""
    update.message.reply_text('Hello! How can I help you?')


def start_kor(update, context):
    """ Send a Message when the Command /도움 is issued. """
    update.message.reply_text("안녕하세요! 어떻게 도와드릴까요?")


def help(update, context):
    """ Send a Message when the command /help is issued."""
    update.message.reply_text('This is Help. How can I help you?')


def echo(update, context):
    """ Echo the user message. """
    update.message.reply_text(update.message.text)


def error(update, context):
    """ Log Errors caused by Updates. """
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """ Start the bot. """
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("912709363:AAHx1AyZD1mfj-CQBDL-tUjk3nKfRHCZ568", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different command - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(CommandHandler("시작", start_kor))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
