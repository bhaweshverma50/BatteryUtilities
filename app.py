import psutil

battery = psutil.sensors_battery()

batteryPercent = str(battery.percent)

if(battery.power_plugged):
    batteryPower = "Charger Connected! Charging..."
else:
    batteryPower = "On battery power! Discharging..."

print("Battery percentage : "+batteryPercent+"%")
print("Power plugged in : "+batteryPower)


def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


timeRemaining = str(convertTime(battery.secsleft))

print("Battery left : "+timeRemaining)

file = open("test.txt", "w")
L = ["Battery % : "+batteryPercent+"%", "Charger Plugged in: "+batteryPower,
     "Time Remaininng: "+timeRemaining]
file.writelines(str(L))
file.close()
