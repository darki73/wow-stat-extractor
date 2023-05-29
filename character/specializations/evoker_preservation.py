from character.classes import \
    BaseSpecialization, \
    SpecializationStatBonus, \
    BaseStatPerPercent, \
    BaseCriticalStrikeStatPerPercent, \
    BaseHasteStatPerPercent, \
    BaseMasteryStatPerPercent, \
    BaseVersatilityStatPerPercent


# Class: EvokerPreservationCriticalStrikeStatPerPercent
class EvokerPreservationCriticalStrikeStatPerPercent(BaseCriticalStrikeStatPerPercent):
    # Stat value per percent
    value_per_percent: float = 180.0


# Class: EvokerPreservationHasteStatPerPercent
class EvokerPreservationHasteStatPerPercent(BaseHasteStatPerPercent):
    # Stat value per percent
    value_per_percent: float = 170.0


# Class: EvokerPreservationMasteryStatPerPercent
class EvokerPreservationMasteryStatPerPercent(BaseMasteryStatPerPercent):
    # Stat value per percent
    value_per_percent: float = 100.0


# Class: EvokerPreservationVersatilityStatPerPercent
class EvokerPreservationVersatilityStatPerPercent(BaseVersatilityStatPerPercent):
    # Stat value per percent
    value_per_percent: float = 205.0


# Class: EvokerPreservationSpecialization
class EvokerPreservationSpecialization(BaseSpecialization):
    # Specialization identifier
    id: int = 1468
    # Specialization name
    name: str = "Preservation"
    # Specialization slug
    slug: str = "preservation"
    # Specialization enum
    enum: str = "PRESERVATION"
    # Specialization stat bonuses
    stat_bonuses: list[SpecializationStatBonus] = []
    # Class stat per percent
    stat_per_percent: list[BaseStatPerPercent] = [
        EvokerPreservationCriticalStrikeStatPerPercent(),
        EvokerPreservationHasteStatPerPercent(),
        EvokerPreservationMasteryStatPerPercent(),
        EvokerPreservationVersatilityStatPerPercent(),
    ]
