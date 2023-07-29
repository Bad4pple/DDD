from models import Room, Resident

def test_room_is_able_to_lease():

    room = Room(reference="STD-011", price=30000.0)
    person1 = Resident(reference="PER-111",firstname="Saharat", surname="Muksarn"),
    person2 = Resident(reference="PER-111",firstname="Voldermorth", surname="XXXXXXX")
    residents = [
        person1,
        person2
    ]

    room.lease(residents=residents)

    print(room.can_lease())


test_room_is_able_to_lease()