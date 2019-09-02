import unittest
from typing import List


def has_duplicates(lst: List):
    return len(lst) != len(set(lst))


def count_duplicates(lst: List):
    return len(lst) - len(set(lst))


class HitAndBlow:
    _len_answer = 4

    def __init__(self, answer: int = 0):
        self._numbers = list(range(1, 10))
        self.is_over = False
        self.count_tries = 0
        if answer == 0:
            self._correct_answer = self._generate_answer()
        else:
            self._correct_answer = list(str(answer))

    def _generate_answer(self) -> List:
        import random
        return random.sample(self._numbers, k=self._len_answer)

    def score(self, int_answer: int):
        answer = list(str(int_answer))
        hit_ = len([i for i, j in zip(answer, self._correct_answer) if i == j])
        blow_ = count_duplicates(answer + self._correct_answer) - hit_
        return "{0}H{1}B".format(hit_, blow_)

    def input(self, input_: str):
        if input_ == "A":
            return "Correct answer is {}".format(self._correct_answer)
        elif input_.isnumeric() and len(input_) == self._len_answer:
            score = self.score(int(input_))
            self.count_tries += 1
            self.is_over = (score == "4H0B")
            return score
        else:
            return "Input {}-digit number.".format(self._len_answer)


class GameConsole:
    def __init__(self):
        self.game = HitAndBlow()
        self.main()

    def main(self):
        while True:
            score = self.game.input(input())
            print(score)
            if self.game.is_over:
                break


class TestDefDuplicates(unittest.TestCase):
    def test_count_duplicates(self):
        expected = 1
        actual = count_duplicates([1, 2, 3, 1])
        self.assertEqual(expected, actual)

    def test_has_duplicates(self):
        expected = True
        actual = has_duplicates([1, 2, 3, 1])
        self.assertEqual(expected, actual)


class TestHitAndBlow(unittest.TestCase):
    def test_score(self):
        self.game = HitAndBlow(1234)
        expect = "1H1B"
        actual = self.game.score(1389)
        self.assertEqual(expect, actual)

    def test_input(self):
        self.game = HitAndBlow(1234)
        expect = "0H4B"
        actual = self.game.input("4321")
        self.assertEqual(expect, actual)


if __name__ == "main":
    a = GameConsole()
    print(a)
    pass
