#!/usr/bin/env python
# encoding: utf-8
#
# Robô Ed Telegram Bot
# Copyright (C) 2015 Leandro Toledo de Souza <leandrotoeldodesouza@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].


__author__ = 'armanfbi1@gmail.com'

import logging
import telegram
import urllib
answered = []

def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    bot = telegram.Bot('129187196:AAHowjHFyVd0DF_1RYeMgbfyOiNgQUkuYYU')  # Telegram Bot Authorization Token
    print bot.username
    LAST_UPDATE_ID = bot.getUpdates()[-1].update_id  # Get lastest update
    for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=1):
        text = update.message.text
        chat_id = update.message.chat.id
        update_id = update.update_id
        #print chat_id
        #print update.username
        if text:
            if (text == '/start' ):
                bot.sendPhoto(chat_id,'https://pypi.python.org/static/images/python-logo.png','به آپ شو خوش آمديد');
            elif (text == '/start1' ):
                bot.sendPhoto(chat_id,'https://pypi.python.org/static/images/python-logo.png','/start1_1 - آزاده رو که تیغ کشیده ست بر اصغر');
                bot.sendPhoto(chat_id,'https://pypi.python.org/static/images/python-logo.png','/start1_2 - اصغر از آزکابان در رفته به داد خودتون برسين :دي');
            elif (text == '/start1_1' ):
                bot.sendPhoto(chat_id,'https://pypi.python.org/static/images/python-logo.png','والله من شنيدم ميخواد از آزکابان فرار کنه \n حالا خود داني');
            elif (text == '/start1_2' ):
                bot.sendPhoto(chat_id,'https://pypi.python.org/static/images/python-logo.png','نگفتم در رو؟؟ \n سکتوم سمپرا');
            elif (text == '/stop' ):
                bot.sendPhoto(chat_id,'https://pypi.python.org/static/images/python-logo.png','اصغر در کمين است، آهسته رو آرام جانت ميرود')
            else:
                bot.sendMessage(chat_id=chat_id, text='آسود باش که اصغر خفته از دکمه ها اصلي استفاده کن')
            LAST_UPDATE_ID = ''
    

def ed(text):
    url = '127.0.0.1:8080/static/' + text
    data = urllib.urlopen(url).read()

    return data.strip()

if __name__ == '__main__':
    while 1:
        try:main()
        except Exception as x:print x
