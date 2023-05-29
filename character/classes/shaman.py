from character.classes import BaseClass, BaseSpecialization


# Class: ShamanClass
class ShamanClass(BaseClass):
    # Class identifier
    id: int = 7
    # Class name
    name: str = "Shaman"
    # Class slug
    slug: str = "shaman"
    # Class enum
    enum: str = "SHAMAN"
    # Class specializations
    specializations: list[BaseSpecialization] = []
