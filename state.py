from aiogram.fsm.state import State, StatesGroup


class PoolStates(StatesGroup):
    name = State()
    second_name = State()
    age = State()  