import json as parser
import os


def concat_path(folder, file_name, makedir=False):
    if makedir:
        check_dir(folder)
    path = os.path.join(folder, file_name)
    return path


def check_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def read_json(file):
    with open(file, 'r', encoding='utf-8') as json_reader:
        json_dict = parser.loads(json_reader.read())
        return json_dict
