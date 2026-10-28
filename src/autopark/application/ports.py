"""Порт збереження транспортних засобів."""
from typing import Protocol

from autopark.domain.entities import Vehicle


class VehicleRepository(Protocol):
    def add(self, vehicle: Vehicle) -> None: ...

    def get(self, vehicle_id: str) -> Vehicle: ...

    def list_all(self) -> list[Vehicle]: ...

    def save(self, vehicle: Vehicle) -> None: ...
