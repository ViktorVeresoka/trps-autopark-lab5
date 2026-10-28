"""Перевірки доменної моделі та сценаріїв автопарку."""
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


if __name__ == "__main__":
    unittest.main()
