#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random as rnd


def create(length, max_value):
    unique_numbers = list(range(max_value))
    rnd.shuffle(unique_numbers)
    return unique_numbers[:length]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        middle = len(arr) // 2
        left, inv_left = merge_sort(arr[:middle])
        right, inv_right = merge_sort(arr[middle:])
        merged, inv_merge = merge(left, right)
        return merged, inv_left + inv_right + inv_merge

def merge(left, right):
    merged = []
    inv_count = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged, inv_count


if __name__ == '__main__':
    array = create(5, 100)
    # array = [5, 4, 3, 2, 1, 6, 7, 8]
    print("Array =", array)
    _, count = merge_sort(array)
    print("Количество инверсий в массиве =", count)
