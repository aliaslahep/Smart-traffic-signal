from durationus import *
from ssDelete import ss
import time
import keyboard

while(True):
    if(keyboard.is_pressed("q")):
        break
    print("LANE 1 IS GREEN")
    ss()
    x = traffic_light_controller(vc)
    time.sleep(x)

    print("LANE 2 IS GREEN")
    ss()
    x = traffic_light_controller(vc1)
    time.sleep(x)

    print("LANE 3 IS GREEN")
    ss()
    x = traffic_light_controller(vc2)
    time.sleep(x)

    print("LANE 4 IS GREEN")
    ss()
    x = traffic_light_controller(vc3)
    time.sleep(x)
