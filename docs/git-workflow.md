# ��������� Git-������

1. `main` ������ ������ ������ ��������� �� ����������� �������� ��������� ��.
2. `feature/maintenance-schedule` ���� ������������ ��� ��: �����������, ������� �����, ����������� (�� ����� 500 ��) ��� �� �� �������.
3. ��� ��������� �������, � `main` �� `feature/maintenance-schedule` ������ ������ ����� `Vehicle.maintenance_status`. ϳ� ��� ������ Git �������� ������ ������� ��������� ��������. ���� ������ ������� ���������� ������������� ������; ���������� ����������� merge-������.
4. `feature/expense-report` ������ ���� � �������� ������ �� ����������. ó��� ���������� ��� �������� pull request.

����� ������� ����������� `python -m unittest discover -s tests -v`. Workflow `.github/workflows/tests.yml` ������� ��� ����� ���� �������� ���� push � ��� pull request � GitHub Actions.
