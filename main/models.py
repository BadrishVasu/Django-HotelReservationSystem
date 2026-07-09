from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Room(models.Model):
    ROOM_CATEGORIES = (
        ("Budget", "Budget"),
        ("Premium", "Premium"),
        ("Grand", "Grand"),
    )

    category = models.CharField(max_length=10, choices=ROOM_CATEGORIES)
    price = models.IntegerField()
    room_no = models.IntegerField(unique=True)

    def __str__(self):
        return f'Room #{self.room_no}, {self.category} room'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f'{self.room} From: {self.check_in.strftime("%d-%b-%Y")} To: {self.check_out.strftime("%d-%b-%Y")}'

    def get_room_category(self):
        room_categories = dict(self.room.ROOM_CATEGORIES)
        room_category = room_categories.get(self.room.category)
        return room_category

    def get_cancel_booking_url(self):
        return reverse_lazy('CancelBooking', args=[self.pk, ])

