import json
from typing import Dict
from item import Item


# Class: CharacterGear
class CharacterGear:
    # Items dictionary (<slot, item>)
    items: Dict[str, Item]

    # Converts class to dict
    def to_dict(self):
        print(self.items)
        result = {}

        for slot, item in self.items.items():
            result[slot] = item.to_dict()

        return result

    # Creates class from dict
    @classmethod
    def from_dict(cls, data: dict):
        for slot, entity in data.items():
            data[slot] = Item.from_dict(entity)

    # Converts the character to a JSON string
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

    # Creates a character from a JSON string
    @classmethod
    def from_json(cls, json_str: str):
        return cls.from_dict(json.loads(json_str))