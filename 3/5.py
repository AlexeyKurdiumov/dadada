import numpy as np
def negr(M, N):
    mat = [[0] * N for _ in range(M)]
    num = 1
    v, n = 0, M - 1
    l, r = 0, N - 1

    while num <= M * N:
        for i in range(l, r + 1):
            mat[v][i] = num
            num += 1
        v += 1
        for i in range(v, n + 1):
            mat[i][r] = num
            num += 1
        r -= 1
        if v <= n:
            for i in range(r, l - 1, -1):
                mat[n][i] = num
                num += 1
            n -= 1
        if l <= r:
            for i in range(n, v - 1, -1):
                mat[i][l] = num
                num += 1
            l += 1
    return np.array(mat)
M, N = 10, 10
asiat = negr(M, N)
print(asiat)