from character.classes import BaseClass, BaseSpecialization


# Class: WarriorClass
class WarriorClass(BaseClass):
    # Class identifier
    id: int = 6
    # Class name
    name: str = "Warrior"
    # Class slug
    slug: str = "warrior"
    # Class enum
    enum: str = "WARRIOR"
    # Class specializations
    specializations: list[BaseSpecialization] = []
