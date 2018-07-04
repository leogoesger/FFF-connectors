from utils.helpers import flatten_list


def combine_functional_rasters(raster_collection, spatial_boundary, conditional_relationship):
    # Given conditional functions and spatial boundary, combine function first flatten all nested
    # arrays, and then compare values at the same position with `and`.
    # Returned value is a dictionary with keys `{}_{}_XX_{}`, where XX is fixed to be unknown

    keys = list(raster_collection[0].keys())
    combined_rasters = {}

    for key in keys:
        combined_key = '{}_X_{}'.format(
            key[:4],
            spatial_boundary
        )
        combined_rasters[combined_key] = None

        for raster in raster_collection:
            current_key = combined_key.replace(
                'X', next(iter(raster))[5])  # replace X with the hydro_var
            # at first conditional function
            flat_list = flatten_list(raster[current_key])
            if not combined_rasters[combined_key]:
                combined_rasters[combined_key] = flat_list
            else:  # for all other conditional function, zip them to determine true or false
                combined_rasters[combined_key] = zip_and_compare(
                    combined_rasters[combined_key], flat_list, conditional_relationship)

    return combined_rasters


def zip_and_compare(list_a, list_b, relation):
    if (relation == 'All'):
        return [a and b for a, b in zip(list_a, list_b)]
    else:
        return [a or b for a, b in zip(list_a, list_b)]
