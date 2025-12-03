import unittest
import part2

class TestPart2(unittest.TestCase):
    def test_largest_joltage_1(self):
        self.assertEqual(part2.largest_joltage('987654321111111'), 987654321111)
        
    def test_largest_joltage_2(self):
        self.assertEqual(part2.largest_joltage('811111111111119'), 811111111119)

    def test_largest_joltage_3(self):
        self.assertEqual(part2.largest_joltage('234234234234278'), 434234234278)
        
    def test_largest_joltage_4(self):
        self.assertEqual(part2.largest_joltage('818181911112111'), 888911112111)

if __name__ == "__main__":
    unittest.main()
