import unittest
import part1

class TestPart1(unittest.TestCase):
    def test_next_invalid_id_1(self):
        self.assertEqual(part1.next_invalid_id(11), 11)
        self.assertEqual(part1.next_invalid_id(12), 22)
        self.assertEqual(part1.next_invalid_id(22), 22)
        self.assertEqual(part1.next_invalid_id(23), 33)

    def test_next_invalid_id_2(self):
        self.assertEqual(part1.next_invalid_id(95), 99)
        self.assertEqual(part1.next_invalid_id(99), 99)
        self.assertEqual(part1.next_invalid_id(100), 1010)

    def test_next_invalid_id_3(self):
        self.assertEqual(part1.next_invalid_id(998), 1010)
        self.assertEqual(part1.next_invalid_id(1010), 1010)
        self.assertEqual(part1.next_invalid_id(1011), 1111)

    def test_next_invalid_id_4(self):
        self.assertEqual(part1.next_invalid_id(1188511880), 1188511885)
        self.assertEqual(part1.next_invalid_id(1188511885), 1188511885)
        self.assertEqual(part1.next_invalid_id(1188511886), 1188611886)

    def test_next_invalid_id_5(self):
        self.assertEqual(part1.next_invalid_id(222220), 222222)
        self.assertEqual(part1.next_invalid_id(222222), 222222)
        self.assertEqual(part1.next_invalid_id(222223), 223223)

    def test_next_invalid_id_6(self):
        self.assertEqual(part1.next_invalid_id(1698522), 10001000)

    def test_next_invalid_id_7(self):
        self.assertEqual(part1.next_invalid_id(38593856), 38593859)
        self.assertEqual(part1.next_invalid_id(38593859), 38593859)
        self.assertEqual(part1.next_invalid_id(38593860), 38603860)

if __name__ == "__main__":
    unittest.main()
