from argparse import ArgumentParser
from loguru import logger
from pathlib import Path
from random import choice
from string import ascii_letters
from sys import argv, stdout


def set_of_logger():
    logger.remove()
    logger.add('./logs/debug.log', format='{time} {function} {line} {level} {message}', level='DEBUG')
    logger.add(stdout, format='{time} {level} {message}', level='INFO')


def generate_words_via_single_line(words_amount: int, letters_amount: int) -> list[str]:
    generator = [(''.join(choice(ascii_letters) for _ in range(letters_amount))) for _ in range(words_amount)]
    logger.debug(f'{generator = }')
    return generator


def generate_words_via_multi_line(words_amount: int, letters_amount: int):
    counter = 0
    while True:
        word = ''.join(choice(ascii_letters) for _ in range(letters_amount))
        yield word
        logger.debug(f'{word = }')
        counter += 1
        if counter == words_amount:
            break


def create_custom_string(iterable_object) -> str:
    return ' '.join(item for item in iterable_object)


def parse_command_line_args() -> tuple[str, Path]:
    parser = ArgumentParser(
        description='Write text to a file at the given path',
        usage='python gallows_2.py [--help] [--text=TEXT] [--file_path=FILE_PATH]'
    )
    parser.add_argument(
        '--text',
        type=str,
        default=create_custom_string(choice([generate_words_via_single_line(5, 2),
                                             generate_words_via_multi_line(10, 5)])),
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
    logger.debug(f'{input_text = }')
    logger.debug(f'{output_file_path = }')
    return input_text, output_file_path


def check_for_user_input():
    if len(argv) == 2:
        if argv[1].startswith("--text="):
            logger.info("User enter text")
            logger.info("User did not enter file path. Default value used")
        else:
            logger.info("User did not enter text. Default value used")
            logger.info("User enter file path.")
    elif len(argv) == 3:
        logger.info("User enter text")
        logger.info("User enter file path.")
    else:
        logger.info("User did not enter text. Default value used")
        logger.info("User did not enter file path. Default value used")
