"""Сценарії для роботи автопарку."""
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
"""Формування звіту про витрати за період."""
from datetime import date
from decimal import Decimal

from autopark.application.ports import ExpenseRepository
from autopark.domain.expenses import Expense


class ExpenseReportService:
    def __init__(self, expenses: ExpenseRepository) -> None:
        self._expenses = expenses

    def create(self, start: date, end: date) -> dict[str, object]:
        if end < start:
            raise ValueError("Кінець періоду не може передувати початку")
        rows = self._expenses.list_for_period(start, end)
        by_category: dict[str, Decimal] = {}
        for expense in rows:
            by_category[expense.category] = by_category.get(expense.category, Decimal("0")) + expense.amount_uah
        return {
            "start": start,
            "end": end,
            "count": len(rows),
            "total_uah": sum(by_category.values(), Decimal("0")),
            "by_category": by_category,
        }
