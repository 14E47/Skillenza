def solution(r,c,k,matrix):
    streaks = 0

    # horizontal streak
    for i in range(r-k):
        for j in range(c-k):
            print(matrix[r:c+1])





t = int(input())
for i in range(t):
    mnk = list(map(int, input().split()))
    m,n,k = mnk[0], mnk[1], mnk[2]
    matrix = []
    for j in range(m):
        matrix.append(input().split())

    print(matrix)
    c = solution(m,n,k,matrix)
    print(c)


# 1
# 3 3 3
# x x x
# x o x
# x x x
