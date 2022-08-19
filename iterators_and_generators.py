#!/usr/bin/env python

from argparse import ArgumentParser
from pathlib import Path
import random
from string import ascii_letters
import functools

root_dir_path = Path()

signs = ascii_letters


def single_line_generator(words_amount, letters_amount):
    generator = [(''.join(random.choice(signs) for _ in range(letters_amount))) for _ in range(words_amount)]
    return generator


def multi_line_generator(words_amount, letters_amount):
    counter = 0
    while True:
        word = ''.join(random.choice(signs) for _ in range(letters_amount))
        yield word
        counter += 1
        if counter == words_amount:
            break


generator_with_condition = functools.partial(multi_line_generator, 10, 5)


def create_custom_string(iterable_object):
    return ' '.join(item for item in iterable_object)


def command_line_parsing():
    parser = ArgumentParser(
        description='Write text to a file at the given path',
        usage='python gallows_2.py [--help] --text=TEXT [--file_path=FILE_PATH]'
    )
    parser.add_argument(
        '--text',
        type=str,
        default=create_custom_string(random.choice([single_line_generator(5, 2), generator_with_condition()])),
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
