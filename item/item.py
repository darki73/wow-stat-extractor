import json
from item import ItemStat, ItemSocket, ItemEnchantment


# Class: Item
class Item:
    # Item identifier
    identifier: int
    # Item name
    name: str
    # Item slot
    slot: str
    # Item level
    item_level: int
    # Item stats
    stats: list[ItemStat]
    # Item sockets
    sockets: list[ItemSocket]
    # Item enchantments
    enchantments: list[ItemEnchantment]

    # Class constructor
    def __init__(self, identifier: int, name: str, slot: str, item_level: int, item_stats: list[ItemStat], item_sockets: list[ItemSocket], item_enchantments: list[ItemEnchantment]):
        self.identifier = identifier
        self.name = name
        self.slot = slot
        self.item_level = item_level
        self.stats = item_stats
        self.sockets = item_sockets
        self.enchantments = item_enchantments

    # Returns the item identifier
    def get_identifier(self) -> int:
        return self.identifier

    # Returns the item name
    def get_name(self) -> str:
        return self.name

    # Returns the item slot
    def get_slot(self) -> str:
        return self.slot

    # Returns the item level
    def get_item_level(self) -> int:
        return self.item_level

    # Returns the item stats
    def get_stats(self) -> list[ItemStat]:
        return self.stats

    # Returns the item sockets
    def get_sockets(self) -> list[ItemSocket]:
        return self.sockets

    # Returns the item enchantments
    def get_enchantments(self) -> list[ItemEnchantment]:
        return self.enchantments

    # Converts class to a dictionary
    def to_dict(self):
        return {
            'identifier': self.identifier,
            'name': self.name,
            'item_level': self.item_level,
            'stats': [stat.to_dict() for stat in self.stats],
            'sockets': [socket.to_dict() for socket in self.sockets],
            'enchantments': [enchantment.to_dict() for enchantment in self.enchantments]
        }

    # Creates class from a dictionary
    @classmethod
    def from_dict(cls, data: dict):
        item_stats = []

        if 'stats' in data:
            for stat in data['stats']:
                if 'is_negated' in stat and stat['is_negated']:
                    continue

                if stat['type']['type'] == "COMBAT_RATING_STURDINESS":
                    continue

                item_stats.append(ItemStat.from_dict(stat))

        item_sockets = []

        if 'sockets' in data:
            for socket in data['sockets']:
                if 'item' in socket:
                    item_sockets.append(ItemSocket.from_dict(socket))

        item_enchantments = []

        if 'enchantments' in data:
            for enchantment in data['enchantments']:
                item_enchantments.append(ItemEnchantment.from_dict(enchantment))

        return cls(
            identifier=data['item']['id'],
            name=data['name'],
            slot=data['slot']['type'],
            item_level=data['level']['value'],
            item_stats=item_stats,
            item_sockets=item_sockets,
            item_enchantments=item_enchantments,
        )

    # Converts the item to a JSON string
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

    # Creates a item from a JSON string
    @classmethod
    def from_json(cls, json_str: str):
        return cls.from_dict(json.loads(json_str))
