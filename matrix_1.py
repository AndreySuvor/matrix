n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
total = 1
k = 0
while total != n * m + 1:
    for i in range(n):
        for j in range(m):
            if i + j == k:
                matrix[i][j] = total
                total += 1
    k += 1
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
