from character.classes import BaseClass, BaseSpecialization


# Class: DemonHunterClass
class DemonHunterClass(BaseClass):
    # Class identifier
    id: int = 12
    # Class name
    name: str = "Demon Hunter"
    # Class slug
    slug: str = "demon_hunter"
    # Class enum
    enum: str = "DEMON_HUNTER"
    # Class specializations
    specializations: list[BaseSpecialization] = []
