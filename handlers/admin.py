from aiogram import types
from misc import dp, bot

from .sqlit import info_members
from .channel_list import obnovlenie


from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


ADMIN_ID_1 = 1035355655
ADMIN2 = 1988049250

ADMIN_ID =[ADMIN_ID_1,ADMIN2,494588959]

class reg(StatesGroup):
    name = State()
    fname = State()

class st_reg(StatesGroup):
    st_name = State()
    st_fname = State()
    step_q = State()
    step_regbutton = State()


class del_user(StatesGroup):
    del_name = State()
    del_fname = State()

class reg_trafik(StatesGroup):
    traf1 = State()
    traf2 = State()

class reg_trafik2(StatesGroup):
    traf1 = State()
    traf2 = State()

class reg_trafik3(StatesGroup):
    traf1 = State()
    traf2 = State()

class reg_trafik4(StatesGroup):
    traf1 = State()
    traf2 = State()

class reg_link(StatesGroup):
    traf1 = State()
    traf2 = State()

@dp.message_handler(commands=['admin'])
async def admin_ka(message: types.Message):
    id = message.from_user.id
    if id in ADMIN_ID:
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Трафик', callback_data='list_members')
        bat_e = types.InlineKeyboardButton(text='Рассылка', callback_data='write_message')
        bat_j = types.InlineKeyboardButton(text='Скачать базу данных', callback_data='baza')
        bat_setin = types.InlineKeyboardButton(text='Настройка трафика', callback_data='settings')

        markup.add(bat_a,bat_e)
        markup.add(bat_setin)
        markup.add(bat_j)
        await bot.send_message(message.chat.id,'Выполнен вход в админ панель',reply_markup=markup)




@dp.callback_query_handler(text='baza')
async def baza(call: types.callback_query):
    a = open('server.db','rb')
    await bot.send_document(chat_id=call.message.chat.id, document=a)


@dp.callback_query_handler(text='list_members')  # АДМИН КНОПКА ТРАФИКА
async def check(call: types.callback_query):
    a = info_members() # Вызов функции из файла sqlit
    await bot.send_message(call.message.chat.id, f'Количество пользователей: {a}')

@dp.callback_query_handler(text='otemena',state='*')
async def otmena_12(call: types.callback_query, state: FSMContext):
    try:
        await bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
    except:
        pass

    await bot.send_message(call.message.chat.id, 'Отменено')
    await state.finish()


