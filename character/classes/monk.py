from character.classes import BaseClass, BaseSpecialization


# Class: MonkClass
class MonkClass(BaseClass):
    # Class identifier
    id: int = 10
    # Class name
    name: str = "Monk"
    # Class slug
    slug: str = "monk"
    # Class enum
    enum: str = "MONK"
    # Class specializations
    specializations: list[BaseSpecialization] = []
