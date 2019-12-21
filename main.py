import numpy as np

def DD(infile):
    K = []
    f = open(infile, 'r')
    temp = f.readline().split(' ')
    T = int(temp[0])
    n = int(temp[1])
    columnIndex = (1 << n) - 1 # columnIndex = 0 if column is removed
    for i in range(0, T):
        temp = f.readline()
        temp = temp.split(' ')
        tempK = 0

        for j in range(0, len(temp) - 1):
            if temp[j] == '1':
                tempK = tempK ^ (1 << (len(temp) - j - 2)) # set ith bit
        K.append(tempK)

        if temp[-1].rstrip() == '0': # if outcome = 0
            for j in range(0, n):
                if K[i] & (1 << j) != 0: # if ith bit = 1
                    if columnIndex & (1 << j) != 0:
                        columnIndex = columnIndex ^ (1 << j)

    columnIndex = bin(columnIndex)
    columnIndex = columnIndex[2:].zfill(n)
    for i in range(0, len(K)):
        for j in range(0, n):
            if columnIndex[j] == '0':
                if K[i] & (1 << (n - j - 1)) != 0:
                    K[i] = K[i] ^ (1 << (n - j - 1))
    return K, n

if __name__ == "__main__":
    K, n = DD("input.txt")
    for i in K:
        print(bin(i)[2:].zfill(n))
    pass