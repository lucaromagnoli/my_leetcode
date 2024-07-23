def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


def combinations_recursive(array, k):
    if k == 0:
        return [[]]
    if not array:
        return []
    result = []
    for i in range(len(array)):
        # Get combinations of the remaining elements
        for combo in combinations_recursive(array[i + 1 :], k - 1):
            result.append([array[i]] + combo)
    return result


r = combinations_recursive([1, 2, 3, 4, 5], 2)
print(r)


def recursive_list(array, n):
    if n == 0:
        return array
    results = []
    for i in range(len(array)):
        for result in recursive_list(array[i + 1 :], n - 1):
            results.append(result + array[i])
    return results


def traverse_nested(nested):
    for k, v in nested.items():
        if isinstance(v, dict):
            yield from traverse_nested(v)
        else:
            yield v


nested_dict = {
    "key": {
        "sub_key": {
            "sub_sub_key_1": "value1",
            "sub_sub_key_2": "value2",
        }
    }
}


def lex_gen(bounds):
    elem = [0] * len(bounds)
    while True:
        yield elem
        i = 0
        while elem[i] == bounds[i] - 1:
            elem[i] = 0
            i += 1
            if i == len(bounds):
                return
        elem[i] += 1


def cart_product(lists):
    bounds = [len(lst) for lst in lists]
    for elem in lex_gen(bounds):
        yield [lists[i][elem[i]] for i in range(len(lists))]


# for k in cart_product([['1', '2'], ['x', 'y'], ['a', 'b', 'c']]):
#     print(k)
