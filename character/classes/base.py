import json


# Class: SpecializationStatBonus
class SpecializationStatBonus:
    # Stat name
    name: str
    # Stat slug
    slug: str
    # Stat enum
    enum: str
    # Bonus value
    value: float

    # Returns the stat name
    def get_name(self) -> str:
        return self.name

    # Returns the stat slug
    def get_slug(self) -> str:
        return self.slug

    # Returns the stat enum
    def get_enum(self) -> str:
        return self.enum

    # Returns the bonus value
    def get_value(self) -> float:
        return self.value

    # Converts class to dict
    def to_dict(self) -> dict:
        return {
            "name": self.get_name(),
            "slug": self.get_slug(),
            "enum": self.get_enum(),
            "value": self.get_value(),
        }

    # Converts class to json
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)


# Class: BaseCriticalStrikeStatBonus
class BaseCriticalStrikeStatBonus(SpecializationStatBonus):
    # Stat name
    name: str = "Critical Strike"
    # Stat slug
    slug: str = "critical_strike"
    # Stat enum
    enum: str = "CRIT_RATING"


# Class: BaseHasteStatBonus
class BaseHasteStatBonus(SpecializationStatBonus):
    # Stat name
    name: str = "Haste"
    # Stat slug
    slug: str = "haste"
    # Stat enum
    enum: str = "HASTE_RATING"


# Class: BaseMasteryStatBonus
class BaseMasteryStatBonus(SpecializationStatBonus):
    # Stat name
    name: str = "Mastery"
    # Stat slug
    slug: str = "mastery"
    # Stat enum
    enum: str = "MASTERY_RATING"


# Class: BaseVersatilityStatBonus
class BaseVersatilityStatBonus(SpecializationStatBonus):
    # Stat name
    name: str = "Versatility"
    # Stat slug
    slug: str = "versatility"
    # Stat enum
    enum: str = "VERSATILITY"


# Class: BaseStatPerPercent
class BaseStatPerPercent:
    # Stat name
    name: str
    # Stat slug
    slug: str
    # Stat enum
    enum: str
    # Stat value per percent
    value_per_percent: float

    # Returns the stat name
    def get_name(self) -> str:
        return self.name

    # Returns the stat slug
    def get_slug(self) -> str:
        return self.slug

    # Returns the stat enum
    def get_enum(self) -> str:
        return self.enum

    # Returns the stat value per percent
    def get_value_per_percent(self) -> float:
        return self.value_per_percent

    # Converts class to dict
    def to_dict(self) -> dict:
        return {
            "name": self.get_name(),
            "slug": self.get_slug(),
            "enum": self.get_enum(),
            "value_per_percent": self.get_value_per_percent(),
        }

    # Converts class to json
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)


# Class: BaseCriticalStrikeStatPerPercent
class BaseCriticalStrikeStatPerPercent(BaseStatPerPercent):
    # Stat name
    name: str = "Critical Strike"
    # Stat slug
    slug: str = "critical_strike"
    # Stat enum
    enum: str = "CRIT_RATING"


# Class: BaseHasteStatPerPercent
class BaseHasteStatPerPercent(BaseStatPerPercent):
    # Stat name
    name: str = "Haste"
    # Stat slug
    slug: str = "haste"
    # Stat enum
    enum: str = "HASTE_RATING"


# Class: BaseMasteryStatPerPercent
class BaseMasteryStatPerPercent(BaseStatPerPercent):
    # Stat name
    name: str = "Mastery"
    # Stat slug
    slug: str = "mastery"
    # Stat enum
    enum: str = "MASTERY_RATING"


# Class: BaseVersatilityStatPerPercent
class BaseVersatilityStatPerPercent(BaseStatPerPercent):
    # Stat name
    name: str = "Versatility"
    # Stat slug
    slug: str = "versatility"
    # Stat enum
    enum: str = "VERSATILITY"


# Class: BaseSpecialization
class BaseSpecialization:
    # Specialization identifier
    id: int
    # Specialization name
    name: str
    # Specialization slug
    slug: str
    # Specialization enum
    enum: str
    # Specialization stat bonuses
    stat_bonuses: list[SpecializationStatBonus]
    # Class stat per percent
    stat_per_percent: list[BaseStatPerPercent]

    # Returns the specialization identifier
    def get_id(self) -> int:
        return self.id

    # Returns the specialization name
    def get_name(self) -> str:
        return self.name

    # Returns the specialization slug
    def get_slug(self) -> str:
        return self.slug

    # Returns the specialization enum
    def get_enum(self) -> str:
        return self.enum

    # Returns the specialization stat bonuses
    def get_stat_bonuses(self) -> list[SpecializationStatBonus]:
        return self.stat_bonuses

    # Returns the specialization stat per percent
    def get_stat_per_percent(self) -> list[BaseStatPerPercent]:
        return self.stat_per_percent

    # Returns true if the specialization has stat bonus by name
    def has_stat_bonus_by_name(self, name: str) -> bool:
        for stat_bonus in self.get_stat_bonuses():
            if stat_bonus.get_name() == name:
                return True
        return False

    # Returns the specialization stat bonus by name
    def get_stat_bonus_by_name(self, name: str) -> SpecializationStatBonus:
        for stat_bonus in self.get_stat_bonuses():
            if stat_bonus.get_name() == name:
                return stat_bonus
        raise Exception(f"Stat bonus with name '{name}' not found.")

    # Returns true if the specialization has stat bonus by slug
    def has_stat_bonus_by_slug(self, slug: str) -> bool:
        for stat_bonus in self.get_stat_bonuses():
            if stat_bonus.get_slug() == slug:
                return True
        return False

    # Returns the specialization stat bonus by slug
    def get_stat_bonus_by_slug(self, slug: str) -> SpecializationStatBonus:
        for stat_bonus in self.get_stat_bonuses():
            if stat_bonus.get_slug() == slug:
                return stat_bonus
        raise Exception(f"Stat bonus with slug '{slug}' not found.")

    # Returns true if the specialization has stat bonus by enum
    def has_stat_bonus_by_enum(self, enum: str) -> bool:
        for stat_bonus in self.get_stat_bonuses():
            if stat_bonus.get_enum() == enum:
                return True
        return False

    # Returns the specialization stat bonus by enum
    def get_stat_bonus_by_enum(self, enum: str) -> SpecializationStatBonus:
        for stat_bonus in self.get_stat_bonuses():
            if stat_bonus.get_enum() == enum:
                return stat_bonus
        raise Exception(f"Stat bonus with enum '{enum}' not found.")

    # Returns the specialization stat per percent by name
    def get_stat_per_percent_by_name(self, name: str) -> BaseStatPerPercent:
        for stat_per_percent in self.get_stat_per_percent():
            if stat_per_percent.get_name() == name:
                return stat_per_percent
        raise Exception(f"Stat per percent with name '{name}' not found.")

    # Returns the specialization stat per percent by slug
    def get_stat_per_percent_by_slug(self, slug: str) -> BaseStatPerPercent:
        for stat_per_percent in self.get_stat_per_percent():
            if stat_per_percent.get_slug() == slug:
                return stat_per_percent
        raise Exception(f"Stat per percent with slug '{slug}' not found.")

    # Returns the specialization stat per percent by enum
    def get_stat_per_percent_by_enum(self, enum: str) -> BaseStatPerPercent:
        for stat_per_percent in self.get_stat_per_percent():
            if stat_per_percent.get_enum() == enum:
                return stat_per_percent
        raise Exception(f"Stat per percent with enum '{enum}' not found.")

    # Converts class to dict
    def to_dict(self) -> dict:
        return {
            "name": self.get_name(),
            "slug": self.get_slug(),
            "enum": self.get_enum(),
            "stat_bonuses": [stat_bonus.to_dict() for stat_bonus in self.get_stat_bonuses()],
            "stat_per_percent": [stat_per_percent.to_dict() for stat_per_percent in self.get_stat_per_percent()],
        }

    # Converts class to json
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)


# Class: BaseClass
class BaseClass:
    # Class identifier
    id: int
    # Class name
    name: str
    # Class slug
    slug: str
    # Class enum
    enum: str
    # Class specializations
    specializations: list[BaseSpecialization]

    # Class constructor
    def __init__(self):
        self._specialization_id_dict = {spec.get_id(): spec for spec in self.specializations}
        self._specialization_slug_dict = {spec.get_slug(): spec for spec in self.specializations}
        self._specialization_enum_dict = {spec.get_enum(): spec for spec in self.specializations}
        self._specialization_name_dict = {spec.get_name(): spec for spec in self.specializations}

    # Returns the class identifier
    def get_id(self) -> int:
        return self.id

    # Returns the class name
    def get_name(self) -> str:
        return self.name

    # Returns the class slug
    def get_slug(self) -> str:
        return self.slug

    # Returns the class enum
    def get_enum(self) -> str:
        return self.enum

    # Returns the class specializations
    def get_specializations(self) -> list[BaseSpecialization]:
        return self.specializations

    # Returns whether the class has specializations
    def has_specializations(self) -> bool:
        return len(self.get_specializations()) > 0

    # Returns the class specialization by id
    def get_specialization_by_id(self, id: int) -> BaseSpecialization:
        if id in self._specialization_id_dict:
            return self._specialization_id_dict[id]
        raise Exception(f"Specialization with id {id} not found")

    # Returns the class specialization by slug
    def get_specialization_by_slug(self, slug: str) -> BaseSpecialization:
        if slug in self._specialization_slug_dict:
            return self._specialization_slug_dict[slug]
        raise Exception(f"Specialization with slug {slug} not found")

    # Returns the class specialization by enum
    def get_specialization_by_enum(self, enum: str) -> BaseSpecialization:
        if enum in self._specialization_enum_dict:
            return self._specialization_enum_dict[enum]
        raise Exception(f"Specialization with enum {enum} not found")

    # Returns the class specialization by name
    def get_specialization_by_name(self, name: str) -> BaseSpecialization:
        if name in self._specialization_name_dict:
            return self._specialization_name_dict[name]
        raise Exception(f"Specialization with name {name} not found")

    # Returns the class specialization by id or slug or enum or name
    def get_specialization(self, search_term: str) -> BaseSpecialization:
        try:
            return self.get_specialization_by_id(int(search_term))
        except ValueError:
            pass
        if search_term in self._specialization_slug_dict:
            return self.get_specialization_by_slug(search_term)
        if search_term in self._specialization_enum_dict:
            return self.get_specialization_by_enum(search_term)
        if search_term in self._specialization_name_dict:
            return self.get_specialization_by_name(search_term)
        raise Exception(f"Specialization with search term {search_term} not found")

    # Returns true if class specialization exists by id or slug or enum or name
    def has_specialization(self, search_term: str) -> bool:
        try:
            self.get_specialization_by_id(int(search_term))
            return True
        except ValueError:
            pass
        if search_term in self._specialization_slug_dict:
            return True
        if search_term in self._specialization_enum_dict:
            return True
        if search_term in self._specialization_name_dict:
            return True
        return False

    # Converts class to dict
    def to_dict(self) -> dict:
        return {
            "name": self.get_name(),
            "slug": self.get_slug(),
            "enum": self.get_enum(),
            "specializations": [specialization.to_dict() for specialization in self.get_specializations()],
        }

    # Converts class to json
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
