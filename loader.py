import requests
from bs4 import BeautifulSoup
from py_mini_racer import py_mini_racer
import json
from character import Character


# Class: Loader
class Loader:
    # Character name
    name: str
    # Character realm
    realm: str
    # Character region
    region: str
    # Character data
    data: dict

    # Class constructor
    def __init__(self, character: Character):
        self.name = character.get_name()
        self.realm = character.get_realm().lower()
        self.region = character.get_region().lower()
        self.load()

    # Returns the character name
    def get_name(self) -> str:
        return self.name

    # Returns the character realm
    def get_realm(self) -> str:
        return self.realm

    # Returns the character region
    def get_region(self) -> str:
        return self.region

    # Returns the character data
    def get_data(self) -> dict:
        return self.data

    # Loads character data
    def load(self):
        response = requests.get(self.build_request_url())
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
        self.data = parsed_data['summary']['character']['gear']

    # Returns the request URL
    def build_request_url(self) -> str:
        return f"https://worldofwarcraft.blizzard.com/en-gb/character/{self.region}/{self.realm}/{self.name}"
