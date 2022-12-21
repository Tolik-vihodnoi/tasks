a = "3aabacbebebe"
n = int(a[0])
listik = list()
setik = set()
word = str()
index_last_letter = len(a) - 1
for i in range(1, len(a)):
    index = i - 1
    for letter in a[i:]:
        if len(setik) < n or (len(setik) == n and letter in setik):
            setik.add(letter)
            word += letter
            index += 1
            if index == index_last_letter:
                listik.append(word)
                setik.clear()
                word = str()
        else:
            listik.append(word)
            setik.clear()
            word = str()
            break
print(listik)

result = max(*listik, key=lambda x: len(x))
print(result)