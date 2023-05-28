import json


# Class: ItemStat
class ItemStat:
    # Stat identifier
    id: str
    # Stat name
    name: str
    # Stat value
    value: int

    # Class constructor
    def __init__(self, identifier: str, name: str, value: int):
        self.id = identifier
        self.name = name
        self.value = value

    # Returns the stat identifier
    def get_identifier(self) -> str:
        return self.id

    # Returns the stat name
    def get_name(self) -> str:
        return self.name

    # Returns the stat value
    def get_value(self) -> int:
        return self.value

    # Converts class to a dictionary
    def to_dict(self):
        return {
            'type': self.get_identifier(),
            'name': self.get_name(),
            'value': self.get_value()
        }

    # Creates a new instance from a dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(
            identifier=data['type']['type'],
            name=data['type']['name'],
            value=data['value'],
        )

    # Converts the stat to a JSON string
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

    # Creates a stat from a JSON string
    @classmethod
    def from_json(cls, json_str: str):
        return cls.from_dict(json.loads(json_str))