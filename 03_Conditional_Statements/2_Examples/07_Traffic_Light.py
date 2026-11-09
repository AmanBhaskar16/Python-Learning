# TRAFFIC LIGHT SYSTEM

light = input("Enter traffic light color: ").lower()

if light == "red":
    print("STOP")

elif light == "yellow":
    print("WAIT")

elif light == "green":
    print("GO")

else:
    print("Invalid Traffic Light")