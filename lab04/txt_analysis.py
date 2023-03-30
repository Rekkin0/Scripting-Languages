import csv, sys
from pathlib import Path
from collections import Counter


if __name__ == "__main__":
    
    filepath = Path(input())
    with open(filepath, "r") as file:
        text = file.read()
    
    char_count = len(text)
    
    words = text.split()
    word_count = len(words)
    
    line_count = len(text.splitlines())
    
    char_occurences = Counter(text)
    # char_occurences.pop(' ')
    most_common_char = char_occurences.most_common(1)[0][0]
    
    word_occurences = Counter(words)
    most_common_word = word_occurences.most_common(1)[0][0]
    
    result = {
        'filepath': filepath,
        'char_count': char_count,
        'word_count': word_count,
        'line_count': line_count,
        'most_common_char': most_common_char,
        'most_common_word': most_common_word,
    }

    writer = csv.DictWriter(sys.stdout, fieldnames=result.keys(), delimiter="\t")
    writer.writerow(result)
    # print(*result.values(), sep="\t")
    
    #/home/rekkin/text/file1
    