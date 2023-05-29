from character.classes import BaseClass, BaseSpecialization


# Class: PaladinClass
class PaladinClass(BaseClass):
    # Class identifier
    id: int = 2
    # Class name
    name: str = "Paladin"
    # Class slug
    slug: str = "paladin"
    # Class enum
    enum: str = "PALADIN"
    # Class specializations
    specializations: list[BaseSpecialization] = []
