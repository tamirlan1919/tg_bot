from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state import PoolStates
from database.crud import update_table_user, get_user_by_id, insert_to_table_users

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    user = get_user_by_id(message.from_user.id)
    if not user:
        insert_to_table_users(message.from_user.id)
    await message.answer("Привет я бот который делает опрос /pool")


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Я бот который делает опросы, чтобы начать опрос напиши /pool")


@router.message(Command("pool"))
async def cmd_pool(message: Message, state: FSMContext):
    await message.answer("Как тебя зовут?")
    await state.set_state(PoolStates.name)

@router.message(Command("pool"))
async def cmd_pool(message: Message, state: FSMContext):
    await message.answer("Какая твоя фамилия?")
    await state.set_state(PoolStates.second_name)


@router.message(PoolStates.name)
async def pool_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Сколько тебе лет?")
    await state.set_state(PoolStates.age)

@router.message(PoolStates.age)
async def pool_age(message: Message, state: FSMContext):
    age = state.update_data(age=message.text)
    data = await state.get_data()
    name = data.get("name")
    second_name = data.get('second_name')
    age = data.get("age")
    await message.answer(f"Тебя зовут {name}, и твоя фамилия {second_name} тебе {age} лет")
    update_table_user(message.from_user.id, name, age)
    await state.clear()
    await message.answer("Спасибо за участие в опросе!")