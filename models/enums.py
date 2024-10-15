import enum


class RoleType(enum.Enum):
    admin = "admin"
    user = "user"
    moderator = "moderator"


class Category(enum.Enum):
    paintings = "Paintings"
    web_design = "Web design"
    photography = "Photography"
