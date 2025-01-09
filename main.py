import timeit
from insertion_sort import insertion_sort
from merge_sort import merge_sort

test_list = list(reversed(range(10000)))


def test_sort_performance(fn_name, need_import=True):
    time = timeit.timeit(
        f"{fn_name}(test_list)",
        setup=(
            f"from __main__ import {fn_name}, test_list"
            if need_import
            else "from __main__ import test_list"
        ),
        number=1,
    )
    return time


def main():
    fastest_time = None
    fastest_fn = None

    for fn in [insertion_sort, merge_sort, sorted]:
        fn_name = fn.__name__
        time = test_sort_performance(fn_name, need_import=fn_name != "sorted")
        print(f"{fn_name} time: {time}")
        if not fastest_time or time < fastest_time:
            fastest_time = time
            fastest_fn = fn_name

    print(f"Fastest is {fastest_fn} with time {fastest_time} for n=10000 elements")


if __name__ == "__main__":
    main()
