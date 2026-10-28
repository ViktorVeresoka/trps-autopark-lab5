"""������� ���������� ��� ��������� ������������ �� �����."""
from autopark.domain.entities import Vehicle


class InMemoryVehicleRepository:
    def __init__(self) -> None:
        self._vehicles: dict[str, Vehicle] = {}

    def add(self, vehicle: Vehicle) -> None:
        if vehicle.vehicle_id in self._vehicles:
            raise ValueError(f"������������ ���� {vehicle.vehicle_id} ��� ����")
        self._vehicles[vehicle.vehicle_id] = vehicle

    def get(self, vehicle_id: str) -> Vehicle:
        try:
            return self._vehicles[vehicle_id]
        except KeyError as exc:
            raise KeyError(f"������������ ���� {vehicle_id} �� ��������") from exc

    def list_all(self) -> list[Vehicle]:
        return list(self._vehicles.values())

    def save(self, vehicle: Vehicle) -> None:
        if vehicle.vehicle_id not in self._vehicles:
            raise KeyError(f"������������ ���� {vehicle.vehicle_id} �� ������������")
        self._vehicles[vehicle.vehicle_id] = vehicle
