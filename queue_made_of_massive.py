# Астрологи объявили день очередей ограниченного размера. Тимофею нужно написать класс MyQueueSized, который принимает параметр max_size, означающий максимально допустимое количество элементов в очереди.
#
# Помогите ему —– реализуйте программу, которая будет эмулировать работу такой очереди. Функции, которые надо поддержать, описаны в формате ввода.
#
# Формат ввода
# В первой строке записано одно число — количество команд, оно не превосходит 5000.
# Во второй строке задан максимально допустимый размер очереди, он не превосходит 5000.
# Далее идут команды по одной на строке. Команды могут быть следующих видов:
#
# push(x) — добавить число x в очередь;
# pop() — удалить число из очереди и вывести на печать;
# peek() — напечатать первое число в очереди;
# size() — вернуть размер очереди;
# При превышении допустимого размера очереди нужно вывести «error». При вызове операций pop() или peek() для пустой очереди нужно вывести «None».
# Формат вывода
# Напечатайте результаты выполнения нужных команд, по одному на строке.

from typing import Optional

from dataclasses import dataclass, field

num_of_com = int(input())
max_q = int(input())
commands = []
for i in range(num_of_com):
    commands.append(input().split())


@dataclass
class MyQueueSized:
    max_q: int
    size_val: int = 0
    head: int = 0
    tale: int = 0
    queue: list[Optional[int]] = field(default_factory=lambda: [None] * max_q)

    def push(self, item):
        if self.size_val == self.max_q:
            return 'error'
        self.queue[self.tale] = item
        self.tale = (self.tale + 1) % max_q
        self.size_val += 1
        return None

    def pop(self):
        if self.size_val == 0:
            return None
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_q
        self.size_val -= 1
        return item

    def peek(self):
        if self.size_val == 0:
            return None
        return self.queue[self.head]

    def size(self):
        return self.size_val


q = MyQueueSized(max_q)
for command in commands:
    if command[0] == 'push':
        res = q.push(command[1])
        if res != None:
            print(res)
    elif command[0] == 'pop':
        print(q.pop())
    elif command[0] == 'peek':
        print(q.peek())
    else:
        print(q.size())
