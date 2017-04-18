import functools
import sys
import time


def takes(*types):
    def decorator(func):
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            tup = args + tuple(kwargs)
            length1 = len(types)
            length2 = len(tup)
            for i in range(min(length1, length2)):
                # print(types[i])
                if not isinstance(tup[i], types[i]):
                    raise TypeError
            result = func(*args, **kwargs)
            return result
        return decorated
    return decorator


exec(sys.stdin.read())


'''@takes(int, int)
def sum(a, b=None):
    if b is None:
        b = a
    return a + b


print(sum(1, 1))
print(sum(1))'''
