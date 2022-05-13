import math

x = int(input())
w = int(input())
m = int(input())

brick_in_course = w * m
total_courses = math.ceil(x / brick_in_course)
print(total_courses)