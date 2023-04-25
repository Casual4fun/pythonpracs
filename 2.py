class MealyError(Exception):
    pass


class raises:
    def __init__(self, exception):
        self.exception = exception
        self.exc_info = None

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            raise AssertionError("False")
        if not issubclass(exc_type, self.exception):
            return False
        self.exc_info = (exc_type, exc_val, exc_tb)
        return True


def func(a):
    if a == 0:
        raise MealyError("Empty")
    return None


try:
    with raises(MealyError) as e:
        func(0)
    print("all good")
except MealyError as e:
    assert 1 / 2 == 0
