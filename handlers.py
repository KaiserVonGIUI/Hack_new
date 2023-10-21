from aiogram import F, Router, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State
from aiogram.types import Message
import text

router = Router()


class Profil:
    name1 = "",
    name2 = "",
    name3 = "",
    otdel = ""


class Profile(StatesGroup):
    test123 = State()
    name1 = State()
    name2 = State()
    name3 = State()
    otdel = State()
    admin = State()


global name1
global name2
global name3
global otdel


@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    await msg.answer(text.greet)
    await msg.answer(text.name1)
    await state.set_state(Profile.test123)


@router.message(Profile.test123, F.text)
async def vod_name1(msg: Message, state: FSMContext):
    Profil.name1 = msg.text
    print(Profil.name1)
    await state.set_state(Profile.name1)
    await msg.answer(text.name2)


@router.message(Profile.name1, F.text)
async def vod_name2(msg: Message, state: FSMContext):
    Profil.name2 = msg.text
    print(Profil.name2)
    await state.set_state(Profile.name2)
    await msg.answer(text.name3)


@router.message(Profile.name2, F.text)
async def vod_name2(msg: Message, state: FSMContext):
    Profil.name3 = msg.text
    print(Profil.name3)
    await state.set_state(Profile.name3)
    await msg.answer(text.otdel)


@router.message(Profile.name3, F.text)
async def vod_name3(msg: Message, state: FSMContext):
    Profil.otdel = msg.text
    print(Profil.otdel)
    await state.set_state(Profile.otdel)

@router.message(Profile.otdel, F.text)
async def profil(msg: Message, state: FSMContext):
    #await msg.answer("Добро пожаловать,", profil.name2, " ", profil.name3, " отдел ", profil.otdel)
    await msg.answer(f"{Profil.name3} {Profil.name2} {Profil.name1} {Profil.otdel}")


"""
@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)"""
