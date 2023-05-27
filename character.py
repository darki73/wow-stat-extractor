import re
from item import Item, stat_mapping
from prettytable import PrettyTable


# Returns the list of stats that are considered primary
def primary_stats() -> list[str]:
    return ['STRENGTH', 'AGILITY', 'INTELLECT', "STAMINA"]


# Class: Character
class Character:
    # Character name
    name: str
    # Character realm
    realm: str
    # Character region
    region: str
    # Character gear
    gear: list[Item]
    # Character stats
    stats: dict

    # Class constructor
    def __init__(self, name: str, realm: str, region: str):
        self.name = name
        self.realm = self.create_realm_slug(realm)
        self.region = region
        self.gear = []
        self.stats = {}

    # Returns the character name
    def get_name(self) -> str:
        return self.name

    # Returns the character realm
    def get_realm(self) -> str:
        return self.realm

    # Returns the character region
    def get_region(self) -> str:
        return self.region

    # Returns the character gear
    def get_gear(self) -> list[Item]:
        return self.gear

    # Returns the character stats
    def get_stats(self) -> dict:
        return self.stats

    # Returns character realm slug
    def create_realm_slug(self, realm_name: str):
        slug = re.sub(r'[^\w\s-]', '', realm_name).strip().lower()
        slug = re.sub(r'\s+', '-', slug)
        slug = re.sub(r'-+', '-', slug)
        return slug

    # Returns the character primary stats
    def get_primary_stats(self) -> dict:
        return {k: v for k, v in self.stats.items() if k in primary_stats()}

    # Returns the character secondary stats
    def get_secondary_stats(self) -> dict:
        return {k: v for k, v in self.stats.items() if k not in primary_stats()}

    # Returns the character secondary stats with percentages (contribution to total)
    def get_secondary_stats_with_percentages(self) -> dict:
        total = sum(self.get_secondary_stats().values())
        stats = {}
        for k, v in self.get_secondary_stats().items():
            data = {
                'value': v,
                'percentage': round(v / total * 100, 2)
            }
            stats[k] = data

        stats = dict(sorted(stats.items(), key=lambda item: item[1]['percentage'], reverse=True))

        return stats

    # Compares the character with another character
    def compare(self, character):
        this_name = self.get_name()
        target_name = character.get_name()

        stats = {}
        for k, v in self.stats.items():
            if k in character.get_stats():
                stats[k] = {
                    this_name: v,
                    target_name: character.get_stats()[k],
                    'difference': v - character.get_stats()[k],
                    'trend': 'more' if v > character.get_stats()[k] else 'less'
                }
            else:
                stats[k] = {
                    this_name: v,
                    target_name: 0,
                    'difference': v,
                    'trend': 'more'
                }

        # Get all the unique headers
        headers = [""] + list(stats[list(stats.keys())[0]].keys())

        # Create the table
        table = PrettyTable(headers)

        for header in stats:
            row_data = [stat_mapping[header]] + [str(stats[header].get(col, "")) for col in headers[1:]]
            table.add_row(row_data)

        # Print the table
        print(table)

    # Processes the raw gear data
    def process_raw_gear(self, items: dict):
        for slot, entity in items.items():
            self.gear.append(Item.from_json(entity, slot))

        for item in self.gear:
            for stat in item.get_stats():
                if stat.get_identifier() not in self.stats:
                    self.stats[stat.get_identifier()] = stat.get_value()
                else:
                    self.stats[stat.get_identifier()] += stat.get_value()
            for socket in item.get_sockets():
                for stat in socket.get_stats():
                    if stat.get_identifier() not in self.stats:
                        self.stats[stat.get_identifier()] = stat.get_value()
                    else:
                        self.stats[stat.get_identifier()] += stat.get_value()
