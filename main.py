# bot.py
import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, ContentType

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = "8589621495:AAGygoZUhMykeWEUkBnjNuzs5SX3EbbvedY"

API_TOKEN = os.environ.get("BOT_TOKEN")  # пеш аз иҷрош, export BOT_TOKEN="123:ABC..."

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    # URL-ро ба URL-и онлайн вебсаҳифаат иваз кун
    webapp_url = "https://your-webapp-domain.example/"  # <-- инро иваз кун
    keyboard.add( InlineKeyboardButton("Open KFC Menu", web_app=WebAppInfo(url=webapp_url)) )
    await message.answer("Салом! Менюи KFC-ро кушо ва фармоиш фирист.", reply_markup=keyboard)

# Гирифтани маълумоти фиристода аз WebApp
@dp.message_handler(content_types=ContentType.WEB_APP_DATA)
async def webapp_data_handler(message: types.Message):
    data = message.web_app_data.data  # ин сатрест, ки аз tg.sendData(... ) фиристода шуд
    user = message.from_user
    text = f"Новый заказ от {user.first_name} (id={user.id}):\n{data}"
    # Послать подтверждение юзеру
    await message.answer("Ташаккур! Фармоиши шумо қабул шуд.")
    # Барои мисол: ба худат бифирист ё ба администратор
    admin_id = os.environ.get("ADMIN_ID")
    if admin_id:
        await bot.send_message(chat_id=admin_id, text=text)

async def main():
    print("bot")
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
