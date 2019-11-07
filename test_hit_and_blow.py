import unittest
from hit_and_blow import count_duplicates, HitAndBlow


class TestDefDuplicates(unittest.TestCase):
    def test_count_duplicates(self):
        expected = 1
        actual = count_duplicates([1, 2, 3, 1, 1])
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
        with self.assertRaises(ValueError):
            HitAndBlow(min_=1, max_=1)
        with self.assertRaises(ValueError):
            HitAndBlow(max_=10)

        game = HitAndBlow(correct_answer=33, allows_duplicate=True, len_answer=2)
        self.assertEqual("[1]1H1B", game.answer("34"))
        self.assertEqual("[1]1H1B", game.answer("34"))

    def test__generate_answer(self):
        count_values = 500
        count_keys = 504
        len_answer = 3
        game = HitAndBlow(len_answer=len_answer, min_=1, max_=9, allows_duplicate=False)
        # count_keys*count_values回実行する
        result = [int(''.join(game._generate_answer())) for _ in range(count_keys * count_values)]
        # 実行結果の集計
        import collections
        counted = collections.Counter(result)
        # イレギュラーな目が出ていないか確認
        expected = [x for x in range(10**len_answer)
                    if '0' not in list(str(x))
                    and count_duplicates(list(str(x))) == 0
                    and len(str(x)) == len_answer]
        self.assert_(set(counted.keys()) <= set(expected))
        # カイ二乗検定を行い、有意水準1%で偏りがないという帰無仮説を棄却できた場合にテスト失敗とする
        # だいたいどの目もcount_values回ほど出現するはずで、そこから著しくズレていれば失敗になる
        from scipy import stats
        chi_square_value, p_value = stats.chisquare(
            list(counted.values()),
            f_exp=[count_values]*count_keys
        )
        self.assertLess(0.01, p_value)
