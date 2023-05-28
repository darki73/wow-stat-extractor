from prettytable import PrettyTable
from character import Character


# Class: Comparator
class Comparator:
    # First character instance
    first_character: Character
    # Second character instance
    second_character: Character

    # Class constructor
    def __init__(self, first_character: Character, second_character: Character):
        self.first_character = first_character
        self.second_character = second_character

    # Compares the stats of the two characters
    def stats(self):
        print("Comparing stats for:")
        print("\t{} - {} {} - Level {} - Item Level {} ({} / {})".format(
            self.first_character.get_name(),
            self.first_character.get_character_spec().get_name(),
            self.first_character.get_character_class().get_name(),
            self.first_character.get_level(),
            self.first_character.get_item_level(),
            self.first_character.get_realm(),
            self.first_character.get_region().upper(),
        ))
        print("\t{} - {} {} - Level {} - Item Level {} ({} / {})".format(
            self.second_character.get_name(),
            self.second_character.get_character_spec().get_name(),
            self.second_character.get_character_class().get_name(),
            self.second_character.get_level(),
            self.second_character.get_item_level(),
            self.second_character.get_realm(),
            self.second_character.get_region().upper(),
        ))
        print("")

        first_character_name = self.first_character.get_name()
        first_character_stats = self.first_character.get_character_stats().to_dict()

        second_character_name = self.second_character.get_name()
        second_character_stats = self.second_character.get_character_stats().to_dict()

        stats = {}

        for stat, value in first_character_stats.items():
            if stat in second_character_stats:
                stats[stat] = {
                    first_character_name: value,
                    second_character_name: second_character_stats[stat],
                    'difference': value - second_character_stats[stat],
                    'trend': '➕' if value > second_character_stats[stat] else '➖'
                }
            else:
                stats[stat] = {
                    first_character_name: value,
                    second_character_name: 0,
                    'difference': value,
                    'trend': '➕'
                }

        headers = [""] + list(stats[list(stats.keys())[0]].keys())

        table = PrettyTable(headers)

        for header in stats:
            header_name = self._capitalize_words(header)
            row_data = [header_name] + [str(stats[header].get(col, "")) for col in headers[1:]]
            table.add_row(row_data)

        print(table)

    # Capitalizes the words in a string
    def _capitalize_words(self, variable: str):
        words = variable.split('_')
        capitalized_words = [word.capitalize() for word in words]
        return ' '.join(capitalized_words)
