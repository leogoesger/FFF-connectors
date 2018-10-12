import os
import csv
import errno
from os import path
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
    """[Transpose csv in place]

    Arguments:
        file_name {[string]} -- [path of the file]
    """

    a = zip(*csv.reader(open(file_name, "r")))
    csv.writer(open(file_name, "w")).writerows(a)


def create_folders(folders):
    for folder in folders:
        try:
            os.makedirs(folder)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise


def read_csv_to_arrays(file_path, header=False):
    if(path.splitext(file_path)[1] == '.csv'):
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            if header:
                return [row for index, row in enumerate(reader) if index > 0]
            else:
                return [row for row in reader]


def write_arrays_to_csv(arrays, file_path):
    with open(file_path, "w") as output:
        writer = csv.writer(output, delimiter=',', lineterminator='\n')
        for val in arrays:
            writer.writerow(val)
