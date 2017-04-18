import functools
import sys


def memoize(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tup = (args, tuple(kwargs.items()))
        if not hasattr(func, "dic"):
            func.dic = dict()
        if tup not in func.dic:
            func.dic[tup] = func(*args, **kwargs)
        return func.dic[tup]

    return wrapper

exec(sys.stdin.read())
