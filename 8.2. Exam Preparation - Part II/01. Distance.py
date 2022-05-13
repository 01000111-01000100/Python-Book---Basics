start_speed = int(input())
time1 = int(input()) / 60
time2 = int(input()) / 60
time3 = int(input()) / 60
total_trip_distance = start_speed * time1
total_trip_distance += start_speed * 1.1 * time2
total_trip_distance += start_speed * 1.1 * 0.95 * time3

final_result = ("{:.2f}".format(total_trip_distance))
print(final_result)