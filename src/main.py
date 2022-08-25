#!/usr/bin/env python

from functions import *


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
