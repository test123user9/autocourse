from datetime import date

from Homework_13.decorators import vacation_title, vacation_type_header
from Homework_13.exceptions import InvalidDatePeriod, InvalidFromDate, InvalidVacationTypeValueError


class Worker:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    @vacation_title
    @vacation_type_header
    def vacation_request_pattern(self, vacation_type: str, from_date: date = date.today(), to_date: date = date.today()):
        """
        The function prints vacation request depending on vacation type and from/to dates

        :param vacation_type: Vacation type in type str. Allowed values: vacation, sick leave, day off
        :param from_date: the first vacation day in type date(yyyy, mm, dd)
        :param to_date: the last vacation day in type date(yyyy, mm, dd)
        :return: None
        """
        v_list = ['vacation', 'sick leave', 'day off']
        if from_date > to_date:
            raise InvalidDatePeriod(from_date)
        if from_date < date.today():
            raise InvalidFromDate(from_date)
        if vacation_type not in v_list:
            raise InvalidVacationTypeValueError(vacation_type)

        if from_date != to_date:
            print(f'Hi John, I need the paid {vacation_type} from {from_date} to {to_date}. {self.name} {self.surname}')
        else:
            print(f'Hi John, I need 1 day of the paid {vacation_type} at {from_date}. {self.name} {self.surname}')


