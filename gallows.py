rom pathlib import Path
root_dir_path = Path.cwd()
## Get file's absolute path
abs_path = Path('gallows.py').absolute()
print(f'{abs_path = }')
## create a data folder in the directory with the gallows.py file
Path("data").mkdir(exist_ok = True)
## create a text.txt file and write a line to it
d = Path(root_dir_path, 'data/text.txt')
d.write_text('Hi, im a text in file!')
## print the contents of the file to the screen
consinstance_of_file = d.read_text()
print(f'{consinstance_of_file = }')
