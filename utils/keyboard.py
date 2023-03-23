from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import database.data as data

menu_button = KeyboardButton(text='Меню 🍣')
start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

start_kb.add(menu_button)

category_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

for i in data.categories:
    category_button = KeyboardButton(text=i)
    category_kb.add(category_button)

