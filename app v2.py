import psutil
import keyboard
import time

print("Starting Program...")

while True:
    battery = psutil.sensors_battery()
    status = battery.power_plugged
    print(status)
    if keyboard.is_pressed("q"):
        break
    elif(status == True):
        print("Charging...")
    elif(status == False):
        print("Discharging...")
    time.sleep(1)
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
