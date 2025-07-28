from enum import Enum

class JobType(str, Enum):
    full_time = "full_time"
    part_time = "part_time"
    freelance = "freelance"
    internship = "internship"
    contract = "contract"