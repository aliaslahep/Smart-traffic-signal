import time
from vehdec import *

MIN_DURATION = 10
MAX_DURATION = 100

vc = b*1+c*3+bs*7
vc1 = b1*1+c1*3+bs1*7
vc2 = b2*1+c2*3+bs2*7
vc3 = b3*1+c3*3+bs3*7

def calculate_duration(num_vehicles,green_lane):

    duration = (green_lane/(num_vehicles))*100  # Example linear mapping function
    return min(MAX_DURATION, max(MIN_DURATION, duration))

def traffic_light_controller(x):

     duration_total = calculate_duration(vc+vc1+vc2+vc3, x)
     print(f"duration: {duration_total} seconds")
     print("Adjusting traffic light durations...")
     return duration_total
     #time.sleep(5)

# Run the traffic light controller




