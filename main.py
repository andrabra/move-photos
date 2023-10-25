import shutil
import os

# Путь к исходной папке, где находятся файлы
source_folder = 'D:\a'

# Путь к папке, в которую нужно перенести файлы
destination_folder = 'D:\b'

# Список файлов, которые нужно перенести
files_to_move = ['IMG_5146.CR2',
'IMG_5147.CR2',
'IMG_5156.CR2',
'IMG_5185.CR2',
'IMG_5194.CR2',
'IMG_5213.CR2',
'IMG_5258.CR2',
'IMG_5282.CR2',
'IMG_5297.CR2',
'IMG_5323.CR2',
'IMG_5368.CR2',
'IMG_5401.CR2',
'IMG_5405.CR2',
'IMG_5432.CR2',
'IMG_5466.CR2',
'IMG_5492.CR2',
'IMG_5577.CR2',
'IMG_5669.CR2',
'IMG_5688.CR2',
'IMG_5737.CR2',
'IMG_5700.CR2',
'IMG_5709.CR2',
'IMG_5717.CR2',
'IMG_5934.CR2',
'IMG_5979.CR2',
'IMG_6002.CR2',
'IMG_6042.CR2',
'IMG_6077.CR2',
'IMG_6113.CR2',
'IMG_6160.CR2']

for file_name in files_to_move:
    source_path = os.path.join(source_folder, file_name)
    destination_path = os.path.join(destination_folder, file_name)

    try:
        shutil.move(source_path, destination_path)
        print(f"Файл '{file_name}' успешно перенесен в {destination_folder}")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден в {source_folder}")
    except shutil.Error as e:
        print(f"Ошибка при переносе файла '{file_name}': {e}")

# По завершении работы программы, файлы будут перемещены в указанную папку.
