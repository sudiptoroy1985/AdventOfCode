import unittest
import FuelCalculator

class TestTotalFuel(unittest.TestCase) :
    
    def test_single_mass_Fuel(self):
        calculator = FuelCalculator.FuelCalculator([12])
        self.assertEqual(calculator.calculate(), 2)

    def test_single_mass_Fuel_round(self):
        calculator = FuelCalculator.FuelCalculator([14])
        self.assertEqual(calculator.calculate(), 2)

    def test_single_mass_Fuel_4_digit_number(self):
        calculator = FuelCalculator.FuelCalculator([1969])
        self.assertEqual(calculator.calculate(), 654)

    def test_single_mass_Fuel_5_digit_number(self):
        calculator = FuelCalculator.FuelCalculator([100756])
        self.assertEqual(calculator.calculate(), 33583)

    def test_multiple_mass_Fuel_Total(self):
        calculator = FuelCalculator.FuelCalculator([12,14,1969,100756])
        self.assertEqual(calculator.calculate(), 2+2+654+33583)
    
    

if __name__ == '__main__':
    unittest.main()



