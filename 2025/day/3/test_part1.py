import unittest
import part1

class TestPart1(unittest.TestCase):
    def test_largest_joltage_1(self):
        self.assertEqual(part1.largest_joltage('987654321111111'), 98)
        
    def test_largest_joltage_2(self):
        self.assertEqual(part1.largest_joltage('811111111111119'), 89)

    def test_largest_joltage_3(self):
        self.assertEqual(part1.largest_joltage('234234234234278'), 78)
        
    def test_largest_joltage_4(self):
        self.assertEqual(part1.largest_joltage('818181911112111'), 92)

if __name__ == "__main__":
    unittest.main()
