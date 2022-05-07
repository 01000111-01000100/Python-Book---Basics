n = int(input())

min_number = 1000000000
count = 1
while count <= n:
    current_number = int(input())
    if current_number < min_number:
        min_number = current_number
    count += 1
print(min_number)