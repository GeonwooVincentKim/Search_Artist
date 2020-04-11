import telegram
from telegram.ext import Updater, CommandHandler
import time


class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = 561540338
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id=self.id, text=text)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()


class BotCK(TelegramBot):
    def __init__(self):
        self.token = '912709363:AAHx1AyZD1mfj-CQBDL-tUjk3nKfRHCZ568'
        TelegramBot.__init__(self, 'This is test..', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.sendMessage('Please Press "/stttaaarrt" to start this project.')
        self.updater.start_polling()
        time.sleep(5)
        self.updater.idle()

    # def regular_choice(self, update, context):
    #     self.text =
