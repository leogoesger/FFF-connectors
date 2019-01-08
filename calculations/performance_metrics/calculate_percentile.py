from numpy import nanpercentile, nanmax, nanmin


def calculate_percentile(matrix):
    result = []
    for row in matrix:
        row_fil = [i for i in row if i is not None]
        percentiles = {
            "min": nanmin(row_fil),
            "10th": nanpercentile(row_fil, 10),
            "25th": nanpercentile(row_fil, 25),
            "50th": nanpercentile(row_fil, 50),
            "75th": nanpercentile(row_fil, 75),
            "90th": nanpercentile(row_fil, 90),
            "max": nanmax(row_fil)
        }
        result.append(percentiles)
    return result
