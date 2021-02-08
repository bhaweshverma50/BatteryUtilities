import psutil
import keyboard
import time

print("Starting Program...")

dischargeStart = 0
dischargeEnd = 0

chargingStart = 0
chargingEnd = 0
chargeStartPercent = 0
chargeEndPercent = 0


b = psutil.sensors_battery()
init_status = b.power_plugged

if(init_status):
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
    percent = battery.percent
    timeRemaining = convertTime(battery.secsleft)

    if keyboard.is_pressed("q"):
        break

    elif(status == True):
        if(run == 1):
            print("\n**************************************")
            print("Plugged in! Charging...\n")

            chargingStart = time.time()
            chargeStartPercent = battery.percent

            if(chargingEnd != 0):
                dischargeTime = convertTime(chargingStart-chargingEnd)
                totalPercentDischarged = chargeEndPercent - chargeStartPercent

                print(
                    f"Discharged {totalPercentDischarged}% in {dischargeTime} time\n")
                print(f"Charging started at: {percent}%")
                print("**************************************")
            else:
                print(f"Charging started at: {percent}%")
                print("**************************************")

            run = 0

    elif(status == False):
        if(run == 0):
            print("\n**************************************")
            print("Running on battery! Discharging...\n")

            chargingEnd = time.time()
            chargeEndPercent = battery.percent

            if(chargingStart != 0):
                chargeTime = convertTime(chargingEnd-chargingStart)
                totalPercentCharged = chargeEndPercent - chargeStartPercent

                print(f"Charged {totalPercentCharged}% in {chargeTime} time\n")
                print(f"Charging ended at: {percent}%\n")
                print(f"Predicted Time Remaining: {timeRemaining}")
                print("**************************************")
            else:
                print(f"Discharging started at: {percent}%\n")
                print(f"Predicted Time Remaining: {timeRemaining}")
                print("**************************************")

            run = 1

print("\nClosing Program...")
