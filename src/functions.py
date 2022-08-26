from argparse import ArgumentParser
from functools import partial
from pathlib import Path
from random import choice
from string import ascii_letters


def single_line_generator(words_amount, letters_amount):
    generator = [(''.join(choice(ascii_letters) for _ in range(letters_amount))) for _ in range(words_amount)]
    return generator


def multi_line_generator(words_amount, letters_amount):
    counter = 0
    while True:
        word = ''.join(choice(ascii_letters) for _ in range(letters_amount))
        yield word
        counter += 1
        if counter == words_amount:
            break


generator_with_condition = partial(multi_line_generator, 10, 5)


def create_custom_string(iterable_object):
    return ' '.join(item for item in iterable_object)


def command_line_parsing():
    parser = ArgumentParser(
        description='Write text to a file at the given path',
        usage='python main.py [--help] [--text=TEXT] [--file_path=FILE_PATH]'
    )
    parser.add_argument(
        '--text',
        type=str,
        default=create_custom_string(choice([single_line_generator(5, 2), generator_with_condition()])),
        help='The text to be written to the file'
    )
    parser.add_argument(
        '--file_path',
        type=Path,
        default=Path() / 'data' / 'results.txt',
        help='Path to the file to which the text will be written and will be read',
    )
    arguments = parser.parse_args()
    input_text = arguments.text
    output_file_path = arguments.file_path

    return input_text, output_file_path
