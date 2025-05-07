from django.core.management.base import BaseCommand
from reservas.models import Habitacion, Cliente, Reserva
from datetime import date

class Command(BaseCommand):
    help = "Crea datos iniciales para la aplicación de reservas"

    def handle(self, *args, **kwargs):
        # Crear habitaciones
        Habitacion.objects.bulk_create([
            Habitacion(numero="101", tipo="Individual", precio=50.00, disponible=True),
            Habitacion(numero="102", tipo="Doble", precio=80.00, disponible=True),
            Habitacion(numero="103", tipo="Suite", precio=150.00, disponible=True),
        ])
        self.stdout.write(self.style.SUCCESS("✅ Habitaciones creadas"))

        # Crear clientes
        Cliente.objects.bulk_create([
            Cliente(nombre="Axel Pérez", email="axel@example.com"),
            Cliente(nombre="María López", email="maria@example.com"),
        ])
        self.stdout.write(self.style.SUCCESS("✅ Clientes creados"))

        # Crear reservas
        Reserva.objects.bulk_create([
            Reserva(habitacion=Habitacion.objects.get(numero="101"), cliente=Cliente.objects.get(email="axel@example.com"), fecha_inicio=date(2025, 5, 10), fecha_fin=date(2025, 5, 15), estado="confirmada"),
            Reserva(habitacion=Habitacion.objects.get(numero="102"), cliente=Cliente.objects.get(email="maria@example.com"), fecha_inicio=date(2025, 6, 1), fecha_fin=date(2025, 6, 5), estado="pendiente"),
        ])
        self.stdout.write(self.style.SUCCESS("✅ Reservas creadas"))
