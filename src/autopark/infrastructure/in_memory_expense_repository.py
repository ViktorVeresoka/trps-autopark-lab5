"""������� ����� ������ � ���'��."""
from datetime import date

from autopark.domain.expenses import Expense


class InMemoryExpenseRepository:
    def __init__(self) -> None:
        self._expenses: list[Expense] = []

    def add(self, expense: Expense) -> None:
        if any(current.expense_id == expense.expense_id for current in self._expenses):
            raise ValueError(f"������� {expense.expense_id} ��� ������������")
        self._expenses.append(expense)

    def list_for_period(self, start: date, end: date) -> list[Expense]:
        return [expense for expense in self._expenses if start <= expense.incurred_on <= end]
