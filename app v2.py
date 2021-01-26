# import psutil

# battery = psutil.sensors_battery()


# def convertTime(seconds):
#     minutes, seconds = divmod(seconds, 60)
#     hours, minutes = divmod(minutes, 60)
#     return "%d:%02d:%02d" % (hours, minutes, seconds)


# batteryPercent = str(battery.percent)
# status = battery.power_plugged
# if(status):
#     batteryPower = "Charging..."
# else:
#     batteryPower = "Discharging..."
# timeRemaining = str(convertTime(battery.secsleft))

# print("Battery : "+batteryPercent+"%", "\nStatus: "+batteryPower,
#       "\nTime Remaininng: "+timeRemaining)

import keyboard
print("starting")
keyboard.wait('q')
print("closing")
