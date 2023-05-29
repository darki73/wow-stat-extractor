from character.classes import BaseClass, BaseSpecialization


# Class: HunterClass
class HunterClass(BaseClass):
    # Class identifier
    id: int = 3
    # Class name
    name: str = "Hunter"
    # Class slug
    slug: str = "hunter"
    # Class enum
    enum: str = "HUNTER"
    # Class specializations
    specializations: list[BaseSpecialization] = []
