from enum import Enum

class UserRole(str, Enum):
    specialist = "specialist"
    company = "company"
    admin = "admin"