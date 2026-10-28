"""������� ������ ������������� ������."""
from dataclasses import dataclass


@dataclass
class Vehicle:
    """������������ ���� �� �������� ������ �� ���������� ��."""

    vehicle_id: str
    registration_number: str
    make: str
    model: str
    mileage_km: int
    next_service_km: int

    def __post_init__(self) -> None:
        if not self.vehicle_id.strip() or not self.registration_number.strip():
            raise ValueError("������������� �� ��������� ����� ����'�����")
        if self.mileage_km < 0 or self.next_service_km < 0:
            raise ValueError("����� �� ���� ���� ��'�����")

    def add_trip_mileage(self, distance_km: int) -> None:
        if distance_km <= 0:
            raise ValueError("������� ����� �� ���� ������ �� ����")
        self.mileage_km += distance_km

    def maintenance_status(self) -> str:
        """������ ���������� ��������� �������������� �� �������."""
        remaining_km = self.next_service_km - self.mileage_km
        if remaining_km < 0:
            return "�� �����������"
        if remaining_km == 0:
            return "�� ������� �����"
        if remaining_km <= 500:
            return "�� �����������"
        return "�� �� �������"
