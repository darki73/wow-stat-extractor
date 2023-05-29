from character.classes import \
    BaseSpecialization, \
    SpecializationStatBonus, \
    BaseStatPerPercent, \
    BaseMasteryStatBonus, \
    BaseCriticalStrikeStatPerPercent, \
    BaseHasteStatPerPercent, \
    BaseMasteryStatPerPercent, \
    BaseVersatilityStatPerPercent


# Class: EvokerDevastationCriticalStrikeStatPerPercent
class EvokerDevastationCriticalStrikeStatPerPercent(BaseCriticalStrikeStatPerPercent):
    # Stat value per percent
    value_per_percent: float = 180.0


# Class: EvokerDevastationHasteStatPerPercent
class EvokerDevastationHasteStatPerPercent(BaseHasteStatPerPercent):
    # Stat value per percent
    value_per_percent: float = 170.0


# Class: EvokerDevastationMasteryStatPerPercent
class EvokerDevastationMasteryStatPerPercent(BaseMasteryStatPerPercent):
    # Stat value per percent
    value_per_percent: float = 72.0


# Class: EvokerDevastationVersatilityStatPerPercent
class EvokerDevastationVersatilityStatPerPercent(BaseVersatilityStatPerPercent):
    # Stat value per percent
    value_per_percent: float = 205.0


# Class: EvokerDevastationSpecializationMasteryStatBonus
class EvokerDevastationSpecializationMasteryStatBonus(BaseMasteryStatBonus):
    # Stat value
    value: int = 22.5


# Class: EvokerDevastationSpecialization
class EvokerDevastationSpecialization(BaseSpecialization):
    # Specialization identifier
    id: int = 1467
    # Specialization name
    name: str = "Devastation"
    # Specialization slug
    slug: str = "devastation"
    # Specialization enum
    enum: str = "DEVASTATION"
    # Specialization stat bonuses
    stat_bonuses: list[SpecializationStatBonus] = [
        EvokerDevastationSpecializationMasteryStatBonus(),

    ]
    # Class stat per percent
    stat_per_percent: list[BaseStatPerPercent] = [
        EvokerDevastationCriticalStrikeStatPerPercent(),
        EvokerDevastationHasteStatPerPercent(),
        EvokerDevastationMasteryStatPerPercent(),
        EvokerDevastationVersatilityStatPerPercent(),
    ]
