from functools import wraps

ZERO = 0


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= ZERO:
                raise ValueError("Все аргументы должны быть положительными")

        for value in kwargs.values():
            if isinstance(arg, (int, float) and arg <= ZERO):
                raise ValueError("Все аргументы должны быть положительными")

        result = func(*args, **kwargs)
        return result

    return wrapper
