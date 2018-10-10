def calculate_binning(num, bins):
    belongs_to = None
    for index, b in enumerate(bins):
        if num <= b:
            belongs_to = index

    if not belongs_to:
        belongs_to = len(bins)

    return belongs_to


def get_binings_array(data_array, bins):
    binnings = []
    for num in data_array:
        binnings.append(calculate_binning(num, bins))
    return binnings
