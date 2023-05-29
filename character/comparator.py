from prettytable import PrettyTable
from character import Character, Classes, BaseSpecialization


# Class: Comparator
class Comparator:
    # Classes instance
    classes: Classes = Classes()
    # First character instance
    first_character: Character
    # Second character instance
    second_character: Character
    # Secondary stats list
    secondary_stats: list[str] = [
        "critical_strike",
        "haste",
        "mastery",
        "versatility",
    ]

    # Class constructor
    def __init__(self, first_character: Character, second_character: Character):
        self.first_character = first_character
        self.second_character = second_character

    # Compares the stats of the two characters
    def stats(self):
        [
            first_character_name,
            first_character_spec_data,
            second_character_name,
            second_character_spec_data,
        ] = self._print_header(self.first_character, self.second_character)

        first_character_stats = self.first_character.get_character_stats().to_dict()
        second_character_stats = self.second_character.get_character_stats().to_dict()

        stats = {}

        for stat, value in first_character_stats.items():
            if stat in second_character_stats:
                first_character_value = value
                second_character_value = second_character_stats[stat]

                if stat in self.secondary_stats:
                    if first_character_spec_data is not None:
                        first_character_value = self._compute_character_value_with_percentage(
                            stat,
                            value,
                            first_character_spec_data,
                        )

                    if second_character_spec_data is not None:
                        second_character_value = self._compute_character_value_with_percentage(
                            stat,
                            second_character_value,
                            second_character_spec_data,
                        )

                stats[stat] = {
                    first_character_name: first_character_value,
                    second_character_name: second_character_value,
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

    # Computes the value of a character stat with percentage
    def _compute_character_value_with_percentage(self, stat: str, value: int, spec_data: BaseSpecialization):
        percentage_of_value = value / (spec_data.get_stat_per_percent_by_slug(stat).get_value_per_percent())
        percentage_bonus = 0

        if spec_data.has_stat_bonus_by_slug(stat):
            percentage_bonus = spec_data.get_stat_bonus_by_slug(stat).get_value()

        final_percentage = round(percentage_of_value + percentage_bonus, 2)

        return f"{value} / {final_percentage}%"

    # Capitalizes the words in a string
    def _capitalize_words(self, variable: str):
        words = variable.split('_')
        capitalized_words = [word.capitalize() for word in words]
        return ' '.join(capitalized_words)

    # Prints the header for the stats comparison
    def _print_header(self, first_character, second_character):
        first_character_name = self.first_character.get_name()
        first_character_class = self.first_character.get_character_class().get_name()
        first_character_spec = self.first_character.get_character_spec().get_name()
        first_character_spec_data = None

        if self.classes.get_class(first_character_class).has_specialization(first_character_spec):
            first_character_spec_data = self.classes. \
                get_class(first_character_class). \
                get_specialization(first_character_spec)

        second_character_name = self.second_character.get_name()
        second_character_class = self.second_character.get_character_class().get_name()
        second_character_spec = self.second_character.get_character_spec().get_name()
        second_character_spec_data = None

        if self.classes.get_class(second_character_class).has_specialization(second_character_spec):
            second_character_spec_data = self.classes. \
                get_class(second_character_class). \
                get_specialization(second_character_spec)

        print("Comparing stats for:")
        print("\t{} - {} {} - Level {} - Item Level {} ({} / {})".format(
            first_character_name,
            first_character_spec,
            first_character_class,
            first_character.get_level(),
            first_character.get_item_level(),
            first_character.get_realm(),
            first_character.get_region().upper(),
        ))
        print("\t{} - {} {} - Level {} - Item Level {} ({} / {})".format(
            second_character_name,
            second_character_spec,
            second_character_class,
            second_character.get_level(),
            second_character.get_item_level(),
            second_character.get_realm(),
            second_character.get_region().upper(),
        ))
        print("")

        return [
            first_character_name,
            first_character_spec_data,
            second_character_name,
            second_character_spec_data
        ]
