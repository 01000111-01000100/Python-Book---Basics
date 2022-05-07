import math

hours = int(input())
day = int(input())
workers = int(input())
working_days = day * 0.90

working_hours = working_days * workers * (8 + 2)
difference = abs(hours - working_hours)

if working_hours >= hours:
    print('Yes!{0} hours left.' .format(math.floor(difference)))
else:
    print('Not enough time!{0} hours needed.' .format(math.ceil(difference)))