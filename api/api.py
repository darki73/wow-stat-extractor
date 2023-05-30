import json
import os.path
import time
import requests
from api.models import PlayableCollection
from character import Character
from helpers import Configurator

# Class: API
class API:
    # Character instance
    _character: Character
    # Configuration instance
    _configuration: Configurator
    # API region
    _region: str
    # API namespace
    _namespace: str
    # API locale
    _locale: str
    # API access token
    _access_token: str
    # API base URL
    _base_url: str

    # Class constructor
    def __init__(self, character: Character, configuration: Configurator):
        self._character = character
        self._configuration = configuration
        self._region = self._character.get_region().lower()
        self._namespace = self._deduce_namespace()
        self._locale = self._deduce_locale()
        self._access_token = self._retrieve_access_token()
        self._base_url = self._generate_base_url()
        self._bootstrap()

    # Returns the API region
    def get_region(self) -> str:
        return self._region

    # Returns the API namespace
    def get_namespace(self) -> str:
        return self._namespace

    # Returns the API locale
    def get_locale(self) -> str:
        return self._locale

    # Returns character base information
    def get_character_base_information(self) -> dict:
        return self._get(self._profile_url(""))

    # Returns character equipment information
    def get_character_gear_information(self) -> dict:
        return self._get(self._profile_url("equipment"))

    # Bootstraps the API
    def _bootstrap(self):
        if self._should_download("classes.json"):
            self._download_data("playable-class/index", "classes.json", "classes")
        if self._should_download("races.json"):
            self._download_data("playable-race/index", "races.json", "races")
        if self._should_download("specializations.json"):
            self._download_data("playable-specialization/index", "specializations.json", "character_specializations")

    def _get(self, url: str) -> dict:
        response = requests.get(url)
        response_json = response.json()
        response_json.pop("_links", None)
        return response_json

    # Returns the access token
    def _retrieve_access_token(self) -> str:
        response = requests.post(
            "https://{}.battle.net/oauth/token".format(self._region),
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

    # Deduces the namespace based on the character region
    def _deduce_namespace(self) -> str:
        region_based_namespace = {
            "eu": "profile-eu",
            "us": "profile-us",
        }

        if self._character.get_region() not in region_based_namespace:
            raise Exception("Region not supported")

        return region_based_namespace[self._region]

    # Deduces the locale based on the character region
    def _deduce_locale(self) -> str:
        region_based_locale = {
            "eu": "en_GB",
            "us": "en_US",
        }

        if self._character.get_region() not in region_based_locale:
            raise Exception("Region not supported")

        return region_based_locale[self._region]

    # Generates the base URL
    def _generate_base_url(self) -> str:
        return "https://{}.api.blizzard.com".format(
            self._region,
        )

    # Returns the data endpoint URL
    def _data_url(self, endpoint: str) -> str:
        return "{}/data/wow/{}?namespace={}&locale={}&access_token={}".format(
            self._base_url,
            endpoint,
            self._namespace.replace("profile", "static"),
            self._locale,
            self._access_token,
        )

    # Returns the profile endpoint URL
    def _profile_url(self, endpoint: str) -> str:
        return "{}/profile/wow/character/{}/{}{}{}?namespace={}&locale={}&access_token={}".format(
            self._base_url,
            self._character.get_realm_slug().lower(),
            self._character.get_name().lower(),
            "" if endpoint == "" else "/",
            endpoint,
            self._namespace,
            self._locale,
            self._access_token,
        )

    # Returns true if the file should be downloaded
    def _should_download(self, file_name: str) -> bool:
        if not self._configuration.file_exists(file_name):
            return True

        is_old = (time.time() - os.path.getmtime(self._configuration.get_file_path(file_name))) > 604800
        if is_old:
            os.remove(self._configuration.get_file_path(file_name))
            return True

        return False

    # Downloads data from the data endpoint
    def _download_data(self, endpoint: str, file_name: str, accessor: str):
        response = requests.get(self._data_url(endpoint))
        response_json = response.json()[accessor]

        collection = PlayableCollection.from_api(response_json)
        with open(self._configuration.get_file_path(file_name), "w") as file:
            file.write(collection.to_json())

    # Converts class to dict
    def to_dict(self) -> dict:
        return {
            "region": self._region,
            "namespace": self._namespace,
            "locale": self._locale,
            "access_token": self._access_token,
            "base_url": self._base_url,
        }

    # Converts class to JSON
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)