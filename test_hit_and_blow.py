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

    def test_answer(self):
        game = HitAndBlow(4, 1234)

        self.assertEqual("[1]0H4B", game.answer("4321"))
        self.assertEqual(False, game.is_over)

        self.assertEqual("[2]1H1B", game.answer("1389"))
        self.assertEqual(False, game.is_over)

        self.assertEqual("[3]4H0B", game.answer("1234"))
        self.assertEqual(True, game.is_over)

        with self.assertRaises(HitAndBlow.LengthError):
            HitAndBlow(4, 12345)

        with self.assertRaises(HitAndBlow.DuplicationError):
            HitAndBlow(4, 1233)
