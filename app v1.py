# Imported required library and made object of battery sensor class/function
import psutil
import time
battery = psutil.sensors_battery()


# Defined funtions to convert secs to hh:mm:ss format and to output the corresponding result
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


def output():
    L = ["Battery : "+batteryPercent+"%", "Status: "+batteryPower,
         "Time Remaininng: "+timeRemaining]
    for i in L:
        print(i, flush=True)
        file.write("%s\n" % i)


# Gathering all data and storing as string
batteryPercent = str(battery.percent)
status = battery.power_plugged

if(status):
    batteryPower = "Charging..."
else:
    batteryPower = "Discharging..."

timeRemaining = str(convertTime(battery.secsleft))
start = 0
chargeTime = 0
lastCharged = 0

# while(status):
#     start = time.time()

# end = time.time()
# chargeTime = convertTime(end-start)

# Outputting the data in terminal as well as in txt file
file = open("output.txt", "w")
output()
file.close()
