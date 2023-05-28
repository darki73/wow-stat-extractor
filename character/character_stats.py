import json
from item import Item, stat_mapping


# Class: CharacterStats
class CharacterStats:
    # Character stamina
    stamina: int
    # Character strength
    strength: int
    # Character agility
    agility: int
    # Character intellect
    intellect: int
    # Character critical strike
    critical_strike: int
    # Character haste
    haste: int
    # Character mastery
    mastery: int
    # Character versatility
    versatility: int
    # Character leech
    leech: int
    # Character avoidance
    avoidance: int

    # Class constructor
    def __init__(self):
        self.stamina = 0
        self.strength = 0
        self.agility = 0
        self.intellect = 0
        self.critical_strike = 0
        self.haste = 0
        self.mastery = 0
        self.versatility = 0
        self.leech = 0
        self.avoidance = 0

    # Returns the character stamina
    def get_stamina(self) -> int:
        return self.stamina

    # Sets the character stamina
    def set_stamina(self, stamina: int):
        self.stamina = stamina

    # Returns the character strength
    def get_strength(self) -> int:
        return self.strength

    # Sets the character strength
    def set_strength(self, strength: int):
        self.strength = strength

    # Returns the character agility
    def get_agility(self) -> int:
        return self.agility

    # Sets the character agility
    def set_agility(self, agility: int):
        self.agility = agility

    # Returns the character intellect
    def get_intellect(self) -> int:
        return self.intellect

    # Sets the character intellect
    def set_intellect(self, intellect: int):
        self.intellect = intellect

    # Returns the character critical strike
    def get_critical_strike(self) -> int:
        return self.critical_strike

    # Sets the character critical strike
    def set_critical_strike(self, critical_strike: int):
        self.critical_strike = critical_strike

    # Returns the character haste
    def get_haste(self) -> int:
        return self.haste

    # Sets the character haste
    def set_haste(self, haste: int):
        self.haste = haste

    # Returns the character mastery
    def get_mastery(self) -> int:
        return self.mastery

    # Sets the character mastery
    def set_mastery(self, mastery: int):
        self.mastery = mastery

    # Returns the character versatility
    def get_versatility(self) -> int:
        return self.versatility

    # Sets the character versatility
    def set_versatility(self, versatility: int):
        self.versatility = versatility

    # Returns the character leech
    def get_leech(self) -> int:
        return self.leech

    # Sets the character leech
    def set_leech(self, leech: int):
        self.leech = leech

    # Returns the character avoidance
    def get_avoidance(self) -> int:
        return self.avoidance

    # Sets the character avoidance
    def set_avoidance(self, avoidance: int):
        self.avoidance = avoidance

    # Get primary stat value
    def get_primary_stat(self) -> int:
        primary_stats = [
            ('Strength', self.strength),
            ('Agility', self.agility),
            ('Intellect', self.intellect)
        ]
        primary_stat = next(((name, stat) for name, stat in primary_stats if stat > 0), (None, 0))
        return primary_stat[1]

    # Get primary stat name
    def get_primary_stat_name(self) -> str:
        primary_stats = [
            ('Strength', self.strength),
            ('Agility', self.agility),
            ('Intellect', self.intellect)
        ]
        primary_stat = next(((name, stat) for name, stat in primary_stats if stat > 0), (None, 0))
        return primary_stat[0] if primary_stat[0] is not None else 'None'

    # Converts identifier to stat name
    def identifier_to_name(self, identifier: str) -> str:
        for key, value in stat_mapping.items():
            if key == identifier:
                return value.replace(' ', '_')
        raise ValueError(f'Invalid identifier: {identifier}')

    # Increments a stat by a value
    def increment_stat(self, stat_type: str, stat_value: int):
        if hasattr(self, stat_type):
            current_value = getattr(self, stat_type)
            setattr(self, stat_type, current_value + stat_value)

    # Converts class to dict
    def to_dict(self):
        return {
            'stamina': self.get_stamina(),
            'strength': self.get_strength(),
            'agility': self.get_agility(),
            'intellect': self.get_intellect(),
            'critical_strike': self.get_critical_strike(),
            'haste': self.get_haste(),
            'mastery': self.get_mastery(),
            'versatility': self.get_versatility(),
            'leech': self.get_leech(),
            'avoidance': self.get_avoidance()
        }

    # Creates class from dict
    @classmethod
    def from_list(cls, data: list[Item]):
        instance = cls()

        for item in data:
            for stat in item.get_stats():
                stat_type = instance.identifier_to_name(stat.get_identifier()).lower()
                stat_value = stat.get_value()
                instance.increment_stat(stat_type, stat_value)

            for enchantment in item.get_enchantments():
                for stat in enchantment.get_stats():
                    stat_type = instance.identifier_to_name(stat.get_identifier()).lower()
                    if stat_type == 'primary_stat':
                        stat_type = instance.get_primary_stat_name().lower()
                    stat_value = stat.get_value()
                    instance.increment_stat(stat_type, stat_value)

            for socket in item.get_sockets():
                for stat in socket.get_stats():
                    stat_type = instance.identifier_to_name(stat.get_identifier()).lower()
                    if stat_type == 'primary_stat':
                        stat_type = instance.get_primary_stat_name().lower()
                    stat_value = stat.get_value()
                    instance.increment_stat(stat_type, stat_value)

        return instance

    # Converts the stat to a JSON string
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

