bitcoin = int(input())
yuan = float(input())
comission = float(input()) / 100

euro = ((bitcoin * 1168) + (yuan * 0.15 * 1.76)) / 1.95 - (comission * ((bitcoin * 1168) + (yuan * 0.15 * 1.76)) / 1.95)
print("%.2f" % euro)