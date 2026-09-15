from dataclasses import dataclass

@dataclass
class Airport:
    ID: int
    AIRPORT: str
    STATE: str
    n_voli: int

    def __str__(self):
        return f"{self.ID} - {self.STATE} - {self.AIRPORT} - {self.n_voli}"
    def __repr__(self):
        return f"{self.ID} - {self.STATE} - {self.AIRPORT} - {self.n_voli}"

    def __hash__(self):
        return hash(self.ID)
