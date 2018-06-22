import os
import csv
import errno
from functools import reduce


def will_it_float(element):
    try:
        float(element)
        return True
    except ValueError:
        return False


def flatten_list(l):
    return [item for items in l for item in items]


def count_truthy(list):
    return reduce(lambda x, y: x + 1 if(y) else x, list, 0)


def write_dict_to_csv(dict, file_name):
    keys = dict[0].keys()
    with open(file_name, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dict)
    transpose_csv(file_name)


def transpose_csv(file_name):
    a = zip(*csv.reader(open(file_name, "r")))
    csv.writer(open(file_name, "w")).writerows(a)


def create_folders(folders):
    for folder in folders:
        try:
            os.makedirs(folder)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
