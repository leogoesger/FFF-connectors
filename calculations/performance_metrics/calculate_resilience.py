import datetime
from utils.time_series_conversion import date_to_offset_julian


def get_comparision_array(matrix, limits, inputs):
    """Compare senario with optimal, and get an array of difference if any

    Arguments:
      matrix {[type]} -- [description]
      limits {[lower_limit, upper_limit]} -- [description]
      inputs {[type]} -- [description]

    Returns:
      [number] -- array of difference
    """

    lower_limit = limits['lower_limit']
    upper_limit = limits['upper_limit']

    start_indx = date_to_offset_julian(
        inputs["bioperiod_start_date"]+"/2000", "10/01") - 1
    end_indx = date_to_offset_julian(
        inputs["bioperiod_end_date"]+"/2000", "10/01") - 1

    scenario = matrix['scenario']
    percentile = matrix['percentile']

    sorting_ary = []

    for i in range(start_indx, end_indx + 1):
        lower_diff = float(scenario[i]) - float(percentile[i][lower_limit])
        upper_diff = float(scenario[i]) - float(percentile[i][upper_limit])

        if lower_diff < 0:
            sorting_ary.append(abs(lower_diff))
        elif upper_diff > 0:
            sorting_ary.append(abs(upper_diff))
        else:
            sorting_ary.append(0)

    return sorting_ary


def get_recorvery_days(array):
    """count plus by one any time a number isn't a zero is followed by a number is zero

    Arguments:
      array {[number]} -- [array of numbers]

    Returns:
      [number] -- count
    """

    count = 0
    for index, ele in enumerate(array):
        if index != len(array) - 1 and ele != 0 and array[index + 1] == 0:
            count = count + 1

    return count


def get_deficit_days(array):
    """count plus by one any time a number isn't a zero

    Arguments:
      array {[number]} -- [array of numbers]

    Returns:
      [number] -- count
    """

    count = 0
    for ele in array:
        if ele != 0:
            count = count + 1

    return count
