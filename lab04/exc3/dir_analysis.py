import sys, subprocess, csv
from pathlib import Path
from collections import Counter
from _collections_abc import Generator

from utils import SCRIPT_DIR, KEYS


ResultDict = dict[str, str]
ResultList = list[ResultDict]
Outcome = tuple[int, int, int, int, str, str]


def get_text_files(dir: Path) -> Generator[Path, None, None]:
    """
    Recursively yields Path objects of all text files in a directory.
    """
    for file in dir.iterdir():
        if file.is_dir():
            yield from get_text_files(file)
        elif file.is_file() and file.suffix == '.txt':
            yield file
        else:
            continue


def analyze_files(dir: Path, include_spaces: bool = False) -> ResultList:
    """
    Runs txt_analysis.py on all text files in a directory and returns a list 
    of dictionaries with the results.
    """
    results = []
    command = ['python3', 'txt_analysis.py']
    if include_spaces: command.append('-i')
    for file in get_text_files(dir):
        output = subprocess.run(command, cwd=SCRIPT_DIR, input=str(file), text=True, 
                                capture_output=True).stdout
        result = csv.DictReader(output.splitlines(), fieldnames=KEYS, delimiter="\t")
        results.append(next(result))
        
    return results
    
    
def process_results(results: ResultList) -> Outcome:
    """
    Processes the results of txt_analysis.py being run on all text files in a directory 
    and returns a tuple with the outcome.
    """
    file_count = len(results)
    char_count = sum(int(result['char_count']) for result in results)
    word_count = sum(int(result['word_count']) for result in results)
    line_count = sum(int(result['line_count']) for result in results)
    most_common_char = Counter(result['most_common_char'] for result in results).most_common(1)[0][0]
    most_common_word = Counter(result['most_common_word'] for result in results).most_common(1)[0][0]
    
    most_common_char, most_common_word = f"'{most_common_char}'", f"'{most_common_word}'"
    
    return file_count, char_count, word_count, line_count, most_common_char, most_common_word


def pretty_print_outcome(outcome: Outcome) -> None:
    """
    Prints the outcome of the processed results of txt_analysis.py being run 
    on all text files in a directory in a neat format.
    """
    headers = [header.replace('_', ' ').capitalize() for header in KEYS]
    headers[0] = 'File count'
    print(*headers, sep='\t')
    
    print(f'{outcome[0]:>10}\t{outcome[1]:>10}\t{outcome[2]:>10}\t{outcome[3]:>10}\t'
          f'{outcome[4]:<16}\t{outcome[5]:<16}')


if __name__ == '__main__':
    include_spaces = input('Include spaces in evaluating the most common character? (y/N): ').lower() == 'y'
    dir = Path(sys.argv[1]).expanduser().resolve()
    results = analyze_files(dir, include_spaces)
    outcome = process_results(results)
    pretty_print_outcome(outcome)
