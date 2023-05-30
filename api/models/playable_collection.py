import json
from api.models import Playable
from helpers import Configurator


# Class: PlayableCollection
class PlayableCollection:
    # Items list
    _items: list[Playable]

    # Class constructor
    def __init__(self):
        self._items = []

    # Adds an item to the collection
    def add(self, item: Playable):
        self._items.append(item)

    # Creates a collection from an api response
    @classmethod
    def from_api(cls, data: dict) -> "PlayableCollection":
        collection = cls()
        for item in data:
            collection.add(Playable(
                item["id"],
                item["name"],
            ))
        return collection

    # Creates a collection from local data
    @classmethod
    def from_local(cls, configuration: Configurator, file_name: str) -> "PlayableCollection":
        with open(f"{configuration.get_static_folder()}/{file_name}") as file:
            data = json.load(file)

        collection = cls()

        for item in data:
            collection.add(Playable(
                item["id"],
                item["name"],
                item["slug"],
                item["enum"],
            ))

        return collection

    # Converts class to a dictionary
    def to_dict(self) -> list[dict]:
        return [item.to_dict() for item in self._items]

    # Converts class to JSON
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
