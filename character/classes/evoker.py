from character.classes import BaseClass, BaseSpecialization
from character.specializations import \
    EvokerDevastationSpecialization, \
    EvokerPreservationSpecialization, \
    EvokerAugmentationSpecialization


# Class: EvokerClass
class EvokerClass(BaseClass):
    # Class identifier
    id: int = 13
    # Class name
    name: str = "Evoker"
    # Class slug
    slug: str = "evoker"
    # Class enum
    enum: str = "EVOKER"
    # Class specializations
    specializations: list[BaseSpecialization] = [
        EvokerDevastationSpecialization(),
        EvokerPreservationSpecialization(),
        EvokerAugmentationSpecialization(),
    ]
