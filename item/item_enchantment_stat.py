import json
from item import stat_mapping


# Class: ItemEnchantmentStat
class ItemEnchantmentStat:
    # Enchantment stat identifier
    identifier: str
    # Enchantment stat name
    name: str
    # Enchantment stat value
    value: int

    # Class constructor
    def __init__(self, name: str, value: int):
        self.name = name
        self.name_to_identifier()
        self.value = value

    # Returns the enchantment stat identifier
    def get_identifier(self) -> str:
        return self.identifier

    # Returns the enchantment stat name
    def get_name(self) -> str:
        return self.name

    # Returns the enchantment stat value
    def get_value(self) -> int:
        return self.value

    # Converts the enchantment stat name to an identifier
    def name_to_identifier(self):
        inverse_mapping = {v: k for k, v in stat_mapping.items()}
        if self.name in inverse_mapping:
            self.identifier = inverse_mapping[self.name]
        else:
            raise Exception("Unknown stat name: " + self.name)

    # Converts class to a dictionary
    def to_dict(self):
        return {
            'id': self.get_identifier(),
            'name': self.get_name(),
            'value': self.get_value(),
        }

    # Creates class from a dictionary
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data['name'],
            value=data['value']
        )

    # Converts the enchantment stat to a JSON string
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

    # Creates a enchantment stat from a JSON string
    @classmethod
    def from_json(cls, json_str: str):
        return cls.from_dict(json.loads(json_str))
