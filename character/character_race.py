import json
from helpers import name_to_slug, name_to_enum


# Class: CharacterRace
class CharacterRace:
    # Race identifier
    id: int
    # Race name
    name: str
    # Race slug
    slug: str
    # Race enum
    enum: str

    # Class constructor
    def __init__(self, identifier: int, name: str, slug: str, enum: str):
        self.id = identifier
        self.name = name
        self.slug = slug
        self.enum = enum

    # Returns the race identifier
    def get_identifier(self) -> int:
        return self.id

    # Returns the race name
    def get_name(self) -> str:
        return self.name

    # Returns the race slug
    def get_slug(self) -> str:
        return self.slug

    # Returns the race enum
    def get_enum(self) -> str:
        return self.enum

    # Converts class to a dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'enum': self.enum
        }

    # Creates a new instance from a dictionary
    @classmethod
    def from_dict(cls, data):
        if 'slug' not in data:
            data['slug'] = name_to_slug(data['name'])
        if 'enum' not in data:
            data['enum'] = name_to_enum(data['name'])
        return cls(data['id'], data['name'], data['slug'], data['enum'])

    # Converts class to a JSON string
    def to_json(self):
        return json.dumps(self.to_dict())

    # Creates a new instance from a JSON string
    @classmethod
    def from_json(cls, data):
        return cls.from_dict(json.loads(data))
