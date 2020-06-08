import unittest

from employee_report import get_adults, get_all_employees_sorted_by_name, capitalize_employee_names


class TestEmployeeReport(unittest.TestCase):
    given_employees = [
        {'name': 'Max', 'age': 17},
        {'name': 'Sepp', 'age': 18},
        {'name': 'Nina', 'age': 15},
        {'name': 'Mike', 'age': 51},
    ]

    def test_get_adults(self):
        expected_employees = [
            {'name': 'Sepp', 'age': 18},
            {'name': 'Mike', 'age': 51},
        ]

        actual_employees = get_adults(self.given_employees)
        self.assertEqual(expected_employees, actual_employees)

    def test_employees_sorted_by_name(self):
        expected_employees = [
            {'name': 'Sepp', 'age': 18},
            {'name': 'Nina', 'age': 15},
            {'name': 'Mike', 'age': 51},
            {'name': 'Max', 'age': 17},
        ]

        actual_employees = get_all_employees_sorted_by_name(self.given_employees)
        self.assertEqual(expected_employees, actual_employees)

    def test_employees_with_name_capitalized(self):
        given_employees = [
            {'name': 'foo', 'age': 17},
            {'name': 'bar', 'age': 51},
        ]

        expected_employees = [
            {'name': 'FOO', 'age': 17},
            {'name': 'BAR', 'age': 51},
        ]

        self.assertEqual(expected_employees, capitalize_employee_names(given_employees))
