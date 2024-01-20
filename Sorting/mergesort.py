def mergesort(b_array, c_array, a_array):
    b_len, c_len, a_len = len(b_array), len(c_array), len(a_array)
    b, c, a = 0, 0, 0
    while b < b_len and c < c_len:
        if b_array[b] >= c_array[c]:
            a_array[a] = c_array[c]
            a, c = a + 1, c + 1
        else:
            a_array[a] = b_array[b]
            a, b = a + 1, b + 1
    if b == b_len:
        a_array[a:] = c_array[c:]
    else:
        a_array[a:] = b_array[b:]
    return a_array


def merge(a_array, a_len):
    if a_len > 1:
        b_array = [i for i in a_array[:a_len // 2]]
        c_array = [i for i in a_array[a_len // 2:]]
        merge(b_array, len(b_array))
        merge(c_array, len(c_array))
        mergesort(b_array, c_array, a_array)
    return a_array


if __name__ == '__main__':
    array = [1, 5, 2, 6, 3, 7, 4, 8, 9]
    print(merge(array, len(array)))
