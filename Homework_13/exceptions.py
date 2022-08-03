class InvalidVacationTypeValueError(Exception):
    def __init__(self, error):
        self.error = error
        print('Available values: vacation/sick leave/day off')

class InvalidDatePeriod(Exception):
    def __init__(self, error):
        self.error = error
        print('from_date can\'t be later than to_date')

class InvalidFromDate(Exception):
    def __init__(self, error):
        self.error = error
        print('from_date can\'t be in the past')

