def do_flowerbeds(num, seq):
    result = []
    for i in range(num):
        if i == num - 1:
            result.append(seq[i])
            return result
        if seq[i][1] == seq[i+1][0]:
            seq[i+1][0] = seq[i][0]
        elif seq[i][1] < seq[i+1][0]:
            result.append(seq[i])
        else:
            if seq[i][1] <= seq[i+1][1]:
                seq[i + 1][0] = seq[i][0]
            else:
                seq[i + 1][0] = seq[i][0]
                seq[i + 1][1] = seq[i][1]
    return result


if __name__ == '__main__':
    num = int(input())
    num_array = [[int(n) for n in input().split()] for i in range(num)]
    num_array.sort()
    print(*[f'{i[0]} {i[1]}' for i in do_flowerbeds(num, num_array)], sep='\n')
