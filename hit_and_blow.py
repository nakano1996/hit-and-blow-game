from typing import List


def count_duplicates(lst: List):
    return len(lst) - len(set(lst))


class HitAndBlow:

    class DuplicationError(Exception):
        pass

    class NotNumericError(Exception):
        pass

    class LengthError(Exception):
        pass

    def __init__(self, len_answer: int = 4, correct_answer: int = 0,
                 min_: int = 1, max_: int = 9,
                 allows_duplicate: bool = False):
        # rules
        self._len_answer = len_answer
        self._allows_duplicate = allows_duplicate
        self._1_digit_numbers = self._get_numbers_list(min_, max_)
        # score
        self._hit = 0
        self._blow = 0
        self._is_over = False
        self._stored_answers = []
        # answer
        if correct_answer:
            self._valid_answer(str(correct_answer))
            self._correct_answer = list(str(correct_answer))
        else:
            self._correct_answer = self._generate_answer()

    @staticmethod
    def _get_numbers_list(min_: int, max_: int):
        if min_ == max_:
            raise ValueError("min = max")
        elif min_ > max_:
            raise ValueError("min > max")
        elif {min_, max_}.isdisjoint(set(range(0, 10))):  # 1桁の数値か？
            raise ValueError()
        else:
            return [str(n) for n in range(min_, max_ + 1)]

    def _generate_answer(self) -> List:
        import random
        if self._allows_duplicate:
            fn = random.choices
        else:
            fn = random.sample
        return fn(self._1_digit_numbers, k=self._len_answer)

    def _score(self, answer_: str):
        self._valid_answer(answer_)
        self._hit = len([i for i, j in zip(list(answer_), self._correct_answer) if i == j])
        self._blow = count_duplicates(list(answer_) + self._correct_answer) - self._hit
        self._is_over = (self._hit == self._len_answer)
        self._stored_answers.append(answer_)

    @property
    def is_over(self):
        return self._is_over

    def _valid_answer(self, answer_: str):
        if not answer_.isnumeric():
            raise self.NotNumericError()
        if len(answer_) != self._len_answer:
            raise self.LengthError()
        if not self._allows_duplicate and count_duplicates(list(answer_)):
            raise self.DuplicationError()

    def answer(self, input_: str):
        input_ = input_.upper()
        try:
            self._score(input_)
            return "[{2}]{0}H{1}B".format(self._hit, self._blow, len(self._stored_answers))
        except self.DuplicationError:
            return "Please enter a unique number."
        except (self.NotNumericError, self.LengthError):
            if input_ in ["", "?", "H"]:
                return "Wikipedia: 'https://en.wikipedia.org/wiki/Mastermind_(board_game)'"
            elif input_ == "A":
                return "Correct [A]nswer is {}.".format(self._correct_answer)
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
    GameConsole(HitAndBlow())
