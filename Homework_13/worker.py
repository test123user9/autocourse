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
        if from_date > to_date:
            raise InvalidDatePeriod(from_date)
        if from_date < date.today():
            raise InvalidFromDate(from_date)

        if from_date == to_date:
            print(f'Hi John, I need 1 day of the paid {vacation_type} at {from_date}. {self.name} {self.surname}')
        elif vacation_type == 'vacation':
            print(f'Hi John, I need the paid {vacation_type} from {from_date} to {to_date}. {self.name} {self.surname}')
        elif vacation_type == 'sick leave':
            print(f'Hi John, I need the paid {vacation_type} from {from_date} to {to_date}. {self.name} {self.surname}')
        elif vacation_type == 'day off':
            print(f'Hi John,I need the paid {vacation_type} from {from_date} to {to_date}. {self.name} {self.surname}')
        else:
            raise InvalidVacationTypeValueError(vacation_type)

