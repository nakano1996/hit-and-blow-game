from typing import List


def has_duplicate(lst: List):
    return count_duplicates(lst) > 0


def count_duplicates(lst: List):
    return len(lst) - len(set(lst))


class HitAndBlow:

    class DuplicationError(Exception):
        pass

    class NotNumericError(Exception):
        pass

    class LengthError(Exception):
        pass

    def __init__(self, len_answer, answer_: int = 0):
        self._len_answer = len_answer
        self._1_digit_numbers = [str(n) for n in range(1, 10)]
        self._hit = 0
        self._blow = 0
        self._is_over = False
        self._count_tries = 0
        if answer_:
            self._valid_answer(str(answer_))
            self._correct_answer = list(str(answer_))
        else:
            self._correct_answer = self._generate_answer()

    def _generate_answer(self) -> List:
        import random
        return random.sample(self._1_digit_numbers, k=self._len_answer)

    def _score(self, answer_: str):
        answer_ = list(answer_)
        self._hit = len([i for i, j in zip(answer_, self._correct_answer) if i == j])
        self._blow = count_duplicates(answer_ + self._correct_answer) - self._hit
        self._is_over = (self._hit == self._len_answer)
        self._count_tries += 1

    @property
    def is_over(self):
        return self._is_over

    def _valid_answer(self, answer_: str):
        if not answer_.isnumeric():
            raise self.NotNumericError()
        if len(answer_) != self._len_answer:
            raise self.LengthError()
        if has_duplicate(list(answer_)):
            raise self.DuplicationError()

    def answer(self, input_: str):
        input_ = input_.upper()
        try:
            self._valid_answer(input_)
            self._score(input_)
            return "[{2}]{0}H{1}B".format(self._hit, self._blow, self._count_tries)
        except self.DuplicationError:
            return "Please enter a unique number."
        except (self.NotNumericError, self.LengthError):
            if input_ in ["", "?", "H"]:
                pass  # todo:マニュアル返す
            elif input_ == "A":
                return "Correct [A]nswer is {}".format(self._correct_answer)
            else:
                return "Please enter a {}-digit number.".format(self._len_answer)


class GameConsole:
    def __init__(self, game: HitAndBlow):
        self.game = game
        self.main()

    def main(self):
        while not self.game.is_over:
            score = self.game.answer(input())
            print(score)


if __name__ == '__main__':
    GameConsole(HitAndBlow(4))
