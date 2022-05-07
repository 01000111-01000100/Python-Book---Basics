n = int(input())
oddSum = 0
oddMin = 1000000000
oddMax = -1000000000
evenSum = 0
evenMin = 1000000000
evenMax = -1000000000
for i in range(1, n + 1):
    num = float(input())

    if i % 2 == 0:
        evenSum = evenSum + num

        if num > evenMax:
            evenMax = num

        if num < evenMin:
            evenMin = num

    else:
        oddSum = oddSum + num

        if num > oddMax:
            oddMax = num

        if num < oddMin:
            oddMin = num

print("OddSum='{0:.5g}'".format(oddSum))
if oddMin != 1000000000:
    print("OddMin='{0:.5g}'".format(oddMin))

else:
    print("OddMin=No")

if oddMax != -1000000000:
    print("OddMax='{0:.5g}'".format(oddMax))

else:
    print("OddMax=No")

print("EvenSum=:'{0:.5g}'".format(evenSum))
if evenMin != 1000000000:
    print("EvenMin='{0:.5g}'".format(evenMin))

else:
    print("EvenMin=No")

if evenMax != -1000000000:
    print("EvenMax='{0:.5g}'".format(evenMax))

else:
    print("EvenMax=No")