import time


def timer(fn):
    def wrapper(*args, **kwargs):
        start = time.monotonic()
        result = fn(*args, **kwargs)
        finish = time.monotonic() - start
        print(f"{fn.__name__} - {finish}")
        return result
    return wrapper


def review_timing_logs(logs: str):
    rows = logs.split('\n')
    cells = [row.split(' - ') for row in rows]
    cells = [[i[0], float(i[1])] for i in cells]
    cells.sort(key=lambda x: x[1], reverse=True)
    return cells
