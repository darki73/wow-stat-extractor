import os
import json
from dotenv import load_dotenv


# Class: CharacterData
class CharacterData:
    # Character name
    _name: str = ""
    # Character realm
    _realm: str = ""
    # Character region
    _region: str = ""

    # Class constructor
    def __init__(self, name: str, realm: str, region: str):
        self._name = name
        self._realm = realm
        self._region = region

    # Returns the character name
    def get_name(self) -> str:
        return self._name

    # Returns the character realm
    def get_realm(self) -> str:
        return self._realm

    # Returns the character region
    def get_region(self) -> str:
        return self._region

    # Returns true if character data is configured
    def is_configured(self) -> bool:
        return self._name != "" and self._realm != "" and self._region != ""


# Class: Configurator
class Configurator:
    # Defines if we want to use the Blizzard Armory or the WoW API
    _legal: bool = True
    # Client token
    _client_token: str = ""
    # Client secret
    _client_secret: str = ""
    # First character data
    _first_character: CharacterData = None
    # Second character data
    _second_character: CharacterData = None

    # Class constructor
    def __init__(self):
        self._load_env()
        self._legal = self._get_env("BATTLE_NET_MAKE_IT_LEGAL", bool)
        self._client_token = self._get_env("BATTLE_NET_ACCESS_TOKEN", str)
        self._client_secret = self._get_env("BATTLE_NET_SECRET_TOKEN", str)

        self._first_character = CharacterData(
            self._get_env("FIRST_CHARACTER_NAME", str),
            self._get_env("FIRST_CHARACTER_REALM", str),
            self._get_env("FIRST_CHARACTER_REGION", str),
        )

        if self._first_character.is_configured() is False:
            print("The main character is not configured. (FIRST_CHARACTER_NAME, FIRST_CHARACTER_REALM, "
                  "FIRST_CHARACTER_REGION)")
            exit(1)

        self._second_character = CharacterData(
            self._get_env("SECOND_CHARACTER_NAME", str),
            self._get_env("SECOND_CHARACTER_REALM", str),
            self._get_env("SECOND_CHARACTER_REGION", str),
        )

        if self._second_character.is_configured() is False:
            self._second_character = None

        # Dumb check to see if we have the client token and client secret
        if self.make_it_legal():
            self.get_client_token()
            self.get_client_secret()

    # Returns if we want to use the Blizzard Armory or the WoW API
    def make_it_legal(self) -> bool:
        return self._legal

    # Returns the client token
    def get_client_token(self) -> str:
        if self.make_it_legal() and (self._client_token == "" or self._client_token is None):
            print(self._create_legal_undefined_message("client token"))
            exit(1)
        return self._client_token

    # Returns the client secret
    def get_client_secret(self) -> str:
        if self.make_it_legal() and (self._client_secret == "" or self._client_secret is None):
            print(self._create_legal_undefined_message("client secret"))
            exit(1)
        return self._client_secret

    # Returns the first character data
    def get_first_character(self) -> CharacterData:
        return self._first_character

    # Returns the second character data
    def get_second_character(self) -> CharacterData:
        return self._second_character

    # Returns the message about the unofficial use
    def get_unofficial_use_nag_message(self) -> str:
        return self._create_unofficial_use_nag_message()

    # Converts the class to dictionary
    def to_dict(self) -> dict:
        return {
            "legal": self.make_it_legal(),
            "client_token": self.get_client_token(),
            "client_secret": self.get_client_secret(),
            "first_character": self.get_first_character(),
            "second_character": self.get_second_character()
        }

    # Converts the class to json
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

    # Loads the .env file
    def _load_env(self):
        load_dotenv()

    # Returns path to the static folder
    def get_static_folder(self) -> str:
        return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static"))

    # Returns true if file exists
    def file_exists(self, file_name: str) -> bool:
        return os.path.isfile(self.get_file_path(file_name))

    # Returns the path to the file
    def get_file_path(self, file_name: str) -> str:
        return os.path.join(self.get_static_folder(), file_name)


    # Returns the environment variable by the given key of the given type
    def _get_env(self, key: str, var_type: type, raise_exception: bool = False):
        value = os.getenv(key).strip()

        if value is None:
            if raise_exception:
                raise Exception("Could not find environment variable with key {}".format(key))
            return None

        if var_type == bool:
            value = value == "true" or value == "True" or value == "TRUE" or value == "1"

        return var_type(value)

    # Generates a message for the given issue when we want to go the legal way
    def _create_legal_undefined_message(self, issue_with: str) -> str:
        base_message = "You want to go the legal way but you did not provide a {}.\n" \
                       "Please, consider using the official Battle.Net API instead of the Blizzard Armory.\n\n"
        base_message = self._get_message_separator() + base_message + self._create_unofficial_use_nag_message(
            appends=True)
        return base_message.format(
            issue_with
        )

    # Generates the message for the unofficial use
    def _create_unofficial_use_nag_message(self, appends: bool = False) -> str:
        message_string = "Blizzard did not intended (and actually prohibits) the use of the Blizzard Armory for" \
                         " this kind of use.\nIF you really have no idea on how to use API, i guess you can use" \
                         " the application in an unofficial way, however, i DO NOT condone this behavior.\n" \
                         "Otherwise, you can obtain API credentials at https://develop.battle.net/ and it is completely free!\n"
        if not appends:
            message_string = self._get_message_separator() + message_string

        return message_string + self._get_message_separator()

    # Returns the message separator
    def _get_message_separator(self) -> str:
        return "=====================================================\n"
