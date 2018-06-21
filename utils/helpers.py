def will_it_float(element):
    try:
        float(element)
        return True
    except ValueError:
        return False


def flatten_list(l):
    return [item for items in l for item in items]
