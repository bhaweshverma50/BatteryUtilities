import psutil

battery = psutil.sensors_battery()

print("Battery percentage : ", battery.percent)
print("Power plugged in : ", battery.power_plugged)


def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


print("Battery left : ", convertTime(battery.secsleft))

file = open("test.txt", "w")
L = [battery.percent, battery.power_plugged,
     convertTime(battery.secsleft)]
file.writelines(str(L))
file.close()
