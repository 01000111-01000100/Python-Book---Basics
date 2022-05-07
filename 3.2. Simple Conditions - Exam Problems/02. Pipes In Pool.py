v = float(input())
p1 = float(input())
p2 = float(input())
n = float(input())
full = (p1*n) + (p2*n)
if full<=v:
    print("The pool is {0}% full. Pipe 1: {1}%. Pipe 2: {2}%.".format(int((full / v) * 100),int(((n*p1) / full) * 100),int((n*p2 / full) * 100)))
else:
    print("For {0} hours the pool overflows with {1} liters.".format(n,abs(v-full)))