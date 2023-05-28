from dotenv import dotenv_values
from character import Character, Comparator
from helpers import Loader

env = dotenv_values()

my_character = Loader(
    Character(
        env["FIRST_CHARACTER_NAME"],
        env["FIRST_CHARACTER_REALM"],
        env["FIRST_CHARACTER_REGION"],
    )
).load()

target_character = Loader(
    Character(
        env["SECOND_CHARACTER_NAME"],
        env["SECOND_CHARACTER_REALM"],
        env["SECOND_CHARACTER_REGION"],
    )
).load()

comparator = Comparator(my_character, target_character)

comparator.stats()
