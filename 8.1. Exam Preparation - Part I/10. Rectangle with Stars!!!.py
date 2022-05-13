import math

n = int(input())  # 2 / 1000
middle_rows = n
if n % 2 == 0:
    middle_rows = n - 1
central_row = math.ceil(middle_rows / 2)

print("%" * (2 * n))

for i in range(middle_rows):
    if central_row - 1 != i:
        print("%", end="")
        print(" " * (2 * n - 2), end="")
        print("%")
    else:
        print("%", end="")
        print(" " * (n - 2), end="")
        print("**", end="")
        print(" " * (n - 2), end="")
        print("%")

print("%" * (2 * n))