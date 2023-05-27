from dotenv import dotenv_values
from character import Character
from loader import Loader

env = dotenv_values()

my_character = Character(
    env["FIRST_CHARACTER_NAME"],
    env["FIRST_CHARACTER_REALM"],
    env["FIRST_CHARACTER_REGION"],
)
my_character.process_raw_gear(Loader(my_character).get_data())

target_character = Character(
    env["SECOND_CHARACTER_NAME"],
    env["SECOND_CHARACTER_REALM"],
    env["SECOND_CHARACTER_REGION"],
)
target_character.process_raw_gear(Loader(target_character).get_data())

my_character.compare(target_character)
