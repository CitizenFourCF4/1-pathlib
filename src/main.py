#!/usr/bin/env python

from functions import parse_command_line_args
from functions import set_of_logger
from functions import check_for_user_input


def main():
    set_of_logger()

    input_text, output_file_path = parse_command_line_args()

    check_for_user_input()
    # creating folders if the current directory does not exist
    output_file_path.parent.mkdir(exist_ok=True, parents=True)
    # create a file and write a text to it
    output_file_path.write_text(input_text)

    # print the contents of the file to the screen
    file_content = output_file_path.read_text()
    print(f'{file_content = }')


if __name__ == "__main__":
    main()
