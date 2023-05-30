import json
import requests
from bs4 import BeautifulSoup
from py_mini_racer import py_mini_racer
from character import Character
from helpers import Configurator
from api import API


# Class: Loader
class Loader:
    # Configuration instance
    _configuration: Configurator
    # Character instance
    _character: Character
    # API instance
    _api: API

    # Class constructor
    def __init__(self, configuration: Configurator, character: Character):
        self._configuration = configuration
        self._character = character
        self._api = API(self._character, self._configuration)

    # Loads character information from the Blizzard Armory
    def load(self) -> Character:
        if self._configuration.make_it_legal() is False:
            return self._get_data_from_armory()
        return self._get_data_from_api()

    # Returns the data obtained from the Blizzard Armory (unofficial way)
    def _get_data_from_armory(self) -> Character:
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
        return self._character.from_dict(character_data)

    # Returns the data obtained from the Blizzard API (official way)
    def _get_data_from_api(self) -> Character:
        base_information = self._api.get_character_base_information()
        gear_information = self._api.get_character_gear_information()
        base_information['gear'] = gear_information['equipped_items']

        return self._character.from_dict(base_information, self._character.get_region().lower())

    # Returns the request URL
    def _build_request_url(self) -> str:
        region = self._character.get_region()
        realm = self._character.get_realm_slug()
        name = self._character.get_name()

        return f"https://worldofwarcraft.blizzard.com/en-gb/character/{region}/{realm}/{name}"

    # Builds the API URL
    def _build_api_url(self, namespace: str, locale: str, endpoint: str) -> str:
        return "https://{}.{}/profile/wow/character/{}/{}/{}?namespace={}&locale={}&access_token={}".format(
            self._character.get_region().lower(),
            "api.blizzard.com",
            self._character.get_realm_slug().lower(),
            self._character.get_name().lower(),
            endpoint,
            namespace,
            locale,
            self._retrieve_access_token()
        )

    # Returns the access token
    def _retrieve_access_token(self) -> str:
        response = requests.post(
            "https://{}.battle.net/oauth/token".format(self._character.get_region().lower()),
            data={
                "grant_type": "client_credentials"
            },
            auth=(
                self._configuration.get_client_token(),
                self._configuration.get_client_secret(),
            )
        )

        response_json = response.json()
        return response_json["access_token"]
