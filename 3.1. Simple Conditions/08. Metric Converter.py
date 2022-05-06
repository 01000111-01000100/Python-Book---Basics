distance = float(input())
input_unit = str(input())
output_unit = str(input())
units = {'mm': 1000, 'cm': 100, 'mi': 0.000621371192, 'in': 39.3700787, 'km': 0.001, 'ft': 3.2808399, 'yd': 1.0936133, 'm': 1}
result = (distance*units[output_unit])/units[input_unit]
print('%s %s' % (result , output_unit))