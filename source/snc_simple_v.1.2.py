wind_speed = int(input("Input cyclone wind speed (km/h): "))

if wind_speed <= 61:
    print("Signal no. 1")
    print("Type: Tropical Depression")
    print("Lead Time: 36 h")
    print("Impact: Minor")

elif 62 <= wind_speed <= 88:
    print("Signal no. 2")
    print("Type: Tropical Storm")
    print("Lead Time: 24 h")
    print("Impact: Moderate")

elif 89 <= wind_speed <= 117:
    print("Signal no. 3")
    print("Type: Severe Tropical Storm")
    print("Lead Time: 18 h")
    print("Impact: Significant")

elif 118 <= wind_speed <= 184:
    print("Signal no. 4")
    print("Type: Typhoon")
    print("Lead Time: 12 h")
    print("Impact: Severe")

else:
    print("Signal no. 5")
    print("Type: Super Typhoon")
    print("Lead Time: 12 h")
    print("Impact: Catastrophic")
