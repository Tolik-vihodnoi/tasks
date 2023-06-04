s = input()
t = input()
y = 0
for i in s:
    x = t.find(i, y, len(t))
    if x == -1:
        print(False)
        break
    y = x + 1
else:
    print(True)

# Пример 1
# Ввод	         Вывод
# abc            True
# ahbgdcu


# Пример 2
# Ввод	         Вывод
# abcp           False
# ahpc
