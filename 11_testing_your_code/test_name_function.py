import unittest

from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Jobplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual('Janis Joplin', formatted_name)

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual("Wolfgang Amadeus Mozart", formatted_name)


if __name__ == '__main__':
    unittest.main()

