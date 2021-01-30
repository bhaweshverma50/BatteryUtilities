import psutil
import keyboard
import time

print("Starting Program...")
start = 0
end = 0
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
            end = time.time()
            runTime = convertTime(end-start)
            print("Last charged "+runTime+" ago\n")
            run = 0

    elif(status == False):
        if(run == 0):
            start = time.time()
            run = 1
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
