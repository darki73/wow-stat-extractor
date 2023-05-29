from character.classes import BaseClass, BaseSpecialization


# Class: DruidClass
class DruidClass(BaseClass):
    # Class identifier
    id: int = 11
    # Class name
    name: str = "Druid"
    # Class slug
    slug: str = "druid"
    # Class enum
    enum: str = "DRUID"
    # Class specializations
    specializations: list[BaseSpecialization] = []
