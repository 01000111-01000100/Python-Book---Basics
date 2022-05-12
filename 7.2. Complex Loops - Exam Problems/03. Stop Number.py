n = int(input())
m = int(input())
s = int(input())
if 0 <= n and n < m and m <= 10000 and s <= m:
    i = m
    while i >= n:
        if i % 2 == 0 and i % 3 == 0:
            if (s == i):
                break
            else:
                print(str(i) + " ", end="")
        i -= 1