from django.urls import path
from rest_framework import routers

from .views import RoomView, CreateRoomView,TodoViewSet

# router.register('<The URL prefix>', <The viewset class>, '<The URL name>')
router = routers.DefaultRouter()
router.register('todos', TodoViewSet, 'todos')

# urlpatterns = [
#     path('', RoomView.as_view()),
#     path('create-room', CreateRoomView.as_view())
# ]

urlpatterns = router.urls