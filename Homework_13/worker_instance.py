from datetime import date

from Homework_13.worker import Worker

vacation_type_list = ['vacation', 'sick leave', 'day off']

worker1 = Worker('Sam', 'Andersen')
worker1.vacation_request_pattern(vacation_type_list[0], date(2022, 11, 11), date(2022, 12, 11))

print('*' * 80)

worker2 = Worker('Alex', 'Ander')
worker2.vacation_request_pattern(vacation_type_list[1], date(2022, 11, 11), date(2022, 11, 11))

print('*' * 80)

worker3 = Worker('Lina', 'Pitt')
worker3.vacation_request_pattern('day off', date(2022, 12, 11), date(2022, 12, 20))

