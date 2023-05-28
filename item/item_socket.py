import re
import json
from item import ItemSocketStat


# Class: ItemSocket
class ItemSocket:
    # Socket gem identifier
    id: int
    # Socket gem name
    name: str
    # Socket gem display string
    display_string: str
    # Socket gem stats
    stats: list[ItemSocketStat]

    # Class constructor
    def __init__(self, identifier: int, name: str, display_string: str, stats: list[ItemSocketStat]):
        self.id = identifier
        self.name = name
        self.display_string = display_string
        self.stats = stats

    # Returns the socket gem identifier
    def get_identifier(self) -> int:
        return self.id

    # Returns the socket gem name
    def get_name(self) -> str:
        return self.name

    # Returns the socket gem display string
    def get_display_string(self) -> str:
        return self.display_string

    # Returns the socket gem stats
    def get_stats(self) -> list[ItemSocketStat]:
        return self.stats

    # Converts class to a dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'display_string': self.display_string,
            'stats': [stat.to_dict() for stat in self.stats],
        }

    # Creates class from a dictionary
    @classmethod
    def from_dict(cls, data: dict):
        socket_stats = []

        pattern = r'\+?(\d+)\s*([A-Za-z\s]+)'
        matches = re.findall(pattern, data['display_string'])

        for match in matches:
            value = int(match[0])
            key = match[1].strip()
            if 'and' in key:
                key = key.split('and')[0].strip()

            socket_stats.append(ItemSocketStat.from_dict({
                'name': key,
                'value': value
            }))

        return cls(
            identifier=data['item']['id'],
            name=data['item']['name'],
            display_string=data['display_string'],
            stats=socket_stats
        )

    # Converts the socket to a JSON string
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

    # Creates a socket from a JSON string
    @classmethod
    def from_json(cls, json_str: str):
        return cls.from_dict(json.loads(json_str))
