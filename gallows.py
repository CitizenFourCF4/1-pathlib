from pathlib import Path
root_dir_path = Path()
# get file's absolute path
file_abs_path = (root_dir_path / 'gallows.py').absolute()
print(f'{file_abs_path = }')
# create a data folder in the directory with the gallows.py file
(root_dir_path / 'data').mkdir(exist_ok=True)
# create a text.txt file and write a line to it
file = root_dir_path / 'data/text.txt'
file.write_text('Hi, im a text in file!')
# print the contents of the file to the screen
file_content = file.read_text()
print(f'{file_content = }')
