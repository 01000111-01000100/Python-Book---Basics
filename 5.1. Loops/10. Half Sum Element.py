cout_of_number = int(input())
sum_of_element = 0
max_number = ''
for number in range(cout_of_number):
    curr_number = int(input())
    if number == 0:
        max_number = curr_number
    sum_of_element += curr_number
    if curr_number > max_number:
        max_number = curr_number
if max_number == sum_of_element - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    diff = abs(max_number - (sum_of_element - max_number))
    print("No")
    print(f"Diff = {diff}")
