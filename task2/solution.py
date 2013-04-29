from collections import OrderedDict


def groupby(func, seq):
    dictionary = {}
    for args in seq:
        dictionary.setdefault(func(args), []).append(args)
    return dictionary


def iterate(func):
    def generate_func(iter_func):
        return lambda x: func(iter_func(x))

    iter_func = lambda x: x
    while True:
        yield iter_func
        iter_func = generate_func(iter_func)


def zip_with(func, *iterables):
    return (func(*args) for args in zip(*iterables))


def cache(func, cache_size):

    if cache_size <= 0:
        return func

    cache_dict = OrderedDict()

    def cache_memory(*args):
        if args not in cache_dict:
            if len(cache_dict) >= cache_size:
                cache_dict.popitem(False)
            cache_dict[args] = func(*args)
        return cache_dict[args]

    return cache_memory
