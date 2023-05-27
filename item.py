import re

stat_mapping = {
    'INTELLECT': "Intellect",
    'STRENGTH': "Strength",
    'AGILITY': "Agility",
    'STAMINA': "Stamina",
    'CRIT_RATING': "Critical Strike",
    'HASTE_RATING': "Haste",
    'MASTERY_RATING': "Mastery",
    'VERSATILITY': "Versatility",
    'COMBAT_RATING_LIFESTEAL': "Leech",
    'COMBAT_RATING_AVOIDANCE': "Avoidance",
    'COMBAT_RATING_SPEED': "Speed",
}


# Class: ItemStat
class ItemStat:
    # Stat identifier
    identifier: str
    # Stat name
    name: str
    # Stat value
    value: int

    # Class constructor
    def __init__(self, identifier: str, value: int):
        self.identifier = identifier
        self.identifier_to_name()
        self.value = value

    # Returns the string representation of the stat
    def __str__(self):
        return self.name + ": " + str(self.value)

    # Returns the stat identifier
    def get_identifier(self) -> str:
        return self.identifier

    # Returns the stat name
    def get_name(self) -> str:
        return self.name

    # Returns the stat value
    def get_value(self) -> int:
        return self.value

    # Converts the stat identifier to a name
    def identifier_to_name(self):
        if self.identifier in stat_mapping:
            self.name = stat_mapping[self.identifier]
        else:
            raise Exception("Unknown stat identifier: " + self.identifier)


# Class: ItemSocketStat
class ItemSocketStat:
    # Socket stat identifier
    identifier: str
    # Socket stat name
    name: str
    # Socket stat value
    value: int

    # Class constructor
    def __init__(self, name: str, value: int):
        self.name = name
        self.name_to_identifier()
        self.value = value

    # Returns the string representation of the socket stat
    def __str__(self):
        return self.name + ": " + str(self.value)

    # Returns the socket stat identifier
    def get_identifier(self) -> str:
        return self.identifier

    # Returns the socket stat name
    def get_name(self) -> str:
        return self.name

    # Returns the socket stat value
    def get_value(self) -> int:
        return self.value

    # Converts the socket stat name to an identifier
    def name_to_identifier(self):
        for key, value in stat_mapping.items():
            if value == self.name:
                self.identifier = key
                return


# Class: ItemSocket
class ItemSocket:
    # Socket gem identifier
    identifier: int
    # Socket display string
    display_string: str
    # Socket stats
    stats: list[ItemSocketStat]

    # Class constructor
    def __init__(self, identifier: int, display_string: str):
        self.identifier = identifier
        self.display_string = display_string
        self.stats = []
        self.parse()

    # Returns the socket gem identifier
    def get_identifier(self) -> int:
        return self.identifier

    # Returns the socket display string
    def get_display_string(self) -> str:
        return self.display_string

    # Returns the socket stats
    def get_stats(self) -> list[ItemSocketStat]:
        return self.stats

    # Parses the display string
    def parse(self):
        pattern = r'\+?(\d+)\s*([A-Za-z\s]+)'
        matches = re.findall(pattern, self.display_string)

        for match in matches:
            value = int(match[0])
            key = match[1].strip()
            if 'and' in key:
                key = key.split('and')[0].strip()
            self.stats.append(ItemSocketStat(key, value))


# Class: Item
class Item:
    # Item identifier
    identifier: int
    # Item name
    name: str
    # Item level
    item_level: int
    # Item stats
    stats: list[ItemStat]
    # Item sockets
    sockets: list[ItemSocket]
    # Item slot
    slot: str

    # Class constructor
    def __init__(self, identifier: int, name: str, item_level: int, stats: list[ItemStat], sockets: list[ItemSocket],
                 slot: str):
        self.identifier = identifier
        self.name = name
        self.item_level = item_level
        self.stats = stats
        self.sockets = sockets
        self.slot = slot

    # Returns the item identifier
    def get_identifier(self) -> int:
        return self.identifier

    # Returns the item name
    def get_name(self) -> str:
        return self.name

    # Returns the item level
    def get_item_level(self) -> int:
        return self.item_level

    # Returns the item stats
    def get_stats(self) -> list[ItemStat]:
        return self.stats

    # Returns the item sockets
    def get_sockets(self) -> list[ItemSocket]:
        return self.sockets

    # Returns the item slot
    def get_slot(self) -> str:
        return self.slot

    # Class constructor
    @staticmethod
    def from_json(data: dict, slot: str):
        item_stats = []
        item_sockets = []

        if 'stats' in data:
            for stat in data['stats']:
                if 'is_negated' in stat and stat['is_negated']:
                    continue

                stat_type = stat['type']['type']
                stat_value = stat['value']
                if stat_type == "COMBAT_RATING_STURDINESS":
                    continue

                item_stat = ItemStat(stat_type, stat_value)

                if slot == "chest":
                    if stat_type in ['STRENGTH', 'AGILITY', 'INTELLECT']:
                        stat_mapping[stat_type] = "Primary Stat"

                item_stats.append(item_stat)

        if 'sockets' in data:
            for socket in data['sockets']:
                item_sockets.append(ItemSocket(socket['item']['id'], socket['display_string']))

        return Item(
            data['item']['id'],
            data['name'],
            data['level']['value'],
            item_stats,
            item_sockets,
            slot,
        )
