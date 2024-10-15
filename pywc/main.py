import argparse
import pathlib 

parser = argparse.ArgumentParser()
parser.add_argument("filepath", help="archivo a procesar", type=pathlib.Path)
parser.add_argument("-c", "--count-bytes", help="contador de bytes",
                    action="store_true")
parser.add_argument("-l", "--count-lines", help="contador de lineas",
                    action="store_true")
parser.add_argument("-w", "--count-words", help="contador de palabras",
                    action="store_true")
parser.add_argument("-m", "--count-characters", help="contador de caracteres",
                    action="store_true")

args = parser.parse_args()

def count_bytes(filepath):
    with open(args.filepath, "r", encoding='utf-8') as reader:
        return len(reader.read())
    
def count_lines(filepath):
    with open(args.filepath, "r", encoding='utf-8') as reader:
        return len(reader.readlines())
    
def count_words(filepath):
    with open(args.filepath, "r", encoding='utf-8') as reader:
        return len(reader.read().split())
    
def count_characters(filepath):
    with open(args.filepath, "r", encoding='utf-8') as reader:
        return sum(len(line) for line in reader.read().splitlines())
    
def structure() -> str:
    result = []

    if args.count_bytes:
        result.append(count_bytes(args.filepath))

    if args.count_lines:
        result.append(count_lines(args.filepath))

    if args.count_words:
        result.append(count_words(args.filepath))

    if args.count_characters:
        result.append(count_characters(args.filepath))

    if len(result) < 1:
        return f"{count_bytes(args.filepath)} {count_lines(args.filepath)} {count_words(args.filepath)} {args.filepath}"
    else:
        return " ".join(str(num) for num in result) + " " + str(args.filepath)

print(structure())

