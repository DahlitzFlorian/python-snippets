from collections.abc import Iterable


def flatten(input_arr, output_arr=None):
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
        if isinstance(ele, Iterable):
            flatten(ele, output_arr)  # tail-recursion
        else:
            output_arr.append(ele)  # produce the result

    return output_arr


sample_list = [1, [2], [[3, 4], 5], 6]
print(flatten(sample_list))
