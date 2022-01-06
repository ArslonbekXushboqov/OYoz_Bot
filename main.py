from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types.message import Message
from keybords import *
import requests as r
from time import sleep

storage = MemoryStorage()

bot = Bot(token="5037374918:AAEqxkluDDHbcTIh_mSRBpuoCAu2K1Rl6eE", parse_mode='HTML')
dp = Dispatcher(bot,storage=storage)


class Rasm(StatesGroup):
    paper_1 = State()
    paper_2 = State()
    paper_3 = State()
    paper_4 = State()

@dp.message_handler(commands=['start'])
async def start_msg(m: types.Message):
    await bot.send_message(m.chat.id, f"<b>Assalomu alaykum Xush Kelibsiz</b> <a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name}</a>\n\n<i>Men orqali turli xil daftar varoqlari chaklidagi rasmlarga konstpekt yozishingiz mumkin!</i>", reply_markup=main)

async def home_msg(m: types.Message):
    await bot.send_message(m.chat.id, f"<b>Bosh sahifaga qaytdingiz!</b>", reply_markup=main)

async def getpaper(m: types.Message):
    await bot.send_photo(chat_id=m.chat.id, photo="https://telegra.ph/file/f846adb3164654a642a24.jpg", caption="<b>Oʻzingizga kerakli boʻlgan konspekt turini tanlang:</b>", reply_markup=button)

async def dev(m: types.Message):
    await m.answer("<b>👨🏻‍💻 Developer:</b> @LiderBoy\n<b>🍃Api Developer:</b> @Rizayev_Ruslan", reply_markup=home)

async def home_(m: types.Message):
    await home_msg(m)
@dp.callback_query_handler(Text(startswith="paper"))
async def calls(call: types.CallbackQuery):
    global active_state, action
    action = call.data.split("_")[1]
    await bot.delete_message(call.message.chat.id,call.message.message_id)
    if action == '1' or action == '2' or action == '3' or action == '4':
        if action == '1':
            active_state = Rasm.paper_1
        elif action == '2':
            active_state = Rasm.paper_2
        elif action == '3':
            active_state = Rasm.paper_3
        else:
            active_state = Rasm.paper_4
        await active_state.set()
        await bot.send_message(call.message.chat.id, f"<i>[{action}] Konspekt yozish uchun menga text yuboring:</i>")
    if action == 'getpaper':
        await getpaper(call.message)
    elif action == 'dev':
        await dev(call.message)
    elif action == 'home':
        await home_(call.message)

@dp.message_handler(state="*", commands='cancel')
async def cancel(m: types.Message, state: FSMContext):
    await m.answer("Bekor qilindi")
    await state.finish()

@dp.message_handler(state=Rasm.paper_1)
async def paper1(m: types.Message,state=FSMContext):
    res = r.get(f"https://nazirovdev.uzxost.ru/rasm/index.php?text={m.text}").json()
    photo_1 = res['suratlar']['rasm1']
    await m.answer("<b>🍃 Tayyorlanmoqda...</b>")
    sleep(1.5)
    await bot.delete_message(m.chat.id, m.message_id+1)
    await bot.send_photo(m.chat.id, f"{photo_1}", reply_markup=home)
    await state.finish()
@dp.message_handler(state=Rasm.paper_2)
async def paper2(m: types.Message,state=FSMContext):
    res = r.get(f"https://nazirovdev.uzxost.ru/rasm/index.php?text={m.text}").json()
    photo_1 = res['suratlar']['rasm2']
    await m.answer("<b>🍃 Tayyorlanmoqda...</b>")
    sleep(1.5)
    await bot.delete_message(m.chat.id, m.message_id+1)
    await bot.send_photo(m.chat.id, f"{photo_1}", reply_markup=home)
    await state.finish()
@dp.message_handler(state=Rasm.paper_3)
async def paper3(m: types.Message,state=FSMContext):
    res = r.get(f"https://nazirovdev.uzxost.ru/rasm/index.php?text={m.text}").json()
    photo_1 = res['suratlar']['rasm3']
    await m.answer("<b>🍃 Tayyorlanmoqda...</b>")
    sleep(1.5)
    await bot.delete_message(m.chat.id, m.message_id+1)
    await bot.send_photo(m.chat.id, f"{photo_1}", reply_markup=home)
    await state.finish()
@dp.message_handler(state=Rasm.paper_4)
async def paper4(m: types.Message,state=FSMContext):
    res = r.get(f"https://nazirovdev.uzxost.ru/rasm/index.php?text={m.text}").json()
    photo_1 = res['suratlar']['rasm4']
    await m.answer("<b>🍃 Tayyorlanmoqda...</b>")
    sleep(1.5)
    await bot.delete_message(m.chat.id, m.message_id+1)
    await bot.send_photo(m.chat.id, f"{photo_1}", reply_markup=home)
    await state.finish()


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
