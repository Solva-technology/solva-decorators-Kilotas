from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        all_args = ", ".join(map(str, args))
        print(f"Вызов: {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result

    return wrapper


@log
def add(a, b):
    return a + b


print(add(2, 3))
