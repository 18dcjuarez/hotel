"""HotelManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework.routers import DefaultRouter

from Hotel.views import HotelViewSet
from Services.views import ServicesViewSet
from Guest.views import GuestViewSet
from Room.views import RoomViewSet
from balance.views import BalanceViewSet
from reservations.views import ReservationViewSet
from service_account.views import ServiceAccountViewSet

router = DefaultRouter()
router.register(r'hotel', HotelViewSet, base_name='hotel')
router.register(r'services', ServicesViewSet, base_name='services')
router.register(r'guest', GuestViewSet, base_name='guest')
router.register(r'room', RoomViewSet, base_name='room')
router.register(r'balance', BalanceViewSet, base_name='balance')
router.register(r'reservation', ReservationViewSet, base_name='reservation')
router.register(r'service_account', ServiceAccountViewSet, base_name='service_account')
urlpatterns = router.urls
