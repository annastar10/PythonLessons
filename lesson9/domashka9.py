import os.path as pth
import random as rnd
import string
import json


def get_names_from_file(path, name_pos=1):
    names = []
    if not pth.isfile(path):
        return names
    with open(path) as file:
        for line in file:
            line = line.strip().split("\t")
            names.append(line[name_pos])
    return names


def create_rnd_string(min_limit, max_limit):
    chars = string.ascii_letters
    str_range = rnd.randint(min_limit, max_limit)
    return ''.join(rnd.choice(chars) for i in range(str_range))


def get_rnd_value(value_type, value_rules):
    if value_type == "int":
        val = rnd.randint(value_rules[value_type]["min"], value_rules[value_type]["max"])
    elif value_type == "float":
        val = rnd.random()
    elif value_type == "bool":
        val = rnd.choice(value_rules[value_type])
    else:
        return "unknown error"
    return val


def generate_and_write_json(file_path):
    with open(file_path, 'w') as file:
        loaded = json.loads(json_string)
        json.dump(loaded, file, indent=4)


# zadanie 1
names_src = 'namex.txt'
only_surnames = get_names_from_file(names_src)
print('\n\n zadanie 1 - (Только Фамилии из списка): ', only_surnames, "\n\n")

# zadanie 2
json_key_len = 5
min_keys_qty = 5
max_keys_qty = 20
value_rules = {"float": {"min": 0, "max": 1}, "int": {"min": -100, "max": 100}, "bool": [True, False]}
keys_qty = rnd.randint(min_keys_qty, max_keys_qty)
rand_key_values = {create_rnd_string(json_key_len, json_key_len).lower():
            get_rnd_value(rnd.choice(["bool", "float", "int"]), value_rules) for k in
        range(keys_qty)}
json_string = json.dumps(rand_key_values)
print("Zadanie 2 - (Случайный json): \n", json.dumps(json_string, indent=4), "\n\n")


# zadanie 3
out_json_path = "outfile.json"
generate_and_write_json(out_json_path)

