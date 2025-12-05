import unittest
import part2

class TestPart2(unittest.TestCase):
    def test_is_not_overlap(self):
        self.assertFalse(part2.is_overlap((3, 6), (1, 2)))
        self.assertFalse(part2.is_overlap((3, 6), (7, 8)))

    def test_is_overlap(self):
        self.assertTrue(part2.is_overlap((3, 6), (1, 3)))
        self.assertTrue(part2.is_overlap((3, 6), (1, 4)))

        self.assertTrue(part2.is_overlap((3, 6), (6, 7)))
        self.assertTrue(part2.is_overlap((3, 6), (5, 7)))

        self.assertTrue(part2.is_overlap((3, 6), (2, 7)))
        self.assertTrue(part2.is_overlap((3, 6), (4, 5)))
        self.assertTrue(part2.is_overlap((3, 6), (3, 6)))

    def test_merge_ranges1(self):
        merged = part2.merge_ranges([], (3, 5))
        self.assertEqual(merged, [(3, 5)])

        merged = part2.merge_ranges([(3, 5)], (10, 14))
        self.assertEqual(sorted(merged), [(3, 5), (10, 14)])

    def test_merge_ranges2(self):
        merged = part2.merge_ranges([(10, 14)], (12, 18))
        self.assertEqual(merged, [(10, 18)])

    def test_merge_ranges3(self):
        merged = part2.merge_ranges([(10, 14), (16, 20)], (12, 18))
        self.assertEqual(merged, [(10, 20)])


if __name__ == "__main__":
    unittest.main()
