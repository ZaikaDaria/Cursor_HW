import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee1 = Employee('Daria', 'Zaika', 21000)
        self.employee2 = Employee('Ivan', 'Ivanov', 17000)

    def test_email(self):
        self.assertEqual(self.employee1.email, 'Daria.Zaika@email.com')
        self.assertEqual(self.employee2.email, 'Ivan.Ivanov@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee1.fullname, f'{self.employee1.first} {self.employee1.last}')
        self.assertEqual(self.employee2.fullname, f'{self.employee2.first} {self.employee2.last}')

    def test_apply_raise(self):
        self.employee1.apply_raise()
        self.employee2.apply_raise()

        self.assertEqual(self.employee1.pay, 22050)
        self.assertEqual(self.employee2.pay, 17850)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.text = 'Success'

            schedule = self.employee1.monthly_schedule('June')
            mock_get.assert_called_with("http://company.com/Zaika/June")
            self.assertEqual(schedule, 'Success')


if __name__ == '__main__':
    unittest.main()