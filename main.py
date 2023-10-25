import shutil
import os

# Path to the source folder where the source_folder files
source_folder = ''

# Path to the folder to move the files
destination_folder = ''

# List of files to transfer
files_to_move = []

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
