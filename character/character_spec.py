import json


# Class: CharacterSpec
class CharacterSpec:
    # Spec identifier
    id: int
    # Spec name
    name: str
    # Spec slug
    slug: str
    # Spec enum
    enum: str

    # Class constructor
    def __init__(self, identifier: int, name: str, slug: str, enum: str):
        self.id = identifier
        self.name = name
        self.slug = slug
        self.enum = enum

    # Returns the spec identifier
    def get_identifier(self) -> int:
        return self.id

    # Returns the spec name
    def get_name(self) -> str:
        return self.name

    # Returns the spec slug
    def get_slug(self) -> str:
        return self.slug

    # Returns the spec enum
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
        return cls(data['id'], data['name'], data['slug'], data['enum'])

    # Converts class to a JSON string
    def to_json(self):
        return json.dumps(self.to_dict())

    # Creates a new instance from a JSON string
    @classmethod
    def from_json(cls, data):
        return cls.from_dict(json.loads(data))