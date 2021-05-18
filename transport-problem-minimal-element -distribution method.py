n = 3
m = 4
a = [20, 15, 25]
b = [13, 17, 19, 11]
c = [[6, 5, 2, 1], [3, 5, 4, 2], [5, 3, 6, 3]]
x = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# Least Element Method
i = 0
j = 0
M = 10 ** 5
min_elem = c[0][0]
while True:
    for i in range(n):
        for j in range(m):
            if c[i][j] < min_elem and a[i] != 0 and b[j] != 0:
                min_elem = c[i][j]
                i0 = i
                j0 = j
    if all(v == 0 for v in a) and all(g == 0 for g in b):
        break
    elif a[i0] > b[j0]:
        x[i0][j0] = b[j0]
        a[i0] -= b[j0]
        b[j0] = 0
    elif a[i0] < b[j0]:
        x[i0][j0] = a[i0]
        b[j0] -= a[i0]
        a[i0] = 0
    elif a[i0] == b[j0]:
        x[i0][j0] = a[i0]
        a[i0] = 0
        b[j0] = 0
    min_elem = M
print(x, '\n')
while True:
    empty_cells = []
    for i in range(n * m - (n + m - 1)):
        empty_cells.append(0)
    full_cells = []
    for i in range(n + m - 1):
        full_cells.append(0)
    p = 0
    q = 0
    for i in range(n):
        for j in range(m):
            if x[i][j] == 0:
                empty_cells[p] = [i, j]
                p += 1
            else:
                full_cells[q] = [i, j]
                q += 1
    Loop = []
    for k in range(len(empty_cells)):
        Loop.append([])
    for k in range(len(empty_cells)):
        i0 = empty_cells[k][0]
        j0 = empty_cells[k][1]
        Edge_k = [i0, j0]
        Loop[k].append(Edge_k)
        for r in range(len(full_cells)):
            if j0 == full_cells[r][1]:
                Edge_k = full_cells[r]
                Loop[k].append(Edge_k)
                i1 = full_cells[r][0]
                break
        for r in range(len(full_cells)):
            if i1 == full_cells[r][0] and j0 != full_cells[r][1]:
                Edge_k = full_cells[r]
                Loop[k].append(Edge_k)
                j1 = full_cells[r][1]
                break
        for r in range(len(full_cells)):
            if [i0, j1] == full_cells[r]:
                Edge_k = [i0, j1]
                Loop[k].append(Edge_k)
                break
        if len(Loop[k]) < 4:
            for r in range(len(full_cells)):
                if j1 == full_cells[r][1] and i1 != full_cells[r][0]:
                    Edge_k = full_cells[r]
                    Loop[k].append(Edge_k)
                    i2 = full_cells[r][0]
                    break
            for r in range(len(full_cells)):
                if i2 == full_cells[r][0] and j1 != full_cells[r][1]:
                    Edge_k = full_cells[r]
                    Loop[k].append(Edge_k)
                    j2 = full_cells[r][1]
                    break
            for r in range(len(full_cells)):
                if [i0, j2] == full_cells[r]:
                    Edge_k = [i0, j2]
                    Loop[k].append(Edge_k)
                    break
    q = 10 ** 5
    u = []
    for i in range(n):
        u.append(q)
    v = []
    for i in range(m):
        v.append(q)
    u[full_cells[0][0]] = 0
    for i in range(len(full_cells)):
        if u[full_cells[i][0]] != q and v[full_cells[i][1]] == q:
            v[full_cells[i][1]] = c[full_cells[i][0]][full_cells[i][1]] - u[full_cells[i][0]]
        elif v[full_cells[i][1]] != q and u[full_cells[i][0]] == q:
            u[full_cells[i][0]] = c[full_cells[i][0]][full_cells[i][1]] - v[full_cells[i][1]]
    for i in range(len(full_cells)):
        if u[full_cells[i][0]] != q and v[full_cells[i][1]] == q:
            v[full_cells[i][1]] = c[full_cells[i][0]][full_cells[i][1]] - u[full_cells[i][0]]
        elif v[full_cells[i][1]] != q and u[full_cells[i][0]] == q:
            u[full_cells[i][0]] = c[full_cells[i][0]][full_cells[i][1]] - v[full_cells[i][1]]
    Delta = []
    sum_c = 0
    for i in range(len(Loop)):
        for j in range(len(Loop[i])):
            k1 = Loop[i][j][0]
            k2 = Loop[i][j][1]
            if j % 2 == 0:
                sum_c -= c[k1][k2]
            else:
                sum_c += c[k1][k2]
        Delta.append(sum_c)
        sum_c = 0
    max_elem = Delta[0]
    for i in range(len(Delta)):
        if max_elem < Delta[i]:
            max_elem = Delta[i]
    if max_elem <= 0:
        break
    index_max_elem = Delta.index(max_elem)
    min_x = []
    for j in range(len(Loop[index_max_elem])):
        k1 = Loop[index_max_elem][j][0]
        k2 = Loop[index_max_elem][j][1]
        if j % 2 != 0:
            min_x.append(x[k1][k2])
    for j in range(len(Loop[index_max_elem])):
        k1 = Loop[index_max_elem][j][0]
        k2 = Loop[index_max_elem][j][1]
        if j % 2 == 0:
            x[k1][k2] += min(min_x)
        else:
            x[k1][k2] -= min(min_x)
print(Delta, '\n')
print(x, '\n')
f = 0
for i in range(n):
    for j in range(m):
        if x[i][j] != 0:
            f += x[i][j] * c[i][j]
print(f)
