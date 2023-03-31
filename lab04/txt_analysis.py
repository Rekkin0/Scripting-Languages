import csv, sys
from pathlib import Path
from collections import Counter
from typing import Any


DictAnalysis = dict[str, Path | int | str]


def analyze_file(filepath: Path) -> DictAnalysis:
    with open(filepath, 'r') as file:
        text = file.read()
    
    char_count = len(text)
    word_count = len(words := text.split())
    line_count = len(text.splitlines())
    most_common_char = Counter(text).most_common(1)[0][0]
    most_common_word = Counter(words).most_common(1)[0][0]
    
    return {
        'filepath': filepath,
        'char_count': char_count,
        'word_count': word_count,
        'line_count': line_count,
        'most_common_char': most_common_char,
        'most_common_word': most_common_word,
    }
    

if __name__ == "__main__":
    filepath = Path(input()).expanduser().resolve()
    result = analyze_file(filepath)
    writer = csv.DictWriter(sys.stdout, fieldnames=result.keys(), delimiter='\t')
    writer.writerow(result)
    