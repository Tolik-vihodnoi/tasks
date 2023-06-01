
# Любимый вариант очереди Тимофея — очередь, написанная с использованием связного списка. Помогите ему с реализацией. Очередь должна поддерживать выполнение трёх команд:
#
# get() — вывести элемент, находящийся в голове очереди, и удалить его. Если очередь пуста, то вывести «error».
# put(x) — добавить число x в очередь
# size() — вывести текущий размер очереди
# Формат ввода
# В первой строке записано количество команд n — целое число, не превосходящее 1000. В каждой из следующих n строк записаны команды по одной строке.


from typing import Optional, Type

from dataclasses import dataclass


@dataclass
class Node:
    value: Optional[int] = None
    next: Optional[Type] = None


class LinkedList:

    def __init__(self):
        self.head: Optional[Type] = None

    def add(self, data):
        new_node: Type = Node(data)
        if not self.head:
            self.head = new_node
            return
        current_node: Type = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node


class LinkedQueue:

    def __init__(self):
        self.queue: LinkedList = LinkedList()
        self.size_of: int = 0

    def get(self):
        if self.size_of == 0:
            return 'error'
        res = self.queue.head.value
        self.queue.head = self.queue.head.next
        self.size_of -= 1
        return res

    def put(self, item):
        self.queue.add(item)
        self.size_of += 1
        return

    def size(self):
        return self.size_of

num_of_com = int(input())
commands = []
for i in range(num_of_com):
    commands.append(input().split())

q = LinkedQueue()
for command in commands:
    if command[0] == 'put':
        q.put(command[1])
    elif command[0] == 'get':
        print(q.get())
    else:
        print(q.size())
