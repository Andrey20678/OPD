import logging, time, asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import app.keyboard as k

logging.basicConfig(level=logging.INFO)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Терапевт"),
    KeyboardButton(text="Невролог")],
    [KeyboardButton(text="Окулист"),
    KeyboardButton(text="Травматолог")]
])

tera = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='9:30',  callback_data='9:30')],
    [InlineKeyboardButton(text='10:00', callback_data='10:00')],
    [InlineKeyboardButton(text='10:30', callback_data='10:30')],
    [InlineKeyboardButton(text='11:00', callback_data='11:00')]
])
neur = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='9:30',  callback_data='9:30')],
    [InlineKeyboardButton(text='10:30', callback_data='10:30')],
    [InlineKeyboardButton(text='11:30', callback_data='11:30')],
    [InlineKeyboardButton(text='13:00', callback_data='13:00')]
])
oku = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='11:30', callback_data='11:30')],
    [InlineKeyboardButton(text='13:00', callback_data='13:00')],
    [InlineKeyboardButton(text='14:30', callback_data='14:30')],
    [InlineKeyboardButton(text='15:00', callback_data='15:00')]
])
travm = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='9:30',  callback_data='9:30')],
    [InlineKeyboardButton(text='10:00', callback_data='10:00')],
    [InlineKeyboardButton(text='10:30', callback_data='10:30')],
    [InlineKeyboardButton(text='11:00', callback_data='11:00')]
])

bot = Bot(token="7599352485:AAFwiijyBXcS4Vs2ml2XBXh-6PhUVg0PcgM")
dp = Dispatcher()


class Reg(StatesGroup):
    who = State()
    time = State()
    fio = State()



@dp.message(CommandStart())
async def process_start_command(message: types.Message):
    await message.answer("Запись к врачу", reply_markup=k.kb)

@dp.message(Command('help'))
async def process_start_command(message: types.Message):
    await message.reply("Введите /start")

@dp.message(F.text == "Терапевт")
async def cmd_tera(message: types.Message, state: FSMContext):
    await state.update_data(who=message.text)
    await state.set_state(Reg.time)
    await message.answer("Выберите время записи", reply_markup=k.tera)

@dp.message(F.text == "Невролог")
async def cmd_tera(message: types.Message, state: FSMContext):
    await state.update_data(who=message.text)
    await state.set_state(Reg.time)
    await message.answer("Выберите время записи", reply_markup=k.neur)

@dp.message(F.text == "Окулист")
async def cmd_tera(message: types.Message, state: FSMContext):
    await state.update_data(who=message.text)
    await state.set_state(Reg.time)
    await message.answer("Выберите время записи", reply_markup=k.oku)

@dp.message(F.text == "Травматолог")
async def cmd_tera(message: types.Message, state: FSMContext):
    await state.update_data(who=message.text)
    await state.set_state(Reg.time)
    await message.answer("Выберите время записи", reply_markup=k.travm)


@dp.message(Reg.time)
async def reg_time(message: types.Message, state: FSMContext):
    await state.update_data(time=message.text)
    await state.set_state(Reg.fio)
    await message.answer('Введите ФИО')

@dp.message(Reg.fio)
async def reg_time(message: types.Message, state: FSMContext):
    await state.update_data(fio=message.text)
    data = await state.get_data()
    await message.answer(f'Вы записались к {data["who"]}\nНа время {data["time"]}\nВы - {data["fio"]}')
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Выключение")