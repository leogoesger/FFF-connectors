def reclassify_raster(original_raster, binning):
    return (list
            (map(lambda row: [map_column_to_binning(col, binning) for col in row],
                 original_raster
                 ))
            )


def map_column_to_binning(col, binning):
    # [1.2, 1.5, 2] -> 4 bins: [-inf, ~1.2], [1.2, ~1.5], [1.5, ~2], [2, +inf]
    if col >= binning[-1]:
        return len(binning)
    else:
        for index in range(0, len(binning)):
            if col < binning[index]:
                return index
