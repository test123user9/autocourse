class InvalidRewardValueError(Exception):
    def __init__(self, error):
        self.error = error

class TheSameStudentError(Exception):
    pass