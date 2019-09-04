from typing import List


def has_duplicate(lst: List):
    return count_duplicates(lst) > 0


def count_duplicates(lst: List):
    return len(lst) - len(set(lst))


class HitAndBlow:
    _len_answer = 4

    def __init__(self, answer_: int = 0):
        self._numbers = [str(n) for n in range(1, 10)]
        self.is_over = False
        self.count_tries = 0
        if answer_ == 0:
            self._correct_answer = self._generate_answer()
        else:
            self._correct_answer = list(str(answer_))

    def _generate_answer(self) -> List:
        import random
        return random.sample(self._numbers, k=self._len_answer)

    def score(self, int_answer: int):
        answer_ = list(str(int_answer))
        hit_ = len([i for i, j in zip(answer_, self._correct_answer) if i == j])
        blow_ = count_duplicates(answer_ + self._correct_answer) - hit_
        return "{0}H{1}B".format(hit_, blow_)

    def answer(self, input_: str):
        if input_ in ["", "?", "H"]:
            pass  # todo:マニュアル返す
        elif input_ == "A":
            return "Correct answer is {}".format(self._correct_answer)
        elif input_.isnumeric() and len(input_) == self._len_answer:
            if has_duplicate(input_):
                return "Don't duplicate numbers."
            else:
                score_ = self.score(int(input_))
                self.count_tries += 1
                self.is_over = (score_ == "4H0B")
                return score_
        else:
            return "Input {}-digit number.".format(self._len_answer)


class GameConsole:
    def __init__(self):
        self.game = HitAndBlow()
        self.main()

    def main(self):
        while True:
            score = self.game.answer(input())
            print(score)
            if self.game.is_over:
                break


if __name__ == "main":
    GameConsole()
