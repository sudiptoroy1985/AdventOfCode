import unittest
import FuelCalculator

class TestTotalFuel(unittest.TestCase) :

    def test_single_mass_Fuel_round(self):
        totalFuel = FuelCalculator.calculateFuel(14, 0)
        self.assertEqual(totalFuel, 2)

    def test_single_mass_4_digits_Fuel_round(self):
        totalFuel = FuelCalculator.calculateFuel(1969,0)
        self.assertEqual(totalFuel, 966)

    def test_single_mass_6_digits_Fuel_round(self):
        totalFuel = FuelCalculator.calculateFuel(100756,0)
        self.assertEqual(totalFuel, 50346)

if __name__ == '__main__':
    unittest.main()



