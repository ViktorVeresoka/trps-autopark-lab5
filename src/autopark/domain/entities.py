"""Доменна модель транспортного засобу."""
from dataclasses import dataclass


@dataclass
class Vehicle:
    """Транспортний засіб та контроль пробігу до наступного ТО."""

    vehicle_id: str
    registration_number: str
    make: str
    model: str
    mileage_km: int
    next_service_km: int

    def __post_init__(self) -> None:
        if not self.vehicle_id.strip() or not self.registration_number.strip():
            raise ValueError("Ідентифікатор та державний номер обов'язкові")
        if self.mileage_km < 0 or self.next_service_km < 0:
            raise ValueError("Пробіг не може бути від'ємним")

    def add_trip_mileage(self, distance_km: int) -> None:
        if distance_km <= 0:
            raise ValueError("Довжина рейсу має бути більшою за нуль")
        self.mileage_km += distance_km

    def maintenance_status(self) -> str:
        """Оцінює наближення планового обслуговування за пробігом."""
        remaining_km = self.next_service_km - self.mileage_km
        if remaining_km < 0:
            return "ТО прострочене"
        if remaining_km == 0:
            return "ТО потрібно зараз"
        if remaining_km <= 500:
            return "ТО наближається"
        return "ТО не потрібне"
