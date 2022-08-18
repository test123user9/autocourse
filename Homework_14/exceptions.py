class NotEnoughMoney(Exception):
    def __init__(self, error):
        self.error = error


