import functools
import sys
import time


def profiler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if sys._getframe().f_back.f_code.co_name != func.__name__:
            wrapper.calls = 0
        wrapper.calls += 1
        time_start = time.time()
        result = func(*args, **kwargs)
        wrapper.last_time_taken = time.time() - time_start
        return result

    wrapper.calls = 0
    return wrapper


exec(sys.stdin.read())

'''@profiler
def task():
    pass


task()
print(task.calls)
'''
