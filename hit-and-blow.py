import unittest
from typing import List


def has_duplicates(lst: List):
    return len(lst) != len(set(lst))


class HitAndBlow:
    def __init__(self):
        self._numbers = list(range(1, 10))
        self._len_answer = 4
        self._correct_answer = self._generate_answer()
        print(self._correct_answer)

    def _generate_answer(self):
        import random
        return random.sample(self._numbers, k=self._len_answer)

    @staticmethod
    def _is_valid_format(answer: str):
        return answer.isnumeric()

    def check_answer(self, answer):
        if self._is_valid_format(answer):
            assert self._correct_answer
        else:
            pass


class TestHitAndBlow(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.hit = HitAndBlow()

    def test_answer(self):
        for i in self.hit._correct_answer:
            assert i in list(range(1, 10))
        assert not has_duplicates(self.hit._correct_answer)
        assert len(self.hit._correct_answer) == self.hit._len_answer
