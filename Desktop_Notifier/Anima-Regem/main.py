import notify2
import time

notify2.init("Desktop Notification")
n = notify2.Notification("Drink up!!", 'Drink some water...',)
n.set_urgency(notify2.URGENCY_LOW)

while True:
    n.show()
    time.sleep(3600)
