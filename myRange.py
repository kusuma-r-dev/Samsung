def myRange(start, stop=None, step=1):
    result = []

    if stop is None:
        stop = start
        start = 0

    if step == 0:
        raise ValueError("step cannot be zero")

    if step > 0:
        current = start
        while current < stop:
            result.append(current)
            current += step

    else:
        current = start
        while current > stop:
            result.append(current)
            current += step

    return result

print(myRange(1, 10, 2))