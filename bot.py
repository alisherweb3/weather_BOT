from aiogram import Bot, Dispatcher, types, executor

from settings import bot_config

bot = Bot(token=bot_config.bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
  markup = types.reply_keyboard.ReplykeyboardMarkUp(row_width=2)
  btn1 = types.KeyboardButton('Mening shahrimdagi ob havo')
  btn2 = types.keyboardButton('Boshqa yerdagi ov havo')
  btn3 = types.KeyboardButton('Tarix')
  btn4 = types.KeyboardButton('Shahringizni  tanlang')
  markyp.add(btn1, btn2, btn3, btn4)
  text = f'Salom {message,from_user.first_name},  men bugungi ob havo haqida aytadigan botman.'
  await message.answer(text, reply_markup=markup)
  
@dp.message_handler(regexp='Mening shahrimdagi ob havo')
async def get_user_city_weather(message):
  markup = types.reply_keyboard,replyKeyboardmarkup(row_width=2, resize_keyboard=True)
  btn1 = types.KeyboardButton('Menyu')
  markup.add(btn1)
  text = 'Men hozircha bu ishni qila olmayman')
  await message.answer(text, reply_markup=markup)
  
@dp.message_handler(regexp='Menyu')
async def start_message(message: types.Message):
  markup = types.reply_keyboard.ReplykeyboardMarkUp(row_width=2)
  btn1 = types.KeyboardButton('Mening shahrimdagi ob havo')
  btn2 = types.keyboardButton('Boshqa yerdagi ov havo')
  btn3 = types.KeyboardButton('Tarix')
  btn4 = types.KeyboardButton('Shahringizni  tanlang')
  markyp.add(btn1, btn2, btn3, btn4)
  text = f'Salom {message.from_user.first_name}, men bugungi ob havo haqida aytadigan botman.'
  await message.answer(text, reply_markup=markup)
  
if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
  
