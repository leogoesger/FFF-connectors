from datetime import datetime


def date_to_julian(date):
    return datetime.strptime(date, '%m/%d/%Y').timetuple().tm_yday


def date_to_offset_julian(date, offset_date):
    """Convert date to offset julian date

    Arguments:
        date {string} -- A string following "mm/dd/YYYY"
        offset_date {string} -- A string following "mm/dd"

    Returns:
        {number} -- Offset julian date
    """

    date_formatted = datetime.strptime(date, '%m/%d/%Y')
    offset_formatted = datetime.strptime(
        "{}/{}".format(offset_date, date_formatted.year), '%m/%d/%Y')

    days_in_year = 366 if offset_formatted.year % 4 == 0 else 365

    date_julian = date_formatted.timetuple().tm_yday
    offset_julian = offset_formatted.timetuple().tm_yday

    if date_julian >= offset_julian:
        return date_julian - offset_julian + 1
    else:
        return date_julian + days_in_year - offset_julian + 1


class TimeSeriesConversion:
    """Convert time series data to its matrix equvilant.

    Arguments:
        date_array {array} -- An array with date with the following format "mm/dd/yyyy"
        data_array {array} -- An array with data
        offset_date {string} -- A string following "mm/dd"

    """

    def __init__(self, date_array, data_array, offset_date="01/01"):
        self.date_array = date_array
        self.data_array = data_array
        self.offset_date = offset_date if offset_date else "01/01"
        self.julian_date_array = []

        self.start_year = None
        self.end_year = None
        self.final_matrix = None

        self.get_empty_matrix()
        self.populate()

    def get_year_limits(self):
        """Assign year limits which accounts for leap year at either end
        """

        d1 = datetime.strptime(self.date_array[0], '%m/%d/%Y')
        d_end = datetime.strptime(self.date_array[-1], '%m/%d/%Y')
        d_off_1 = datetime.strptime(
            "{}/{}".format(self.offset_date, d1.year), '%m/%d/%Y')
        d_off_end = datetime.strptime(
            "{}/{}".format(self.offset_date, d_end.year), '%m/%d/%Y')

        self.start_year = d1.year if d1 >= d_off_1 else d1.year - 1
        self.end_year = d_end.year if d_end >= d_off_end else d_end.year - 1

    def get_empty_matrix(self):
        """Create an empty matrix with fixed size using start year/end year
        """
        if not self.start_year:
            self.get_year_limits()
        self.final_matrix = [[None for y in range(
            self.end_year - self.start_year + 1)] for x in range(366)]

    def get_position_index(self, date):
        """[summary]

        Arguments:
            date {[string]} -- string of a date with format mm/dd/yyyy

        Returns:
            [number, number] -- index of row, column
        """

        if not self.start_year:
            self.get_year_limits()

        d_f = datetime.strptime(date, '%m/%d/%Y')
        offset_f = datetime.strptime(
            "{}/{}".format(self.offset_date, d_f.year), '%m/%d/%Y')

        column_index = d_f.year - \
            self.start_year if d_f >= offset_f else d_f.year - self.start_year - 1
        # 01/01 is day 1, so '-1' will give the index of array
        row_index = date_to_offset_julian(date, self.offset_date) - 1

        return row_index, column_index

    def populate(self):
        """Populate matrix with data
        """
        for index, d in enumerate(self.date_array):
            r_i, c_i = self.get_position_index(d)

            self.final_matrix[r_i][c_i] = self.data_array[index]
