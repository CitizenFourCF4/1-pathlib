#!/usr/bin/env python

from argparse import ArgumentParser
from pathlib import Path

root_dir_path = Path()


def command_line_parsing():
    parser = ArgumentParser(
        description='Write text to a file at the given path',
        usage='python gallows_2.py [--help] --text=TEXT [--file_path=FILE_PATH]'
    )
    parser.add_argument('--text', type=str, required=True, help='The text to be written to the file')
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

    # get file's absolute path
    file_abs_path = (root_dir_path / 'gallows_2.py').absolute()
    print(f'{file_abs_path = }')

    # creating folders if the current directory does not exist
    output_file_path.parent.mkdir(exist_ok=True, parents=True)
    # create a file and write a text to it
    output_file_path.write_text(input_text)

    # print the contents of the file to the screen
    file_content = output_file_path.read_text()
    print(f'{file_content = }')


if __name__ == "__main__":
    main()
