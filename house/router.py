from home.views import *
from rest_framework import routers

router =routers.DefaultRouter()
router.register('houses', HouseViewSet)
router.register('rooms', RoomViewSet)
