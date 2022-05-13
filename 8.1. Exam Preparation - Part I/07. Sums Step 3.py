n = int(input())
sum1 = sum2 = sum3 = 0

for i in range(0, n):
    a = int(input())

    if i % 3 == 0:
        sum1 += a
    if i % 3 == 1:
        sum2 += a
    if i % 3 == 2:
        sum3 += a
print('sum1 = %d' % sum1)
print('sum2 = %d' % sum2)
print('sum3 = %d' % sum3)