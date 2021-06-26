from django.test import TestCase
from home.models import House, Room


class HouseTestCase(TestCase):

    def setUp(self):
        House.objects.create(number=1, address='test address')
        
    def test_create_house(self):
        self.assertEqual(House.objects.all().count(), 1)

    def test_update_house(self):
        new_number = 2
        House.objects.filter(id=1).update(number=new_number)
        updated_house = House.objects.all().get(id=1)
        self.assertEqual(updated_house.number, new_number)

    def test_delete_house(self):
        House.objects.filter(id=1).delete()
        self.assertEqual(House.objects.all().count(), 0)


class RoomTestCase(TestCase):
    def setUp(self):
        house=House.objects.create(number=1, address='test address')
        Room.objects.create(number=100, house=house, room_type='bed-room')

    def test_create_room(self):
        self.assertEqual(Room.objects.all().count(), 1)

    def test_update_room(self):
        new_type = 'living-room'
        Room.objects.filter(id=1).update(room_type=new_type)
        updated_Room = Room.objects.all().get(id=1)
        self.assertEqual(updated_Room.room_type, new_type)

    def test_delete_room(self):
        Room.objects.filter(id=1).delete()
        self.assertEqual(Room.objects.all().count(), 0)
