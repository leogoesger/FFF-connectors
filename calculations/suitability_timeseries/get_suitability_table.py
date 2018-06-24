def get_suitability_table(csv_arrays, flow_bins):
    arr = []
    for _ in range(len(csv_arrays[0]) - 1):
        arr.append({})
        for key in flow_bins:
            arr[-1][key[:2]] = [None for i in flow_bins[key]]

    # Fill in the data
    for block in csv_arrays:
        for index, el in enumerate(block):
            if index > 0:
                func_num = index-1
                key = block[0][:2]  # 'T6_4' -> 'T6'
                velocity = int(block[0][-1]) - 1  # 'T6_4' -> '4'
                arr[func_num][key][velocity] = float(el)
    return arr
