import logging
from Manage_OutFile import telegram
from time import sleep

from Manage_OutFile.build.lib.telegram.error import NetworkError, Unauthorized
update_id = 561540338


def main():
    global update_id
    bot = telegram.Bot('912709363:AAHx1AyZD1mfj-CQBDL-tUjk3nKfRHCZ568')

    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            print("There some NetworkError has been occured.\n")
            print("Please fix this issue!!!")
            sleep(1)
        except Unauthorized:
            update_id += 1


def echo(bot):
    """Echo the message the user sent."""
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        # Your bot can receive updates without Messages
        if update.message:
            # Reply to the Message
            update.message.reply_text(update.message.text)


if __name__ == "__main__":
    main()
