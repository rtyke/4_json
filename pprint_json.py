import json
import sys


def load_data(file_path):
    try:
        with open(file_path, 'r') as file_object:
            file_data = file_object.read()
            return file_data
    except FileNotFoundError:
        return None


def convert_to_json(file_data):
    try:
        json_data = json.loads(file_data)
        return json_data
    except json.decoder.JSONDecodeError:
        return None


def pretty_print_json(data):
    prettified_json = json.dumps(data, indent=4, sort_keys=True,
                                 ensure_ascii=False)
    return prettified_json


if __name__ == '__main__':
    json_file_path = sys.argv[1]
    file_data = load_data(json_file_path)
    if not file_data:
        sys.exit('Введенный путь к файлу в формате json не верен')
    json_data = convert_to_json(file_data)
    if not json_data:
        sys.exit('Файл не в формате json')
    print(pretty_print_json(json_data))
