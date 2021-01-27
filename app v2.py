import psutil
import keyboard

battery = psutil.sensors_battery()
status = battery.power_plugged

print("Starting Program...")

while True:
    if keyboard.is_pressed("q"):
        break
    elif(status):
        print("Charging...")
        # pass
    else:
        print("Discharging...")
        # pass
print("Closing Program...")


# def convertTime(seconds):
#     minutes, seconds = divmod(seconds, 60)
#     hours, minutes = divmod(minutes, 60)
#     return "%d:%02d:%02d" % (hours, minutes, seconds)


# batteryPercent = str(battery.percent)
# if(status):
#     batteryPower = "Charging..."
# else:
#     batteryPower = "Discharging..."
# timeRemaining = str(convertTime(battery.secsleft))

# print("Battery : "+batteryPercent+"%", "\nStatus: "+batteryPower,
#       "\nTime Remaininng: "+timeRemaining)
