s = "kyaak"


for i in range(len(s)//2):
    if s[i] != s[len(s) - 1 - i]:
        s = s[0:i]+s[i+1]+s[i]+s[i+2:]
        break

for i in range(len(s)//2):
    if s[i] != s[len(s) - 1 - i]:
        print("-1")
        break
else:
    print(s)

