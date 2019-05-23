#!/usr/bin/env python

from logging import basicConfig, getLogger, INFO
from typing import Dict

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from variables import TOKEN


class EmojifyBot:
    def __init__(self):
        basicConfig(level=INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        self.logger = getLogger('bot')
        self.logger.info('starting bot')

        assert len(TOKEN) > 0, "no token provided"
        self.token = TOKEN

        self.bot = Bot(token=self.token)
        self.updater = Updater(self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher

        self.handlers: Dict = dict()
        self.handlers['start'] = CommandHandler('start', self.start_handler)
        self.handlers['info'] = CommandHandler('info', self.info_handler)
        self.handlers['creators'] = CommandHandler('creators', self.creators_handler)
        self.handlers['any_text'] = MessageHandler(Filters.text, self.any_text_handler)

        for handler in self.handlers:
            self.dispatcher.add_handler(self.handlers[handler])

        self.logger.info('started bot')

    def start_handler(self, update, context):
        self.logger.info(f'{update.message.chat.username} started bot')
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text="Send me any text and I'll try to add emoji to it")

    def info_handler(self, update, context):
        self.logger.info(f'{update.message.chat.username} requested information about the bot')
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text="me")

    def creators_handler(self, update, context):
        self.logger.info(f'{update.message.chat.username} requested information about creators')
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text="@RandomDanil & @Daniil")

    def any_text_handler(self, update, context):
        self.logger.info(f'{update.message.chat.username} wrote {update.message.text}')
        text = '!'
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=text)

    def start(self):
        self.logger.info('start polling')
        self.updater.start_polling()


if __name__ == '__main__':
    bot = EmojifyBot()
    bot.start()
