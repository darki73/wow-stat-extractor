import json
from helpers import name_to_enum, name_to_slug


# Class: Playable
class Playable:
    # Identifier
    _id: int
    # Name
    _name: str
    # Slug
    _slug: str
    # Enum
    _enum: str

    # Class constructor
    def __init__(self, identifier: int, name: str, slug: str = None, enum: str = None):
        self._id = identifier
        self._name = name
        self._slug = slug if slug is not None else name_to_slug(name)
        self._enum = enum if enum is not None else name_to_enum(name)

    # Returns the identifier
    def get_id(self) -> int:
        return self._id

    # Returns the name
    def get_name(self) -> str:
        return self._name

    # Returns the slug
    def get_slug(self) -> str:
        return self._slug

    # Returns the enum
    def get_enum(self) -> str:
        return self._enum

    # Converts class to a dictionary
    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "name": self._name,
            "slug": self._slug,
            "enum": self._enum,
        }

    # Converts class to JSON
    def to_json(self) -> str:
        return json.dumps(self.to_dict())
