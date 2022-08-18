#!/usr/bin/env python

from argparse import ArgumentParser
from pathlib import Path
import random
import string

root_dir_path = Path()

signs = string.ascii_letters


def single_line_generator(words_amount, letters_amount):
    generator = [(''.join(random.choice(signs) for _ in range(letters_amount))) for _ in range(words_amount)]
    return generator


def multi_line_generator(words_amount, letters_amount):
    for _ in range(words_amount):
        word = ''.join(random.choice(signs) for _ in range(letters_amount))
        yield word


def using_multi_line_generator(words_amount, letters_amount):
    sp = []
    for num in multi_line_generator(words_amount, letters_amount):
        sp.append(num)
    return sp


def create_custom_string_using_for(iterable_object):
    return ' '.join(item[1] for item in enumerate(iterable_object))


def create_custom_string_using_map(iterable_object):
    return ' '.join(map(str, iterable_object))


def command_line_parsing():
    parser = ArgumentParser(
        description='Write text to a file at the given path',
        usage='python gallows_2.py [--help] --text=TEXT [--file_path=FILE_PATH]'
    )
    parser.add_argument(
        '--text',
        type=str,
        default=create_custom_string_using_for(single_line_generator(2, 4)),
        help='The text to be written to the file'
    )
    parser.add_argument(
        '--file_path',
        type=Path,
        default=root_dir_path / 'data' / 'results.txt',
        help='Path to the file to which the text will be written and will be read',
    )
    arguments = parser.parse_args()
    input_text = arguments.text
    output_file_path = arguments.file_path

    return input_text, output_file_path


def main():
    input_text, output_file_path = command_line_parsing()

    # creating folders if the current directory does not exist
    output_file_path.parent.mkdir(exist_ok=True, parents=True)
    # create a file and write a text to it
    output_file_path.write_text(input_text)

    # print the contents of the file to the screen
    file_content = output_file_path.read_text()
    print(f'{file_content = }')


if __name__ == "__main__":
    main()
