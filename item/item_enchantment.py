import re
import json
from item import ItemEnchantmentStat


# Class: ItemEnchantment
class ItemEnchantment:
    # Enchantment identifier
    id: int
    # Enchantment display string
    display_string: str
    # Enchantment stats
    stats: list[ItemEnchantmentStat]

    # Class constructor
    def __init__(self, identifier: int, display_string: str, stats: list[ItemEnchantmentStat]):
        self.id = identifier
        self.display_string = display_string
        self.stats = stats

    # Returns the enchantment identifier
    def get_identifier(self) -> int:
        return self.id

    # Returns the enchantment display string
    def get_display_string(self) -> str:
        return self.display_string

    # Returns the enchantment stats
    def get_stats(self) -> list[ItemEnchantmentStat]:
        return self.stats

    # Converts class to a dictionary
    def to_dict(self):
        return {
            'id': self.get_identifier(),
            'display_string': self.display_string,
            'stats': [stat.to_dict() for stat in self.stats]
        }

    # Creates a new instance from a dictionary
    @classmethod
    def from_dict(cls, data: dict):
        item_enchantment_stats = []

        matches = re.findall(r"\+(\d+)\s*([A-Za-z\s]+)", data['display_string'])
        for match in matches:
            value = int(match[0])
            key = match[1].strip()
            item_enchantment_stats.append(ItemEnchantmentStat.from_dict({
                'name': key,
                'value': value
            }))

        return cls(
            identifier=data['enchantment_id'],
            display_string=data['display_string'],
            stats=item_enchantment_stats,
        )

    # Converts the enchantment to a JSON string
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

    # Creates a enchantment from a JSON string
    @classmethod
    def from_json(cls, json_str: str):
        return cls.from_dict(json.loads(json_str))
