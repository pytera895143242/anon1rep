from aiogram import types
from misc import dp,bot
from .sqlit import reg_bd,reg_in_users
from .mysql import reg_user_mysql
reg_bd()


def markup_find():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bat1 = types.InlineKeyboardButton(text="🔎 ПАРЕНЬ")
    bat2 = types.InlineKeyboardButton(text="🔎 ДЕВУШКА")
    bat3 = types.InlineKeyboardButton(text="🎲 СЛУЧАЙНЫ ПОЛ 🎲")
    markup.add(bat1,bat2)
    markup.add(bat3)
    return markup

def markup_gender():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bat1 = types.InlineKeyboardButton(text="🚹 Я парень")
    bat2 = types.InlineKeyboardButton(text="🚺 Я девушка")
    markup.add(bat1,bat2)
    return markup

def markup_stop():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bat1 = types.InlineKeyboardButton(text="❌ Остановить поиск")
    markup.add(bat1)
    return markup

def markup_stop_dialog():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bat1 = types.InlineKeyboardButton(text="❌ Остановить диалог")
    markup.add(bat1)
    return markup



@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await reg_user_mysql(message.chat.id)
    try:
        first_name = message.from_user.first_name
    except:
        first_name = 'anonim'
    if message.text[6:] == '':
        reg_in_users(chat_id=message.chat.id,first_name=first_name,ref= '1')
    else:
        reg_in_users(chat_id=message.chat.id, first_name=first_name, ref=message.text[6:])


    await message.answer(text=f"""<b>Привет {message.from_user.first_name} 😻

💚Наш бот абсолютно бесплатный, перед тем как начать, выбери свой пол👇</b>""",reply_markup=markup_gender())


