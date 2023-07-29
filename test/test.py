from models import Room

def test_room_is_able_to_lease():

    room = Room(reference="STD-011", price=30000.0)
    # resident = Resident(reference="PER-111",firstname="Saharat", surname="Muksarn")

    assert room.can_lease() == False

    # room.lease(resident=resident)


test_room_is_able_to_lease()