def acronym(words: list[str]) -> str:
    """
    Return the acronym of given words.
    """
    return ''.join([word[0].upper() for word in words])

def median(numbers: list[float]) -> float:
    """
    Return the median of given numbers.
    """
    odd_median = numbers[len(numbers) // 2]
    return odd_median if len(numbers) % 2 == 1 \
        else (odd_median + numbers[len(numbers) // 2 - 1]) / 2
        
def square_root(number: float, epsilon: float) -> float:
    """
    Return the approximate square root of a given number.
    """
    def auxiliary(approx: float) -> float:
        return approx if abs(approx**2 - number) < epsilon \
            else auxiliary((approx + number / approx) / 2)
    
    return auxiliary(number)

def make_alpha_dict(string: str) -> dict[str, list[str]]:
    """
    Return a dictionary with letters as keys and words containing that letter as values.
    """
    return {letter: [word for word in string.split() if letter in word] for letter in string if letter.isalpha()}

def flatten(lists: list) -> list:
    """
    Return a flattened list.
    """
    return [lists] if not isinstance(lists, (list, tuple)) \
        else [element for sublist in lists for element in flatten(sublist)]


if __name__ == '__main__':
    raise NotImplementedError
    print(square_root(3, 0.1))
    print(make_alpha_dict('on i ona'))
    print(flatten([1, [2, 3], [[4, 5], 6]]))