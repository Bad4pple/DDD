from typing import List


class Resident:
    def __init__(self, reference: str, firstname: str, surname: str) -> None:
        self.reference = reference
        self.fistname = firstname
        self.surname = surname
    
    def __str__(self) -> str:
        return f"Resident({self.fistname}, {self.surname})"


class Room:
    def __init__(self, reference: str, price: float) -> None:
        self.reference = reference
        self.price = price
        self.residents = set() # คนเช่า
    
    def can_lease(self):
        print(len(self.residents))
        return len(self.residents) == 0
    
    def lease(self, residents: List[Resident]):
        for person in residents:
            self.residents.add(person)


# {
#     "reference": "pre-110",
#     "price": 1200,
#     "residents": [
#         {
#             "reference": "cus-222",
#             "firstname": "Saharat"
#         }
#     ]
# }