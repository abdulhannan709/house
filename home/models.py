from django.db import models

class House(models.Model):
    number = models.IntegerField()
    address = models.TextField(max_length=50)

    def __str__(self):
        return f"{self.number}-{self.address}"


class Room(models.Model):

    BEDROOM = 'bed-room'
    LIVING_ROOM = 'living-room'
    STORE_ROOM =  'store-room'
    BATH_ROOM =  'bath-room'
    ROOM_TYPES = [
        (BEDROOM, 'Bedroom'),
        (LIVING_ROOM, 'Living Room'),
        (STORE_ROOM, 'Store Room'),
        (BATH_ROOM, 'Bath Room'),
    ]

    number = models.IntegerField()
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="rooms", null=True)
    room_type = models.CharField(
        max_length=20,
        choices=ROOM_TYPES,
        default=BEDROOM,
    )

    def __str__(self):
        return f"{self.house} - {self.room_type}"
