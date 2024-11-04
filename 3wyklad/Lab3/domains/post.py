from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Post:
    event_time: datetime
    userId: int
    id: int
    title: str
    body: str

    def dict(self):
        result = {}
        for key, value in asdict(self).items():
            result[key] = str(value)
        return result
