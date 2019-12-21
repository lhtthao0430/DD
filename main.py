import math 

def NaiveDecode(infile):
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
    X, n = NaiveDecode("input.txt")
    # for i in X:
    #     print(bin(i)[2:].zfill(8))

    # DD
    K = []
    for i in X:
        if i != 0 and math.ceil(math.log(i, 2)) == math.floor(math.log(i, 2)): # check if i is power of 2 or there is only one number 1 in a test
            K.append(n - int(math.log(i, 2)))
    print("DD = ", K)

     # COMP
    K = set()
    for i in X:
        if i != 0:
            for j in range(0, n):
                if i & (1 << j) != 0:
                    K.add(n - int(math.log(1 << j, 2)))
    K = list(K)
    print("COMP = ", K)
    pass
