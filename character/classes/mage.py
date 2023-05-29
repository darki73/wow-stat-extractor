from character.classes import BaseClass, BaseSpecialization


# Class: MageClass
class MageClass(BaseClass):
    # Class identifier
    id: int = 9
    # Class name
    name: str = "Mage"
    # Class slug
    slug: str = "mage"
    # Class enum
    enum: str = "MAGE"
    # Class specializations
    specializations: list[BaseSpecialization] = []
