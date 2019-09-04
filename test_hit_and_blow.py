import unittest
from hit_and_blow import count_duplicates, has_duplicate, HitAndBlow


class TestDefDuplicates(unittest.TestCase):
    def test_count_duplicates(self):
        expected = 1
        actual = count_duplicates([1, 2, 3, 1, 1])
        self.assertEqual(expected, actual)

    def test_has_duplicates(self):
        expected = True
        actual = has_duplicate([1, 2, 3, 1])
        self.assertEqual(expected, actual)


class TestHitAndBlow(unittest.TestCase):
    def test_score(self):
        self.game = HitAndBlow(1234)
        expect = "1H1B"
        actual = self.game.score(1389)
        self.assertEqual(expect, actual)

    def test_answer(self):
        self.game = HitAndBlow(1234)
        expect = "0H4B"
        actual = self.game.answer("4321")
        self.assertEqual(expect, actual)
