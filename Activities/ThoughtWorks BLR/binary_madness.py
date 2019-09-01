#
#
# def madness(n):
#
#     if n == 0:
#         return 1,0
#
#     b = str(bin(n).split('b')[1])
#     n_binary = len(b)
#
#
#
#
#     c_ones = 0
#     c_zeroes = 0
#     for i in range(n_binary):
#         for j in range(i,n_binary):
#             sub = b[i:j+1]
#
#             ones = sub.count('1')
#             zeroes = sub.count('0')
#
#             if ones%2 == 1:
#                 c_ones += 1
#             if zeroes%2 == 1:
#                 c_zeroes += 1
#     return c_zeroes, c_ones

def madness(x):
    b = bin(x)[2:]
    n = len(b)

    ####### This is for 1's ########
    mem = [[0 for i in range(n)] for j in range(n)]
    count_1 = 0
    for i in range(n):
        if b[i] == '1':
            count_1 += 1
        if count_1 % 2:
            mem[0][i] = 1
    # print(mem)

    # run DP loop
    c1 = sum(mem[0])
    for i in range(1, n):
        for j in range(i, n):
            # print(i, j, mem[i - 1][j], mem[i - 1][i - 1])
            if mem[i - 1][j] != mem[i - 1][i - 1]:
                # mem[i][j] = 1
                c1 += 1
    # count_1 = sum(sum(mem,[]))

    ####### This is for 0's ########
    mem = [[0 for i in range(n)] for j in range(n)]
    count_0 = 0
    for i in range(n):
        if b[i] == '0':
            count_0 += 1
        if count_0 % 2:
            mem[0][i] = 1
    print(mem)

    # run DP loop
    c0 = sum(mem[0])
    for i in range(1, n):
        for j in range(i, n):
            if mem[i - 1][j] != mem[i - 1][i - 1]:
                c0 += 1

    # count_0 = sum(sum(mem, []))

    print(c0, c1)
    return c0, c1

# t = int(input())
# for i in range(t):
#     n = int(input())
#     res = madness(n)
#     print(res[0], res[1])

n = 17
res = madness(n)
print(res[0], res[1])