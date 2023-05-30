import re
import json
import unicodedata
from .character_class import CharacterClass
from .character_faction import CharacterFaction
from .character_gender import CharacterGender
from .character_race import CharacterRace
from .character_spec import CharacterSpec
from .character_stats import CharacterStats
from item import Item
from helpers import CharacterData


# Class: Character
class Character:
    # Character Name
    name: str
    # Character Realm
    realm: str
    # Character Region
    region: str
    # Character Level
    level: int
    # Character Item Level
    item_level: int
    # Character Class
    character_class: CharacterClass
    # Character Faction
    character_faction: CharacterFaction
    # Character Gear
    character_gear: list[Item]
    # Character Gender
    character_gender: CharacterGender
    # Character Race
    character_race: CharacterRace
    # Character Spec
    character_spec: CharacterSpec
    # Character Stats
    character_stats: CharacterStats

    # Class constructor
    def __init__(self, character_data: CharacterData):
        self.name = character_data.get_name()
        self.realm = character_data.get_realm()
        self.region = character_data.get_region()
        self.level = 0
        self.item_level = 0
        self.character_class = None
        self.character_faction = None
        self.character_gear = []
        self.character_gender = None
        self.character_race = None
        self.character_spec = None
        self.character_stats = None

    # Returns the character name
    def get_name(self) -> str:
        return self.name

    # Returns the character realm
    def get_realm(self) -> str:
        return self.realm

    # Returns the character realm slug
    def get_realm_slug(self) -> str:
        normalized_name = unicodedata.normalize('NFKD', self.get_realm())
        normalized_name = re.sub(r'[^\w\s-]', '', normalized_name)
        slug = normalized_name.strip().lower().replace(' ', '-')
        return re.sub(r'-+', '-', slug)

    # Returns the character region
    def get_region(self) -> str:
        return self.region.lower()

    # Returns the character level
    def get_level(self) -> int:
        return self.level

    # Returns the character item level
    def get_item_level(self) -> int:
        return self.item_level

    # Returns the character class
    def get_character_class(self) -> CharacterClass:
        return self.character_class

    # Returns the character faction
    def get_character_faction(self) -> CharacterFaction:
        return self.character_faction

    # Returns the character gear
    def get_character_gear(self) -> list[Item]:
        return self.character_gear

    # Returns the character gender
    def get_character_gender(self) -> CharacterGender:
        return self.character_gender

    # Returns the character race
    def get_character_race(self) -> CharacterRace:
        return self.character_race

    # Returns the character spec
    def get_character_spec(self) -> CharacterSpec:
        return self.character_spec

    # Returns the character stats
    def get_character_stats(self) -> CharacterStats:
        return self.character_stats

    # Converts the character to a dictionary
    def to_dict(self) -> dict:
        return {
            'name': self.get_name(),
            'realm': self.get_realm(),
            'region': self.get_region(),
            'level': self.get_level(),
            'item_level': self.get_item_level(),
            'class': self.character_class.to_dict() if self.character_class else None,
            'faction': self.character_faction.to_dict() if self.character_faction else None,
            'gear': {item.get_slot(): item.to_dict() for item in
                     self.get_character_gear()} if self.character_gear else None,  # noqa: E501
            'gender': self.character_gender.to_dict() if self.character_gender else None,
            'race': self.character_race.to_dict() if self.character_race else None,
            'spec': self.character_spec.to_dict() if self.character_spec else None,
            'stats': self.character_stats.to_dict() if self.character_stats else None
        }

    # Creates a character from a dictionary
    @classmethod
    def from_dict(cls, data: dict, region: str = None):
        if 'region' not in data:
            if region is None:
                raise ValueError('Region is required')
            data['region'] = region

        character = cls(CharacterData(data['name'], data['realm']['name'], data['region']))
        character.level = data['level']

        if 'averageItemLevel' in data:
            character.item_level = data['averageItemLevel']

        if 'equipped_item_level' in data and 'averageItemLevel' not in data:
            character.item_level = data['equipped_item_level']

        if 'class' in data:
            character.character_class = CharacterClass.from_dict(data['class'])

        if 'character_class' in data and 'class' not in data:
            character.character_class = CharacterClass.from_dict(data['character_class'])

        if 'faction' in data:
            character.character_faction = CharacterFaction.from_dict(data['faction'])

        if 'gear' in data:
            if isinstance(data['gear'], list):
                for item in data['gear']:
                    character.character_gear.append(Item.from_dict(item))
            else:
                for slot, item in data['gear'].items():
                    character.character_gear.append(Item.from_dict(item))

        if 'gender' in data:
            character.character_gender = CharacterGender.from_dict(data['gender'])

        if 'race' in data:
            character.character_race = CharacterRace.from_dict(data['race'])

        if 'spec' in data:
            character.character_spec = CharacterSpec.from_dict(data['spec'])

        if 'active_spec' in data and 'spec' not in data:
            character.character_spec = CharacterSpec.from_dict(data['active_spec'])

        character.character_stats = CharacterStats.from_list(character.character_gear)

        return character

    # Creates a character from an api dictionary
    @classmethod
    def from_api_dict(cls, data: dict, region: str = None):
        if 'region' not in data:
            if region is None:
                raise ValueError('Region is required')
            data['region'] = region
        print(json.dumps(data, indent=4))

    # Converts the character to a JSON string
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

    # Creates a character from a JSON string
    @classmethod
    def from_json(cls, json_str: str):
        return cls.from_dict(json.loads(json_str))
