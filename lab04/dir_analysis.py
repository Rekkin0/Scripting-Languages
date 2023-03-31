import sys, subprocess, csv
from pathlib import Path


def get_files(dir: Path):
    for file in dir.iterdir():
        if file.is_dir():
            yield from get_files(file)
        elif file.is_file():
            yield file
        else:
            continue


if __name__ == "__main__":
    
    dir = Path(sys.argv[1]).expanduser().resolve()
    keys = ('filepath', 'char_count', 'word_count', 'line_count', 'most_common_char', 'most_common_word')
    results = []
    
    for file in get_files(dir):
        output = subprocess.run(["python3", "txt_analysis.py"], input=str(file), text=True, capture_output=True).stdout
        reader = csv.DictReader(output, fieldnames=keys, delimiter="\t")
        #results.append()
        
    print(*results, sep="\n")
