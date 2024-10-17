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

def calculete_result():
    result = []

    if args.count_bytes:
        with open(args.filepath, "rb") as reader:
            bytes_content = reader.read()
            result.append(len(bytes_content))

    with open(args.filepath, "r", encoding='utf-8') as reader:
        content = reader.read()

    if args.count_lines:
        calculate_lines = content.count('\n') + 1
        result.append(calculate_lines)

    if args.count_words:
        calculate_words = len(content.split())
        result.append(calculate_words)

    if args.count_characters:
        calculate_characters = len(content)
        result.append(calculate_characters)

    return result

    
def structure() -> str:

    if not (args.count_bytes or args.count_lines or args.count_words or args.count_characters):
        args.count_lines = True
        args.count_words = True
        args.count_characters = True
    
    string = " ".join(str(num) for num in calculete_result()) + " " + str(args.filepath)

    return string

print(structure())

