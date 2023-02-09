from home.views import HouseViewSet, RoomViewSet
from rest_framework import routers

router =routers.DefaultRouter()
router.register('houses', HouseViewSet)
router.register('rooms', RoomViewSet)
