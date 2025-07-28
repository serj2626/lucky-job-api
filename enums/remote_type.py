from enum import Enum

class RemoteType(str, Enum):
    remote = "remote"
    office = "office"
    hybrid = "hybrid"
