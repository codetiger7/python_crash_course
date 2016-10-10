from city_functions import city_country
import unittest


class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        result = city_country("oslo", "norway")

        self.assertEqual("Oslo, Norway", result)

        result2 = city_country("santiago", "chile")
        self.assertEqual("Santiago, Chile", result2)

    def test_city_country_population(self):
        result = city_country("santiago", "chile", "population=5000000")

