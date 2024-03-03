from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor

bot = Bot('6830187925:AAFn-N6SIb0br1lnVhyBbMN00qdayK4JeMA')
dp = Dispatcher(bot=bot)
btn = InlineKeyboardButton(text='Подписаться', url='https://t.me/+h7z6aaxZQyFhYjZi')
markup = InlineKeyboardMarkup(row_width=2).add(btn)


def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False
    

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=-1002138364675, user_id=message.from_user.id)):
        await message.answer_sticker('CAACAgIAAxkBAAMpZBAAAfUO9xqQuhom1S8wBMW98ausAAI4CwACTuSZSzKxR9LZT4zQLwQ')
        await message.answer(f'{message.from_user.first_name}, поделись фотографией техники для публикации в ТГк.\nОтправь фото в сообщении.')
    else:
        await bot.send_message(message.from_user.id, 'Для использования бота подпишитесь на канал!!!', reply_markup=markup)

@dp.message_handler(content_types=['sticker'])
async def check_sticker(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=-1002138364675, user_id=message.from_user.id)):
        await message.answer(message.sticker.file_id)
        await bot.send_message(message.from_user.id, message.chat.id)
    else:
        await bot.send_message(message.from_user.id, 'Для использования бота подпишитесь на канал!!!', reply_markup=markup)
    


@dp.message_handler(content_types=['document', 'photo'])
async def forward_message(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=-1002138364675, user_id=message.from_user.id)):
        await bot.forward_message(-1002138364675, message.from_user.id, message.message_id)
    else:
        await bot.send_message(message.from_user.id, 'Для использования бота подпишитесь на канал!!!', reply_markup=markup)
    


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я тебя не понимаю.')


if __name__ == '__main__':
    executor.start_polling(dp)