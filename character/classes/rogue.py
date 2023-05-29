from character.classes import BaseClass, BaseSpecialization


# Class: RogueClass
class RogueClass(BaseClass):
    # Class identifier
    id: int = 4
    # Class name
    name: str = "Rogue"
    # Class slug
    slug: str = "rogue"
    # Class enum
    enum: str = "ROGUE"
    # Class specializations
    specializations: list[BaseSpecialization] = []
