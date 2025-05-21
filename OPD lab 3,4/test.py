import unittest
from app.routes import calc

class TestCalc(unittest.TestCase):
    def test_1(self): self.assertAlmostEqual(calc(1000, 1.1, 2), 1022.121)
    def test_2(self): self.assertAlmostEqual(calc(1000, 1.2, 3), 1036.433728)
    def test_3(self): self.assertAlmostEqual(calc(1000, 10.1, 8), 2159.22824079)
    def test_4(self): self.assertAlmostEqual(calc(1000, 1000, 3), 1331000)
    def test_5(self): self.assertAlmostEqual(calc(0.1, 1, 1000), 2095.91556378)
        
if __name__ == "__main__":
    unittest.main()