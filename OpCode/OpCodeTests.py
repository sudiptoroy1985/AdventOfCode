import unittest
import OpCode

class TestOpCode(unittest.TestCase) :

    def test_add_opCode_generation(self):
        final = OpCode.finalState([1,0,0,0,99])
        self.assertEqual(final, [2,0,0,0,99])

    def test_product_opCode_generation(self):
        final = OpCode.finalState([2,3,0,3,99])
        self.assertEqual(final, [2,3,0,6,99])
    
    def test_product_opCode_6_digits(self):
        final = OpCode.finalState([2,4,4,5,99,0])
        self.assertEqual(final, [2,4,4,5,99,9801])

    def test_product_opCode_with_Halt(self):
        final = OpCode.finalState([1,1,1,4,99,5,6,0,99])
        self.assertEqual(final, [30,1,1,4,2,5,6,0,99])


if __name__ == '__main__':
    unittest.main()

