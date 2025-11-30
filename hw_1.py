# Завдання 1

from pathlib import Path
import shutil
from sys import argv


def copy_file(item: Path, dist: Path):
    extension = item.suffix
    extension_folder = dist / extension
    extension_folder.mkdir(exist_ok=True, parents=True)
    try:
        shutil.copy(item, extension_folder / item.name)
    except shutil.Error as e:
        print(e)


def iterate_folder(path: Path, dist: Path):
    for item in path.iterdir():
        try:
            if item.is_dir():
                iterate_folder(item, dist)
            else:
                copy_file(item, dist)
        except PermissionError:
            print(f"Немає доступу: {item}")


if len(argv) > 1:
    source_path = Path(argv[1])

    dist_path = None
    if len(argv) > 2:
        dist_path = Path(argv[2])
    if dist_path == None:
        dist_path = Path('dist')
    dist_path.mkdir(exist_ok=True)

    if (source_path.exists() and source_path.is_dir()):
        iterate_folder(source_path, dist_path)
    else:
        print("Вкажіть коректний шлях до директорій")
