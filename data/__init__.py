import os
BASE_PATH = os.path.dirname(os.path.realpath(__file__))


def get_file_path(file_name, folder=''):
    return os.path.join(BASE_PATH, folder, file_name)
