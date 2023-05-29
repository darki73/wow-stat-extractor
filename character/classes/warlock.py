from character.classes import BaseClass, BaseSpecialization


# Class: WarlockClass
class WarlockClass(BaseClass):
    # Class identifier
    id: int = 9
    # Class name
    name: str = "Warlock"
    # Class slug
    slug: str = "warlock"
    # Class enum
    enum: str = "WARLOCK"
    # Class specializations
    specializations: list[BaseSpecialization] = []
