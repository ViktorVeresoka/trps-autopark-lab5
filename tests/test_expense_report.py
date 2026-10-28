"""Перевірки звіту про витрати."""
import sys
import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from autopark.application.use_cases import ExpenseReportService
from autopark.domain.expenses import Expense
from autopark.infrastructure.in_memory_expense_repository import InMemoryExpenseRepository


class ExpenseReportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = InMemoryExpenseRepository()
        self.service = ExpenseReportService(self.repository)
        self.repository.add(Expense("E-001", "V-001", "Пальне", Decimal("1200.50"), date(2026, 10, 3)))
        self.repository.add(Expense("E-002", "V-001", "Ремонт", Decimal("850.00"), date(2026, 10, 8)))
        self.repository.add(Expense("E-003", "V-002", "Пальне", Decimal("500.00"), date(2026, 11, 2)))

    def test_report_totals_by_category_and_date_range(self) -> None:
        report = self.service.create(date(2026, 10, 1), date(2026, 10, 31))
        self.assertEqual(report["count"], 2)
        self.assertEqual(report["total_uah"], Decimal("2050.50"))
        self.assertEqual(report["by_category"]["Пальне"], Decimal("1200.50"))
        self.assertEqual(report["by_category"]["Ремонт"], Decimal("850.00"))

    def test_reversed_period_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.service.create(date(2026, 11, 1), date(2026, 10, 1))

    def test_expense_amount_must_be_positive(self) -> None:
        with self.assertRaises(ValueError):
            Expense("E-004", "V-001", "Пальне", Decimal("0"), date(2026, 10, 3))


if __name__ == "__main__":
    unittest.main()
