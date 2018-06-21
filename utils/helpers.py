def will_it_float(element):
    try:
        float(element)
        return True
    except ValueError:
        return False
