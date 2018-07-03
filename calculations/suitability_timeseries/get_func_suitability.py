# Given an array with [date, flow value]
# condition one is the flow value is less than flow_bin[0]
# condition two is the flow value is greater than flow_bin[-1]
# ...rest


def get_func_suitability(interpolation, key, row, flow_bins):
     # row is an array with date and flow value
    new_array = []
    for perc_func in interpolation[key]:
        if float(row[1]) < flow_bins[key][0]:  # if the value is below 0 from ip func
            new_array.append(round(perc_func(flow_bins[key][0]).tolist(), 6))
        # if value is greater than max(flow_bin)
        elif float(row[1]) > flow_bins[key][-1]:
            new_array.append(
                round(perc_func(flow_bins[key][-1]).tolist(), 6))
        else:
            new_array.append(round(perc_func(row[1]).tolist(), 6))

    return new_array
