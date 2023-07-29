import models
from typing import List
import abc

class RoomRepository(abc.ABC):

    @abc.abstractmethod
    def get(self, reference: str) -> models.Room:
        raise NotImplementedError
    
    def save(self, room: models.Room):
        raise NotImplementedError

room1 = models.Room(reference="PRE-101", price=30000)
person1 = models.Resident(reference="CUS-222",firstname="Saharat", surname="Muksarn")
room1.lease(residents=[person1])
room2 = models.Room(reference="PRE-102", price=30000)

class RoomRepositoryMemory(RoomRepository):


    def __init__(self) -> None:
        self._databases: List[models.Room] = [
            room1,
            room2,
        ]

    def get(self, reference: str) -> models.Room:
        for item in self._databases:
            if item.reference == reference:
                return item
    
    def save(self, room: models.Room):
        self._databases.append(room)
    
class RoomRepositorySQL(RoomRepository):
    def get(self, reference: str) -> models.Room:
        pass
    
    def save(self, room: models.Room):
        pass

# class RoomRepositoryMongo(RoomRepository):
#     def get(self, reference: str) -> models.Room:
#         return db.query(models.User).filter(models.User.email == email).first()
    
#     def save(self, room: models.Room):
#         return db.query(models.User).filter(models.User.email == email).first()