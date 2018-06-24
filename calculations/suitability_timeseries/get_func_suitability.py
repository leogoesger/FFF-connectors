def get_func_suitability(interpolation, key, row, flow_bins):
    new_array = []
    for perc_func in interpolation[key]:
        ele = perc_func(float(row[1])).tolist()
        if ele < 0:  # if the value is below 0 from ip func
            new_array.append(0)
        # if value is greater than max(flow_bin)
        elif float(row[1]) > flow_bins[key][-1]:
            new_array.append(
                round(perc_func(flow_bins[key][-1]).tolist(), 2))
        else:
            new_array.append(round(ele, 2))
    return new_array
