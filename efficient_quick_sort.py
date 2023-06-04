# 87940976
import random


def is_lt(a, b):
    if a[1] < b[1]:
        return True
    elif a[1] == b[1]:
        if a[2] > b[2]:
            return True
        elif a[2] == b[2]:
            if a[0] > b[0]:
                return True
    return False


def is_lg(a, b):
    if a[1] > b[1]:
        return True
    elif a[1] == b[1]:
        if a[2] < b[2]:
            return True
        elif a[2] == b[2]:
            if a[0] < b[0]:
                return True
    return False


def ef_q_sort(array, start, end):
    if start >= end:
        return
    left, right = start, end
    pivot = random.choice(array[start:end + 1])
    while left <= right:
        while is_lg(array[left], pivot):
            left += 1
        while is_lt(array[right], pivot):
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    ef_q_sort(array, start, right)
    ef_q_sort(array, left, end)


if __name__ == '__main__':
    n = int(input())
    sequence = [[int(col) if col.isdigit() else col for col in input().split()] for i in range(n)]
    ef_q_sort(sequence, 0, n - 1)
    sequence = [seq[0] for seq in sequence]
    print(*sequence, sep='\n')
