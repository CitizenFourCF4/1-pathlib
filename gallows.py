from pathlib import Path
## получаем абсолютный путь файла
pat = Path(Path.cwd(), Path("gallows.py"))
print(f'Абсолютный путь файла - {pat}')
## создаем папку data, в директории с файлом gallows.py
papka = Path("data").mkdir()
## создаем файл text.txt и записываем в него строку
d = Path(Path.cwd(), Path("data/text.txt"))
d.touch()
d.write_text('Hi, im a text in file!')
## выводим содержимое строки на экран
print(d.read_text())
