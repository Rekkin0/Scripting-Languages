import sys, subprocess, csv
from pathlib import Path


def get_files(dirpath: Path):
    for filepath in dirpath.iterdir():
        if filepath.is_dir():
            yield from get_files(filepath)
        elif filepath.is_file():
            yield filepath
        else:
            continue


if __name__ == "__main__":
    
    dirpath = Path(sys.argv[1]).expanduser().resolve()
    keys = ('filepath', 'char_count', 'word_count', 'line_count', 'most_common_char', 'most_common_word')
    results = []
    
    for filepath in traverse_dirs(dirpath):
        output = subprocess.run(["python3", "txt_analysis.py"], input=str(filepath), text=True, capture_output=True).stdout
        reader = csv.DictReader(output, fieldnames=keys, delimiter="\t")
        results.append()
        
    print(*results, sep="\n")
