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
