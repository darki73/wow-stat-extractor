from character.classes import BaseClass, BaseSpecialization


# Class: DeathKnightClass
class DeathKnightClass(BaseClass):
    # Class identifier
    id: int = 6
    # Class name
    name: str = "Death Knight"
    # Class slug
    slug: str = "death_knight"
    # Class enum
    enum: str = "DEATH_KNIGHT"
    # Class specializations
    specializations: list[BaseSpecialization] = []
