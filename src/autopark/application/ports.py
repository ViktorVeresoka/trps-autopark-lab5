"""Порт збереження транспортних засобів."""
from typing import Protocol

from autopark.domain.entities import Vehicle


class VehicleRepository(Protocol):
    def add(self, vehicle: Vehicle) -> None: ...

    def get(self, vehicle_id: str) -> Vehicle: ...

    def list_all(self) -> list[Vehicle]: ...

    def save(self, vehicle: Vehicle) -> None: ...
"""Порт обліку витрат автопарку."""
from datetime import date
from typing import Protocol

from autopark.domain.expenses import Expense


class ExpenseRepository(Protocol):
    def add(self, expense: Expense) -> None: ...

    def list_for_period(self, start: date, end: date) -> list[Expense]: ...
