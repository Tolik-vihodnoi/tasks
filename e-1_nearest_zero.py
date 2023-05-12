# Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить, имеет длину n, то есть состоит из n одинаковых идущих подряд участков. Каждый участок либо пустой, либо на нём уже построен дом.
#
# Общительный Тимофей не хочет жить далеко от других людей на этой улице. Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого участка. Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.
#
# Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы. Дома в городе Тимофея нумеровались в том порядке, в котором строились, поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.
#
# Формат ввода
# В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). В следующей строке записаны n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули). Гарантируется, что в последовательности есть хотя бы один ноль. Номера домов (положительные числа) уникальны и не превосходят 109.
#
# Формат вывода
# Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их пробелами.
#
# 87155480

import sys
from typing import Optional


def distance_to_zero(_len: int, nums: list[str]) -> list[int]:
    result: list[Optional[int]] = [None] * _len
    nums_i: int = 0
    last_idx: int = _len - 1
    while nums_i < _len:
        if nums[nums_i] == '0':
            left: int = nums_i
            result[nums_i] = 0
            for seek_i in range(nums_i + 1, _len):
                if nums[seek_i] == '0':
                    right: int = seek_i
                    for i in range(0, (right - left) // 2 + 1):
                        result[left + i] = result[right - i] = i
                    while right < last_idx and nums[right + 1] == '0':
                        result[right + 1] = 0
                        right += 1
                    nums_i = right
                    break
            else:
                result[left:_len] = range(_len - left)
                return result
        else:
            for seek_i in range(nums_i + 1, _len):
                if nums[seek_i] == '0':
                    right: int = seek_i
                    result[0:right] = range(right, 0, -1)
                    nums_i = right
                    break
    return result


if __name__ == '__main__':
    _len: int = int(input())
    nums: list[str] = sys.stdin.readline().split()
    # Со старым принтом получилось 0.697сек 161.91Мб
    # print(' '.join(map(str, distance_to_zero(_len, nums))))
    #
    # С новым - 0.954сек 113.28Мб
    print(*distance_to_zero(_len, nums), sep=' ')
