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
        
def square_root(number: float, ) -> float:
    """
    Return the square root of given number.
    """
    return number ** 0.5