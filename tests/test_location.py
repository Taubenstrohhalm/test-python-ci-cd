import unittest
from rehome.building import location

class TestLocation(unittest.TestCase):
    def test_conv_zip_to_latlong(self):
        self.assertEqual(location.conv_zip_to_latlong(79271), {'latitude':48.02,'longitude':8.04})

if __name__ == '__main__':
    unittest.main()