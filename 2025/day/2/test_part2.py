import unittest
import part2

class TestPart2(unittest.TestCase):
    def _test(self, low, high, invalid_ids):
        for id in range(low, high + 1):
            if id in invalid_ids:
                self.assertTrue(part2.is_invalid_id(id), id)
            else:
                self.assertFalse(part2.is_invalid_id(id), id)

    def test_is_invalid_id_1(self):
        self._test(11, 22, [11, 22])

    def test_is_invalid_id_2(self):
        self._test(95, 115, [99, 111])

    def test_is_invalid_id_3(self):
        self._test(998, 1012, [999, 1010])

    def test_is_invalid_id_4(self):
        self._test(222220, 222224, [222222])

    def test_is_invalid_id_5(self):
        self._test(1698522, 1698528, [])

    def test_is_invalid_id_6(self):
        self._test(446443, 446449, [446446])

    def test_is_invalid_id_7(self):
        self._test(38593856, 38593862, [38593859])

    def test_is_invalid_id_8(self):
        self._test(565653, 565659, [565656])

    def test_is_invalid_id_9(self):
        self._test(824824821, 824824827, [824824824])

    def test_is_invalid_id_10(self):
        self._test(2121212118, 2121212124, [2121212121])


if __name__ == "__main__":
    unittest.main()
