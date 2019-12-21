import numpy as np

def DD(infile):
    M = [] # test design
    f = open(infile, 'r')
    temp = f.readline().split(' ')
    T = int(temp[0]) # number of tests
    n = int(temp[1]) # number of items
    columnIndex = (1 << n) - 1 # columnIndex = 0 if column is removed

    # read test design
    for i in range(0, T):
        temp = f.readline()
        temp = temp.split(' ')
        tempM = 0

        for j in range(0, len(temp) - 1):
            if temp[j] == '1':
                tempM = tempM ^ (1 << (len(temp) - j - 2)) # set ith bit
        M.append(tempM)

        if temp[-1].rstrip() == '0': # if outcome = 0
            for j in range(0, n):
                if M[i] & (1 << j) != 0: # if ith bit = 1
                    if columnIndex & (1 << j) != 0:
                        columnIndex = columnIndex ^ (1 << j)
    # remove column
    columnIndex = bin(columnIndex)
    columnIndex = columnIndex[2:].zfill(n)
    for i in range(0, len(M)):
        for j in range(0, n):
            if columnIndex[j] == '0':
                if M[i] & (1 << (n - j - 1)) != 0:
                    M[i] = M[i] ^ (1 << (n - j - 1))
    return M, n

if __name__ == "__main__":
    M, n = DD("input.txt")
    for i in M:
        print(bin(i)[2:].zfill(n))
    pass