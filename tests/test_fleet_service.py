"""�������� ������� ����� �� ������� ���������."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from autopark.application.use_cases import FleetService
from autopark.domain.entities import Vehicle
from autopark.infrastructure.in_memory_vehicle_repository import InMemoryVehicleRepository


class FleetServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = InMemoryVehicleRepository()
        self.service = FleetService(self.repository)
        self.vehicle = Vehicle("V-001", "AA1234BC", "MAN", "TGL", 120000, 125000)
        self.service.register_vehicle(self.vehicle)

    def test_trip_updates_vehicle_mileage(self) -> None:
        updated = self.service.record_trip_mileage("V-001", 180)
        self.assertEqual(updated.mileage_km, 120180)
        self.assertEqual(self.service.list_vehicles(), [updated])

    def test_trip_distance_must_be_positive(self) -> None:
        with self.assertRaises(ValueError):
            self.service.record_trip_mileage("V-001", 0)
        self.assertEqual(self.repository.get("V-001").mileage_km, 120000)

    def test_duplicate_vehicle_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.service.register_vehicle(self.vehicle)

    def test_unknown_vehicle_is_reported(self) -> None:
        with self.assertRaises(KeyError):
            self.service.record_trip_mileage("missing", 50)

    def test_maintenance_is_overdue_after_threshold(self) -> None:
        vehicle = Vehicle("V-002", "AA1235BC", "MAN", "TGL", 125001, 125000)
        self.assertEqual(vehicle.maintenance_status(), "�� �����������")

    def test_maintenance_is_due_at_threshold(self) -> None:
        vehicle = Vehicle("V-003", "AA1236BC", "MAN", "TGL", 125000, 125000)
        self.assertEqual(vehicle.maintenance_status(), "�� ������� �����")

    def test_maintenance_warning_starts_within_500_km(self) -> None:
        vehicle = Vehicle("V-004", "AA1237BC", "MAN", "TGL", 124500, 125000)
        self.assertEqual(vehicle.maintenance_status(), "�� �����������")

    def test_maintenance_is_not_due_beyond_warning_range(self) -> None:
        vehicle = Vehicle("V-005", "AA1238BC", "MAN", "TGL", 124000, 125000)
        self.assertEqual(vehicle.maintenance_status(), "�� �� �������")


if __name__ == "__main__":
    unittest.main()
