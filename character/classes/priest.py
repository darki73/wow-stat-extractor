from character.classes import BaseClass, BaseSpecialization


# Class: PriestClass
class PriestClass(BaseClass):
    # Class identifier
    id: int = 5
    # Class name
    name: str = "Priest"
    # Class slug
    slug: str = "priest"
    # Class enum
    enum: str = "PRIEST"
    # Class specializations
    specializations: list[BaseSpecialization] = []
