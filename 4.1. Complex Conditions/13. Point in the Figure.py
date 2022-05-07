h = int(input())
x = int(input())
y = int(input())
insideBottom = (x > 0 and x < h * 3 and y > 0 and y < h)
insideTop = (x > h and x < h * 2 and y > 0 and y < h * 4)
outsideTop = (x < h or x > h * 2 or y < 0 or y > h * 4)
outsideBottom = (x < 0 or x > h * 3 or y < 0 or y > h)
if (insideBottom or insideTop):
    print("Inside")
elif (outsideTop and outsideBottom):
    print("Outside")
else:
    print("Border")