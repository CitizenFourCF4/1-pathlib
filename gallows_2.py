#!/usr/bin/env python

from argparse import ArgumentParser
from pathlib import Path

parser = ArgumentParser(
    description='Write text to a file at the given path',
    usage='gallows_2 [--help] text [--file_path=FILE_PATH]'
)
parser.add_argument('text', type=str, help='The text to be written to the file')
parser.add_argument(
    '--file_path',
    type=Path,
    default='./data/results.txt',
    help='Path to the file to which the text will be written and will be read'
)
arguments = parser.parse_args()
input_text = arguments.text
output_file_path = arguments.file_path

root_dir_path = Path()

# get file's absolute path
file_abs_path = (root_dir_path / 'gallows_2.py').absolute()
print(f'{file_abs_path = }')

# create a data folder in the directory with the gallows_2.py file
(root_dir_path / 'data').mkdir(exist_ok=True)

# create a file and write a text to it
output_file_path.write_text(input_text)

# print the contents of the file to the screen
file_content = output_file_path.read_text()
print(f'{file_content = }')
