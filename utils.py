import timeit
from typing import Union, Callable


def pretty_timeit(
    stmt: Union[str, Callable],
    loops: int = 10000,
    repeat: int = 10,
    setup: str = "pass",
    globals : dict = None,
    format : str = ".2f"
) -> str:
    """
    Time a code snippet and return a formatted string with the results.

    Args:
    stmt: A string of code to be timed or a callable object.
    loops: Number of times to execute the code per measurement.
    repeat: Number of times to repeat the measurement.
    setup: A string of code to execute before timing (for imports, etc.).

    Returns:
    A formatted string with timing results.
    """
    results = timeit.repeat(stmt, setup=setup, number=loops, repeat=repeat, globals=globals)
    best_time = min(results)
    usec = best_time * 1e6 / loops

    return f"{loops} loops, best of {repeat}: {usec: {format}} usec per loop"