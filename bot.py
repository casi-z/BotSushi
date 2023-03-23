from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import utils.keyboard as keyboard
import database.data as data

TOKEN = "6199751866:AAFyLUZOt5IoFu3nnAoetnYcHoRmTJkBjdg"
bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

photo = types.InputFile("./img/fon.jpg")
menuImg = types.InputFile("./img/menu.jpg")

def text(array):
    return '\n'.join(array)
         
       
	

def stringMap(first, array, last):
    
    str = ''
    for elem in array:
        str += (first + elem + last)
        
    return str


@dp.message_handler(commands=['start'])

async def process_start_command(message: types.Message):
    
    await bot.send_photo(
        chat_id=message.chat.id, 
        photo=photo,
        
        caption=text([
			"Приветствуем вас за столом нашего уютного заведения!",
            "Будь как дома путник",
            "",
            "<b>Что бы увидеть меню пишите:</b>",
            "",
            "/menu",
		]),

        reply_markup=keyboard.start_kb
    )


@dp.message_handler(text=['menu', 'Меню 🍣'])

async def process_start_command(message: types.Message):

    await bot.send_photo(
        chat_id=message.chat.id, 
        
        photo=menuImg, 
        
        caption="""Выберите один из наших разделов:\n""" + stringMap('\n<b>--', data.categories, '</b>\n'),
        reply_markup=keyboard.category_kb
    )

async def getMenuUnit(category, message):
    for i in data.menu[category]:
        await bot.send_photo(
			chat_id=message.chat.id, 
			photo=types.InputFile("./img/fon.jpg"),
			caption=text([
				"Выберите один или несколько товаров из категории",
				i['description']
			])   
    	)
        
	# print(data.menu[category])

@dp.message_handler(text=data.categories)
async def process_start_command(message: types.Message):
	
    for i in data.menu[message.text]:
        await bot.send_photo(
			chat_id=message.chat.id, 
			photo=types.InputFile("./img/"+ message.text +"/main.jpg"),
			caption=text([
				i['name'],
				i['description'],
                'Цена:'+str(i['price'])+'Р',
                '',
                'Добавить: /'+ str(data.menu[message.text].index(i))
			])   
    	)





if __name__ == '__main__':
    executor.start_polling(dp)
