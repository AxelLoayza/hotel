from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HabitacionViewSet, ReservaViewSet, verificar_disponibilidad

router = DefaultRouter()
router.register(r'habitaciones', HabitacionViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('verificar_disponibilidad/', verificar_disponibilidad),
]
