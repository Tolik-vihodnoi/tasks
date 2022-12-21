with open("input_glass.txt", "r") as f:
    nm = f.readline().split()
    n = int(nm[0])
    m = int(nm[1])
    glass = f.readlines(n*m)
    k = int(f.readline())
    start = 0
    for i in range(1, k+1):
        ncs = f.readline().split()
        name = ncs[0]
        count = int(ncs[1])
        symbol = ncs[2]
        for lay in range(-1 * (start + count) - 1, -1 - start):
            glass[lay] = glass[lay].replace(" ", symbol)
        start += count

with open("output_glass.txt", "w") as f:
    f.writelines(glass)
