import math

budget = float(input())
width_floor = float(input())
length_floor = float(input())
side_of_triangle = float(input())
height_of_triangle = float(input())
price_per_tile = float(input())
worker_price = float(input())

area_floor = width_floor * length_floor
area_tile = side_of_triangle * height_of_triangle / 2
tiles_needed = math.ceil(area_floor / area_tile) + 5
total_cost = tiles_needed * price_per_tile + worker_price


if budget <= total_cost:
    money_left = budget - total_cost
    print(f"You'll need {abs(money_left):.2f} lv more.")
else:
    money_needed = budget - total_cost
    print(f"{money_needed:.2f} lv left.")
