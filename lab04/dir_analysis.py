import sys, subprocess, csv
from pathlib import Path
from collections import Counter
from _collections_abc import Generator
from txt_analysis import DictAnalysis


def get_files(dir: Path) -> Generator[Path, None, None]:
    for file in dir.iterdir():
        if file.is_dir():
            yield from get_files(file)
        elif file.is_file():
            yield file
        else:
            continue


def process_files(dir: Path) -> list[DictAnalysis]:
    keys = ('filepath', 'char_count', 'word_count', 'line_count', 'most_common_char', 'most_common_word')
    results = []
    for file in get_files(dir):
        raw_output = subprocess.run(["python3", "txt_analysis.py"], input=str(file), text=True, capture_output=True).stdout
        output = csv.DictReader(raw_output.splitlines(), fieldnames=keys, delimiter="\t")
        results.append(next(output))
        
    return results
    
    
def calculate_properties(results: list[DictAnalysis]) -> tuple:
    file_count = len(results)
    char_count = sum(int(result['char_count']) for result in results) # type: ignore
    word_count = sum(int(result['word_count']) for result in results) # type: ignore
    line_count = sum(int(result['line_count']) for result in results) # type: ignore
    most_common_char = str(Counter(result['most_common_char'] for result in results).most_common(1)[0][0]) # type: ignore
    most_common_word = str(Counter(result['most_common_word'] for result in results).most_common(1)[0][0]) # type: ignore
    
    most_common_char = "'" + most_common_char + "'"
    most_common_word = "'" + most_common_word + "'"
    return file_count, char_count, word_count, line_count, most_common_char, most_common_word


if __name__ == "__main__":
    dir = Path(sys.argv[1]).expanduser().resolve()
    results = process_files(dir)
    print(*calculate_properties(results), sep="\t")
