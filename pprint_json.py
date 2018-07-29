import json
import sys


def read_data(file_path):
    try:
        with open(file_path, 'r') as file_object:
            file_data = file_object.read()
            return file_data
    except FileNotFoundError:
        return None


def load_data(file_data):
    try:
        json_data = json.loads(file_data)
        return json_data
    except json.decoder.JSONDecodeError:
        return None


def pretty_print_json(json_data):
    prettified_json = json.dumps(json_data,
                                 indent=4,
                                 sort_keys=True,
                                 ensure_ascii=False)
    print(prettified_json)


if __name__ == '__main__':
    try:
        json_file_path = sys.argv[1]
    except IndexError:
        sys.exit('При вызове скрипта надо ввести путь к файлу '
                 'с данными в json')
    file_data = read_data(json_file_path)
    if not file_data:
        sys.exit('Введенный путь к файлу в формате json не верен')
    loaded_dictionary = load_data(file_data)

    if not loaded_dictionary:
        sys.exit('Файл не в формате json')
    pretty_print_json(loaded_dictionary)
