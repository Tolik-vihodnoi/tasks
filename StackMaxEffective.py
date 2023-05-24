# Реализуйте класс StackMaxEffective, поддерживающий операцию определения максимума среди элементов в стеке.
# Сложность операции должна быть O(1). Для пустого стека операция должна возвращать None. При этом push(x) и pop()
# также должны выполняться за константное время.
#
# Формат ввода
# В первой строке записано одно число — количество команд, оно не превосходит 100000. Далее идут команды по одной в строке.
# Команды могут быть следующих видов:
#
# push(x) — добавить число x в стек;
# pop() — удалить число с вершины стека;
# get_max() — напечатать максимальное число в стеке;
# Если стек пуст, при вызове команды get_max нужно напечатать «None», для команды pop — «error».
# Формат вывода
# Для каждой команды get_max() напечатайте результат её выполнения. Если стек пустой, для команды get_max() напечатайте «None».
# Если происходит удаление из пустого стека — напечатайте «error».


class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_stack = []

    def push(self, item):
        self.items.append(item)
        if not self.max_stack or item >= self.max_stack[-1]:
            self.max_stack.append(item)

    def pop(self):
        if not self.items:
            return "error"
        item = self.items.pop()
        if item == self.max_stack[-1]:
            self.max_stack.pop()

    def get_max(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]

num_of_com = int(input())
commands = []
for i in range(num_of_com):
    commands.append(input().split())

q = StackMaxEffective()
for command in commands:
    if command[0] == 'push':
        q.push(int(command[1]))
    elif command[0] == 'pop':
        val = q.pop()
        if val is not None:
            print(val)
    else:
        print(q.get_max())
