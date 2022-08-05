from datetime import date

from Homework_13.decorators import vacation_title
from Homework_13.exceptions import InvalidDatePeriod, InvalidFromDate, InvalidVacationTypeValueError, InvalidValueRange


class Worker:
    def __init__(self):
        self.name = input('Input name: ')
        self.surname = input('Input surname: ')

    @vacation_title
    def print_request(self, message):
        print()
        print(message)

    def vacation_request(self):
        """
        The function prints vacation request depending on vacation type and from/to dates

        :return: None
        """
        print("Please choose your vacation type:")
        options = ('vacation', 'sick leave', 'day off')
        for _, elem in enumerate(options):
            print("{} {}".format(_ + 1, elem))
        i = int(input("Enter number 1, 2 or 3: "))
        if i < 0 or i > 3:
            raise InvalidValueRange(i)
        year = int(input('Input "from" year: '))
        month = int(input('Input "from"  month: '))
        day = int(input('Input "from" day: '))
        from_date = date(year, month, day)
        year = int(input('Input "to" year: '))
        month = int(input('Input "to" month: '))
        day = int(input('Input "to" day: '))
        to_date = date(year, month, day)

        if from_date > to_date:
            raise InvalidDatePeriod(from_date)
        if from_date < date.today():
            raise InvalidFromDate(from_date)


        if from_date == to_date:
            self.print_request(f'Hi John, I need 1 day of the paid {options[i-1]} at {from_date}. {self.name} {self.surname}')
        else:
            self.print_request(f'Hi John, I need the paid {options[i-1]} from {from_date} to {to_date}. {self.name} {self.surname}')



