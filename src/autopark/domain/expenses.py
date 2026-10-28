"""Витрати на експлуатацію транспортного засобу."""
from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class Expense:
    expense_id: str
    vehicle_id: str
    category: str
    amount_uah: Decimal
    incurred_on: date
    note: str = ""

    def __post_init__(self) -> None:
        if not self.expense_id.strip() or not self.vehicle_id.strip():
            raise ValueError("Ідентифікатори витрати й транспортного засобу обов'язкові")
        if not self.category.strip():
            raise ValueError("Категорія витрати обов'язкова")
        if self.amount_uah <= Decimal("0"):
            raise ValueError("Сума витрати має бути більшою за нуль")
