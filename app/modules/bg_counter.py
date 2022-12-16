from flask import url_for
import random


def get_files(target):
    import pathlib
    initial_count = 0
    for path in pathlib.Path("app" + target).iterdir():
        if path.is_file():
            initial_count += 1
    return initial_count


def bg_counter():
    DIR = url_for('static', filename='Data/images/backgrounds')
    file = random.randint(1, get_files(DIR) - 1)
    return DIR + "/" + str(file) + ".png"
