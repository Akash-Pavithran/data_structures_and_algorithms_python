from utils import time_it

@time_it
def linear_search(numbers_list, number_to_find):
    for index, number in enumerate(numbers_list):
        if number == number_to_find:
            return index
    return -1


@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_element = numbers_list[mid_index]

        if mid_element == number_to_find:
            return mid_index

        if mid_element < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1

if __name__ == '__main__':
    numbers_list = [i for i in range(1000000)]
    number_to_find = 1000000

    index = linear_search(numbers_list, number_to_find)
    index = binary_search(numbers_list, number_to_find)