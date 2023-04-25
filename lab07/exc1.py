from typing import Any
from functools import reduce


def acronym(words: list[str]) -> str:
    """
    Return the acronym of given words.
    """
    # return reduce(lambda acronym, word: acronym + word[0].upper(), words, '')  # different implementation
    return ''.join([word[0].upper() for word in words])

def median(numbers: list[float]) -> float:
    """
    Return the median of given numbers.
    """
    numbers.sort()
    median_idx: int = len(numbers) // 2
    return (numbers[median_idx] if len(numbers) % 2 == 1
            else (numbers[median_idx] + numbers[median_idx - 1]) / 2)
        
def square_root(number: float, epsilon: float) -> float:
    """
    Return the approximate square root of a given number,
    based on Newton's formula.
    """ 
    def reached_precision(approx: float) -> bool:
        return abs(approx**2 - number) < epsilon
    def improve_approx(approx: float) -> float:
        return (approx + number / approx) / 2
    def approximate(approx: float) -> float:
        return (approx if reached_precision(approx)
                else approximate(improve_approx(approx)))
    return approximate(1)

def make_alpha_dict(string: str) -> dict[str, list[str]]:
    """
    Return a dictionary with letters as keys 
    and words containing that letter as values.
    """
    return {letter: [word for word in string.split() if letter in word] 
            for letter in string if letter.isalpha()}

def flatten(seq: list[Any]) -> list[Any]:
    """
    Return a flattened list.
    """
    return ([seq] if not isinstance(seq, (list, tuple))
            else [element for subseq in seq for element in flatten(subseq)])


if __name__ == '__main__':
    print(acronym(['Zakład', 'Ubezpieczeń', 'Społecznych']))
    print(median([1, 1, 19, 2, 3, 4, 4, 5, 1]))
    print(square_root(3, 0.1))
    print(make_alpha_dict('on i ona'))
    print(flatten([1, [2, 3], [[4, 5], 6]]))
