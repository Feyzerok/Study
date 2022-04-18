import glob
import zipfile
from pathlib import Path
import shutil
import os

def relocator(path_from, path_to):
    try:
        files = glob.iglob(os.path.join(path_from, "*.md"))
        for file in files:
            if os.path.isfile(file):
                shutil.move(file, path_to)



        files = glob.iglob(os.path.join(path_from, "*.zip*"))
        for file in files:
            if os.path.isfile(file):
                path = path_to + '/assets'
                shutil.move(file, path)



        files = glob.iglob(os.path.join(path_from, "*.*"))
        for file in files:
            if os.path.isfile(file):
                shutil.move(file, path_to)
    except Exception as exc:
        print(f'ошибка при переносе {exc}')


def unzip(path_from, path_to):
    try:
        files = glob.iglob(os.path.join(path_from, "*.zip"))
        for file in files:
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(path_from)
            os.remove(file)

        files = glob.iglob(os.path.join(path_from, "*.PNG"))
        for file in files:
            if os.path.isfile(file):
                path = path_to + '/assets/imgs'
                shutil.move(file, path)

        files = glob.iglob(os.path.join(path_from, "*.jpg"))
        for file in files:
            if os.path.isfile(file):
                path = path_to + '/assets/imgs'
                shutil.move(file, path)

        files = glob.iglob(os.path.join(path_from, "*.jpeg"))
        for file in files:
            if os.path.isfile(file):
                path = path_to + '/assets/imgs'
                shutil.move(file, path)

        files = glob.iglob(os.path.join(path_from, "*.png"))
        for file in files:
            if os.path.isfile(file):
                path = path_to + '/assets/imgs'
                shutil.move(file, path)

        files = glob.iglob(os.path.join(path_from, "*.svg"))
        for file in files:
            if os.path.isfile(file):
                path = path_to + '/assets/imgs'
                shutil.move(file, path)

    except Exception as exc:
        print(f'ошибка при раззиповке {exc}')