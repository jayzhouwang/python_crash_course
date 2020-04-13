import unittest
    
from city_functions import format

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_string = format('santiago', 'chile')
        self.assertEqual(formatted_string, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()
