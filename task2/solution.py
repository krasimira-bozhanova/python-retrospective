from collections import OrderedDict


def groupby(func, seq):
    dictionary = {}
    for x in seq:
        dictionary.setdefault(func(x), []).append(x)
    return dictionary


def iterate(func):
    def generate_func(iter_func):
        return lambda x: func(iter_func(x))

    iter_func = lambda x: x
    while True:
        yield iter_func
        iter_func = generate_func(iter_func)


def zip_with(func, *iterables):
    if iterables:
        for x in zip(*iterables):
            yield func(*x)
           

def cache(func, cache_size):
    cache_dict = OrderedDict()

    def cache_memory(*args):
        if args in cache_dict:
            return cache_dict[args]
        first_func_call = func(*args)
        if cache_size:  
            if len(cache_dict) >= cache_size:
                cache_dict.popitem(last=False)
            cache_dict[args] = first_func_call
        return first_func_call
        
    return cache_memory
