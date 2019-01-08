def get_functional_rasters(rasters, number):
    functional_rasters = {}
    for key in rasters:
        functional_rasters[key] = raster_to_functional_raster(
            rasters[key], number)

    return functional_rasters


def raster_to_functional_raster(raster, number):
    return list(map(lambda raster_row: (
        [True if raster_col == number else False
         for raster_col in raster_row]),
        raster))
