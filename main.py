from helpers import Configurator, Loader
from character import Character, Comparator

configuration = Configurator()
if configuration.make_it_legal() is False:
    print(configuration.get_unofficial_use_nag_message())

my_character = Loader(
    configuration=configuration,
    character=Character(configuration.get_first_character())
).load()

target_character = Loader(
    configuration=configuration,
    character=Character(configuration.get_second_character())
).load()

comparator = Comparator(my_character, target_character)

comparator.stats()
