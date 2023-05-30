# Converts the name to a slug
def name_to_slug(name: str) -> str:
    return name.lower().replace(" ", "-")


# Converts the name to an enum
def name_to_enum(name: str) -> str:
    return name.upper().replace(" ", "_")
