transport = int(input())

microbus = 0.0
truck = 0.0
train = 0.0
sum_tons = 0.0

tons_microbus = 0.0
tons_truck = 0.0
tons_train = 0.0
average_tons = 0.0

for i in range(transport):
    tons = int(input())
    if tons <= 3:
        microbus += tons * 200
        tons_microbus += tons
    elif tons <= 11:
        truck += tons * 175
        tons_truck += tons
    else:
        train += tons * 120
        tons_train += tons
sum_tons = tons_train + tons_microbus + tons_truck

average_tons = (microbus + truck + train) / sum_tons

microbus_percent = (tons_microbus / sum_tons) * 100
truck_percent = (tons_truck / sum_tons) * 100
train_percent = (tons_train / sum_tons) * 100

print(f"{average_tons:.2f}")
print(f"{microbus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")