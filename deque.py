#id 87596791

class FullDeque(Exception):
    """Дек переполнена."""


class EmptyDeque(Exception):
    """Дек пуста."""


class Deque:
    """Double ended queue."""
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__size = 0
        self.__head = 0
        self.__tale = 0
        self.__deque = [None] * self.__max_size

    def push_back(self, value):
        if self.__size == self.__max_size:
            raise FullDeque(FullDeque.__doc__)
        self.__deque[self.__tale] = value
        self.__tale = (self.__tale + 1) % self.__max_size
        self.__size += 1

    def push_front(self, value):
        if self.__size == self.__max_size:
            raise FullDeque(FullDeque.__doc__)
        self.__head = (self.__head - 1) % self.__max_size
        self.__deque[self.__head] = value
        self.__size += 1

    def pop_front(self):
        if self.__size == 0:
            raise EmptyDeque(EmptyDeque.__doc__)
        res = self.__deque[self.__head]
        self.__deque[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_size
        self.__size -= 1
        return res

    def pop_back(self):
        if self.__size == 0:
            raise EmptyDeque(EmptyDeque.__doc__)
        self.__tale = (self.__tale - 1) % self.__max_size
        res = self.__deque[self.__tale]
        self.__deque[self.__tale] = None
        self.__size -= 1
        return res


def main(num_of_com: int, deque: Deque) -> None:
    for i in range(num_of_com):
        command, *arg = input().split()
        try:
            res = getattr(deque, command)(*arg)
            if res is not None:
                print(res)
        except (FullDeque, EmptyDeque):
            print('error')
    return


if __name__ == '__main__':
    num_of_com = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    main(num_of_com, deque)
