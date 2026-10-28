"""������ ��� ������ ���������."""
from autopark.application.ports import VehicleRepository
from autopark.domain.entities import Vehicle


class FleetService:
    def __init__(self, vehicles: VehicleRepository) -> None:
        self._vehicles = vehicles

    def register_vehicle(self, vehicle: Vehicle) -> None:
        self._vehicles.add(vehicle)

    def record_trip_mileage(self, vehicle_id: str, distance_km: int) -> Vehicle:
        vehicle = self._vehicles.get(vehicle_id)
        vehicle.add_trip_mileage(distance_km)
        self._vehicles.save(vehicle)
        return vehicle

    def list_vehicles(self) -> list[Vehicle]:
        return self._vehicles.list_all()
