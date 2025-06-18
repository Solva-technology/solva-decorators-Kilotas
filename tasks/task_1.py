from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(map(str, args))
        kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        args_kwargs_str = (
            f"{args_str}{', ' if args_str and kwargs_str else ''}{kwargs_str}"
        )
        print(f"Вызов: {func.__name__}({args_kwargs_str})")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result

    return wrapper
