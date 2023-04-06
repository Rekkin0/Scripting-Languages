import csv, sys
from pathlib import Path
from collections import Counter

from utils import KEYS


AnalysisDict = dict[str, Path | int | str]


def analyze_file(file_path: Path, include_spaces: bool = False) -> AnalysisDict:
    """
    Analyzes a text file and returns a dictionary with the results.
    """
    with open(file_path) as file:
        text = file.read()
    
    char_count = len(text)
    word_count = len(words := text.split())
    line_count = len(text.splitlines())
    
    char_occurences = Counter(text)
    if not include_spaces: char_occurences.pop(' ')
    most_common_char = char_occurences.most_common(1)[0][0]
    
    word_occurences = Counter(words)
    most_common_word = word_occurences.most_common(1)[0][0]
    
    values = (file_path, char_count, word_count, line_count, most_common_char, most_common_word)
    return dict(zip(KEYS, values))


if __name__ == '__main__':
    include_spaces = len(sys.argv) > 1 and sys.argv[1] == '-i'
    file_path = Path(input()).expanduser().resolve()
    if not file_path.is_file():
        print(f"{file_path} is not a file.")
        exit()
    result = analyze_file(file_path, include_spaces)
    writer = csv.DictWriter(sys.stdout, fieldnames=result.keys(), delimiter='\t')
    writer.writerow(result)
    