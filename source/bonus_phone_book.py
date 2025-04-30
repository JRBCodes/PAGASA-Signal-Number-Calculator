hotline = input("What hotline do you want the number to?: ")

if hotline == "National Emergency Hotline":
    print(911)
elif hotline == "Red Cross":
    print(143)
elif hotline == "PNP":
    print(177)
    print("or")
    print("(02) 8722-0650")
elif hotline == "MMDA":
    print(136)
elif hotline == "Fire Protection":
    print("(02) 8426-0219")
else:
    print("Number of selected hotline does not exist.")