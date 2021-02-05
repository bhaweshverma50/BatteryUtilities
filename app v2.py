import psutil
import keyboard
import time

print("Starting Program...")
dischargeStart = 0
dischargeEnd = 0
chargingStart = 0
chargingStart = 0
battery = psutil.sensors_battery()
status = battery.power_plugged
if(status):
    run = 1
else:
    run = 0


def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


while True:
    battery = psutil.sensors_battery()
    status = battery.power_plugged

    if keyboard.is_pressed("q"):
        break

    elif(status == True):
        if(run == 1):
            print("*******************************")
            print("\nPlugged in! Charging...")
            dischargeEnd = chargingStart = time.time()
            if(dischargeStart != 0):
                runTime = convertTime(dischargeEnd-dischargeStart)
                print("Last charged "+runTime+" ago\n")
            run = 0

    elif(status == False):
        if(run == 0):
            dischargeStart = chargingEnd = time.time()
            run = 1
            if(dischargeStart != 0):
                runTime = convertTime(dischargeEnd-dischargeStart)
                print("Last charged "+runTime+" ago\n")
            print("*******************************")
            print("Running on battery! Discharging...\n")

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
