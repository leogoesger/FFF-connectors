from utils.helpers import flatten_list


def combine_functional_rasters(conditional_function_collection, spatial_boundary):
    # Given conditional functions and spatial boundary, combine function first flatten all nested
    # arrays, and then compare values at the same position with `and`.
    # Returned value is a dictionary with keys `{}_{}_x_{}`, where x is fixed to be unknown

    keys = list(conditional_function_collection[0].functional_rasters.keys())
    combined_rasters = {}

    for key in keys:
        combined_key = '{}_x_{}'.format(
            key[:3],
            spatial_boundary
        )
        combined_rasters[combined_key] = None

        for conditional_function in conditional_function_collection:
            current_key = '{}_{}_{}'.format(
                key[:3],
                conditional_function.hydrologic_variable,
                conditional_function.spatial_bounding
            )
            # at first conditional function
            flat_list = flatten_list(
                conditional_function.functional_rasters[current_key])
            if not combined_rasters[combined_key]:
                combined_rasters[combined_key] = flat_list
            else:  # for all other conditional function, zip them to determine true or false
                combined_rasters[combined_key] = zip_and_compare(
                    combined_rasters[combined_key], flat_list)

    return combined_rasters


def zip_and_compare(list_a, list_b):
    return [a and b for a, b in zip(list_a, list_b)]
