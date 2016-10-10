from employee import Employee
import unittest


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Anne", "Berkley", 100000)

    def test_give_default_raise(self):
        new_salary = self.employee.give_raise()
        self.assertEqual(105000, new_salary)

    def test_give_custom_raise(self):
        new_salary = self.employee.give_raise(100000)
        self.assertEqual(200000, new_salary)


if __name__ == "__main___":
    unittest.main()
