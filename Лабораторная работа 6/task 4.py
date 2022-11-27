import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename) as file_csv:  # TODO реализовать конвертер из csv в json
        list_ = []
        for index, line in enumerate(file_csv):
            trans_line = line.strip(new_line).split(delimiter)
            if index == 0:
                column = trans_line
            list_dict = [{f'{column[i]}': n for i, n in enumerate(trans_line) if index != 0}]
            if index != 0:
                list_.extend(list_dict)
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))