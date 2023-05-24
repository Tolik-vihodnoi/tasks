#id 87593164

req_actions = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: b - a,
    '*': lambda a, b: a * b,
    '/': lambda a, b: b // a
}


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.__items:
            raise IndexError('Stack is empty')
        return self.__items.pop()


def pol_notation(items: list[str]) -> int:
    stack = Stack()
    for item in items:
        if item[-1].isdigit():
            stack.push(item)
        else:
            stack.push(req_actions[item](int(stack.pop()), int(stack.pop())))
    return stack.pop()


if __name__ == '__main__':
    items: list[str] = input().split()
    print(pol_notation(items))
