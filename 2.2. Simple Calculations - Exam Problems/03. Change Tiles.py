n_side_of_area = int(input())
wight_tile = float(input())
lenght_tile = float(input())
wight_bench = int(input())
lenght_bench = int(input())

total_area = n_side_of_area * n_side_of_area
area_bench = wight_bench * lenght_bench
coverage_area = total_area - area_bench
tile_area = wight_tile * lenght_tile
tile_count = coverage_area / tile_area
time_count = tile_count * 0.2
print(round(tile_count, 2))
print(round(time_count, 2))