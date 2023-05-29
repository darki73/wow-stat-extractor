from character.classes import \
    BaseClass, \
    DeathKnightClass, \
    DemonHunterClass, \
    DruidClass, \
    EvokerClass, \
    HunterClass, \
    MageClass, \
    MonkClass, \
    PaladinClass, \
    PriestClass, \
    RogueClass, \
    ShamanClass, \
    WarlockClass, \
    WarriorClass


# Class: Classes
class Classes:
    # Available classes list
    _classes_list: list[BaseClass] = [
        DeathKnightClass(),
        DemonHunterClass(),
        DruidClass(),
        EvokerClass(),
        HunterClass(),
        MageClass(),
        MonkClass(),
        PaladinClass(),
        PriestClass(),
        RogueClass(),
        ShamanClass(),
        WarlockClass(),
        WarriorClass(),
    ]

    _id_dict = {class_.get_id(): class_ for class_ in _classes_list}
    _name_dict = {class_.get_name(): class_ for class_ in _classes_list}
    _slug_dict = {class_.get_slug(): class_ for class_ in _classes_list}
    _enum_dict = {class_.get_enum(): class_ for class_ in _classes_list}

    # Returns class by id
    @staticmethod
    def get_class_by_id(class_id: int) -> BaseClass:
        if class_id in Classes._id_dict:
            return Classes._id_dict[class_id]
        raise Exception(f"Class with id {class_id} not found")

    # Returns class by name
    @staticmethod
    def get_class_by_name(class_name: str) -> BaseClass:
        if class_name in Classes._name_dict:
            return Classes._name_dict[class_name]
        raise Exception(f"Class with name {class_name} not found")

    # Returns class by slug
    @staticmethod
    def get_class_by_slug(class_slug: str) -> BaseClass:
        if class_slug in Classes._slug_dict:
            return Classes._slug_dict[class_slug]
        raise Exception(f"Class with slug {class_slug} not found")

    # Returns class by enum
    @staticmethod
    def get_class_by_enum(class_enum: str) -> BaseClass:
        if class_enum in Classes._enum_dict:
            return Classes._enum_dict[class_enum]
        raise Exception(f"Class with enum {class_enum} not found")

    # Returns class by id or name or slug or enum
    @staticmethod
    def get_class(search_term: str) -> BaseClass:
        try:
            return Classes.get_class_by_id(int(search_term))
        except ValueError:  # search_term is not int
            pass
        for method in (Classes.get_class_by_name, Classes.get_class_by_slug, Classes.get_class_by_enum):
            try:
                return method(search_term)
            except Exception:  # search_term is not found in dictionary
                pass
        raise Exception(f"Class with search term {search_term} not found")
