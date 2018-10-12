get_year_limits_suit = [
    {
        "test_name": "Happy path",
        "date_array": ["10/01/2001", "10/02/2001"],
        "data_array": [1, 2],
        "offset_date": "10/01",
        "start_year": 2001,
        "end_year": 2001,
    },
    {
        "test_name": "Before offset date - start",
        "date_array": ["09/01/2001", "10/02/2001"],
        "data_array": [1, 2],
        "offset_date": "10/01",
        "start_year": 2000,
        "end_year": 2001,
    },
    {
        "test_name": "Before offset date - start/end",
        "date_array": ["09/01/2001", "09/30/2001"],
        "data_array": [1, 2],
        "offset_date": "10/01",
        "start_year": 2000,
        "end_year": 2000,
    },
    {
        "test_name": "Leap year - start",
        "date_array": ["10/01/2000", "10/02/2001"],
        "data_array": [1, 2],
        "offset_date": "10/01",
        "start_year": 2000,
        "end_year": 2001,
    },
    {
        "test_name": "Leap year - end",
        "date_array": ["10/01/2001", "10/01/2004"],
        "data_array": [1, 2],
        "offset_date": "10/01",
        "start_year": 2001,
        "end_year": 2004,
    },
    {
        "test_name": "On offset date - start/end",
        "date_array": ["10/01/2001", "10/01/2002"],
        "data_array": [1, 2],
        "offset_date": "10/01",
        "start_year": 2001,
        "end_year": 2002,
    },
    {
        "test_name": "No offset date - start/end",
        "date_array": ["10/01/2001", "10/01/2002"],
        "data_array": [1, 2],
        "offset_date": None,
        "start_year": 2001,
        "end_year": 2002,
    },
    {
        "test_name": "No offset date - start/end",
        "date_array": ["10/01/2001", "01/01/2002"],
        "data_array": [1, 2],
        "offset_date": None,
        "start_year": 2001,
        "end_year": 2002,
    },
]

get_empty_matrix_suit = [
    {
        "test_name": "Happy path",
        "date_array": ["10/01/2001", "10/02/2001"],
        "data_array": [1, 2],
        "offset_date": "10/01",
        "sol": [[None] for i in range(366)],
    },
    {
        "test_name": "Before offset - end",
        "date_array": ["10/01/2001", "09/20/2002"],
        "data_array": [1, 2],
        "offset_date": "10/01",
        "sol": [[None] for i in range(366)],
    },
    {
        "test_name": "Before offset - start/end",
        "date_array": ["09/20/2001", "09/20/2002"],
        "data_array": [1, 2],
        "offset_date": "10/01",
        "sol": [[None, None] for i in range(366)],
    },
    {
        "test_name": "Leap year/Before Offset - start",
        "date_array": ["09/30/2000", "09/20/2001"],
        "data_array": [1, 2],
        "offset_date": "10/01",
        "sol": [[None, None] for i in range(366)],
    },
    {
        "test_name": "Leap year - start",
        "date_array": ["10/01/2000", "09/20/2001"],
        "data_array": [1, 2],
        "offset_date": "10/01",
        "sol": [[None] for i in range(366)],
    },
]

# row index is number of the date - 1, 94 is the 95th day of the year, which is located at 94th column
get_position_index_suit = [
    {
        "test_name": "Happy path",
        "date_array": ["10/01/2000", "01/01/2001", "01/01/2002"],
        "data_array": [1, 2, 3],
        "offset_date": "01/01",
        "dates": ["01/03/2001", "01/01/2002", "10/01/2001", "10/01/2000"],
        "sol": [{"r": 2, "c": 1}, {"r": 0, "c": 2}, {"r": 273, "c": 1}, {"r": 274, "c": 0}],
    },
    {
        "test_name": "10/01 offset Date",
        "date_array": ["10/01/2000", "01/01/2001", "01/01/2002"],
        "data_array": [1, 2, 3],
        "offset_date": "10/01",
        "dates": ["01/03/2001", "01/01/2002", "10/01/2001", "10/01/2000"],
        "sol": [{"r": 94, "c": 0}, {"r": 92, "c": 1}, {"r": 0, "c": 1}, {"r": 0, "c": 0}],
    },
]
