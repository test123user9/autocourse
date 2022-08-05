def vacation_title(func):
    def wrapper(*args, **kwargs):
        print()
        print('CEO Red Bull Inc.')
        print('Mr. John Bigbull')
        func(*args, **kwargs)
    return wrapper

