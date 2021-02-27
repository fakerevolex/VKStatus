from bs4 import BeautifulSoup
import requests
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1653579035:AAFud8XCxQuFFN6dUkm6c3kJItOL48xi9B8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# <div class="profile_online_lv">online</div>
def parse(URL):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.182 Safari/537.36 '
    }
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all("div", class_="page_info_wrap")
    statuses = []

    for item in items:
        try:
            statuses.append({
                'name': item.find("h1", class_="page_name").get_text(strip=True),
                'status': item.find("div", class_="profile_online_lv").get_text(strip=True)
            })
        except Exception:
            statuses.append({
                'name': item.find("h1", class_="page_name").get_text(strip=True),
                'status': "? /error"
            })
    for status in statuses:
        print(status['name'], status['status'])
    return status['name'] + " [" + status['status'] + "]"


"""@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)"""


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("VKStatusbot! Type /help for help.")


@dp.message_handler(commands=['error'])
async def send_welcomedfgdgf(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Я не ебу почему еррор вылазиит иди нахуй карчое!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Available commands: \n /check 'url' \n /online \n /denis")


@dp.message_handler(commands=['denis'])
async def process_help_commandfg(message: types.Message):
    await message.reply("https://sun9-62.userapi.com/impg/KlHdnYa-msne7w42Jr5o48NGOf4NeXudykn6Ag/lT2jl2dNTu8.jpg?size"
                        "=540x540&quality=96&sign=bc151cbb13a09a48a52209280c442335&type=album")


@dp.message_handler(commands=['check'])
async def test(message: types.Message):
    try:
        await message.reply(parse(message.text[7:90]))
    except Exception:
        await message.reply("Error!!!!!!")
        await message.reply(message.text[7:90])


@dp.message_handler(commands=['online'])
async def online(message: types.Message):
    try:
        await message.reply("Список пользователей sqd-spm:")
        await message.answer(parse("https://vk.com/revolex"))
        await message.answer(parse("https://vk.com/alonzo_vk"))
        await message.answer(parse("https://vk.com/grinbo1"))
        await message.answer(parse("https://vk.com/pavlovegorga"))
        await message.answer(parse("https://vk.com/katerebaniy"))
        await message.answer(parse("https://vk.com/codein1"))
    except Exception:
        await message.reply("Errorka)")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
