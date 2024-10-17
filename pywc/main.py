import argparse
import pathlib
import time

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

    byte_count = 0
    line_count = 0
    word_count = 0
    character_count = 0

    with open(args.filepath, "rb") as reader:

        for line in reader:
            byte_count += len(line)
            line_count += 1
            word_count += len(line.decode(encoding='utf-8', errors='strict').split())
            character_count += len(line.decode(encoding='utf-8', errors='strict'))


    if args.count_bytes:
        result.append(byte_count)

    if args.count_lines:
        result.append(line_count)

    if args.count_words:
        result.append(word_count)

    if args.count_characters:
        result.append(character_count)

    return result
    


def structure() -> str:

    if not (args.count_bytes or args.count_lines or args.count_words or args.count_characters):
        args.count_bytes = True
        args.count_lines = True
        args.count_characters = True
    
    string = " ".join(str(num) for num in calculete_result()) + " " + str(args.filepath)

    return string

t0 = time.perf_counter()
print(structure())
print("Elapsed time", time.perf_counter() - t0)
