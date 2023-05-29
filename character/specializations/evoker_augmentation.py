from character.classes import \
    BaseSpecialization, \
    SpecializationStatBonus, \
    BaseStatPerPercent, \
    BaseCriticalStrikeStatPerPercent, \
    BaseHasteStatPerPercent, \
    BaseMasteryStatPerPercent, \
    BaseVersatilityStatPerPercent


# Class: EvokerAugmentationCriticalStrikeStatPerPercent
class EvokerAugmentationCriticalStrikeStatPerPercent(BaseCriticalStrikeStatPerPercent):
    # Stat value per percent
    value_per_percent: float = 180.0


# Class: EvokerAugmentationHasteStatPerPercent
class EvokerAugmentationHasteStatPerPercent(BaseHasteStatPerPercent):
    # Stat value per percent
    value_per_percent: float = 170.0


# Class: EvokerAugmentationMasteryStatPerPercent
class EvokerAugmentationMasteryStatPerPercent(BaseMasteryStatPerPercent):
    # Stat value per percent
    value_per_percent: float = 100.0


# Class: EvokerAugmentationVersatilityStatPerPercent
class EvokerAugmentationVersatilityStatPerPercent(BaseVersatilityStatPerPercent):
    # Stat value per percent
    value_per_percent: float = 205.0


# Class: EvokerAugmentationSpecialization
class EvokerAugmentationSpecialization(BaseSpecialization):
    # Specialization identifier
    id: int = 1469
    # Specialization name
    name: str = "Augmentation"
    # Specialization slug
    slug: str = "augmentation"
    # Specialization enum
    enum: str = "AUGMENTATION"
    # Specialization stat bonuses
    stat_bonuses: list[SpecializationStatBonus] = []
    # Class stat per percent
    stat_per_percent: list[BaseStatPerPercent] = [
        EvokerAugmentationCriticalStrikeStatPerPercent(),
        EvokerAugmentationHasteStatPerPercent(),
        EvokerAugmentationMasteryStatPerPercent(),
        EvokerAugmentationVersatilityStatPerPercent(),
    ]
