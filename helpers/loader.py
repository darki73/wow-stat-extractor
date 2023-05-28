import json
import requests
from bs4 import BeautifulSoup
from py_mini_racer import py_mini_racer
from character import Character


# Class: Loader
class Loader:
    # Character instance
    character: Character

    # Class constructor
    def __init__(self, character: Character):
        self.character = character

    # Loads character information from the Blizzard Armory
    def load(self) -> Character:
        response = requests.get(self._build_request_url())
        soup = BeautifulSoup(response.text, "html.parser")
        js_data = None

        scripts = soup.find_all("script")
        for script in scripts:
            if 'characterProfileInitialState' in script.text:
                js_data = script.text
                break

        if js_data is None:
            raise Exception("Could not find characterProfileInitialState")

        context = py_mini_racer.MiniRacer()
        context.eval(js_data)
        json_object = context.eval("JSON.stringify(characterProfileInitialState)")

        parsed_data = json.loads(json_object)
        character_data = parsed_data['summary']['character']
        return self.character.from_dict(character_data)

    # Returns the request URL
    def _build_request_url(self) -> str:
        region = self.character.get_region()
        realm = self.character.get_realm_slug()
        name = self.character.get_name()

        return f"https://worldofwarcraft.blizzard.com/en-gb/character/{region}/{realm}/{name}"
