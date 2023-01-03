def char_range(start, stop, step=1):
    start_code = ord(start)
    stop_code = ord(stop)

    if start_code > stop+code:
        step *= -1

    
    for value in range(start_code, stop_code + 1, step):
        yield chr(value)

from inspect import isgeneratorfunction


assert isgeneratorfunction(
    char_range
), f"Expected char_range to be a generator function but was not."
