def vacation_type_header(func):
    def wrapper(arg, v_type, f_date, t_date):
        print(f'Vacation type: {v_type}')
        func(arg, v_type, f_date, t_date)
    return wrapper


def vacation_title(func):
    def wrapper(*args, **kwargs):
        print('CEO Red Bull Inc.')
        print('Mr. John Bigbull')
        print()
        func(*args, **kwargs)
    return wrapper

