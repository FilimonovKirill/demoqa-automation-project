from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    current_address: str
    full_name: str = field(init=False)
    permanent_address: Optional[str] = None
    gender: Optional[str] = None
    mobile_number: Optional[str] = None
    birth_date: Optional[str] = None
    hobbies: Optional[List[str]] = field(default_factory=list)

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"
        if self.permanent_address is None:
            self.permanent_address = self.current_address
