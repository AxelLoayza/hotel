from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Habitacion, Cliente, Reserva, Reseña
from .serializers import HabitacionSerializer, ClienteSerializer, ReservaSerializer, ReseñaSerializer

class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

@api_view(['GET'])
def verificar_disponibilidad(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    habitaciones_disponibles = Habitacion.objects.filter(disponible=True)
    serializer = HabitacionSerializer(habitaciones_disponibles, many=True)
    return Response(serializer.data)
