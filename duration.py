import time
from vehdec import *

# Define the minimum and maximum durations for a traffic light cycle
MIN_DURATION = 10
MAX_DURATION = 120

# Function to calculate the desired duration based on the number of vehicles
def calculate_duration(num_vehicles,green_lane):
    # Define the mapping function here (e.g., linear function)
    # Adjust the coefficients based on your specific requirements
    duration = (green_lane/(num_vehicles))*100  # Example linear mapping function
    return min(MAX_DURATION, max(MIN_DURATION, duration))


# Function to simulate monitoring the number of vehicles
# Traffic light control loop
def traffic_light_controller():
    x=0
    while x<1:
        # Get the vehicle count for each direction
        vehicles_north = vc
        vehicles_south = vc1
        vehicles_east = vc2
        vehicles_west = vc3
        x=x+1

        # Calculate the desired duration for each traffic light phase
        duration_total = calculate_duration(vehicles_north + vehicles_south+vehicles_east+vehicles_west,vehicles_south)

        # Adjust the traffic light durations
        print(f"North-South: {duration_total} seconds")
        print("Adjusting traffic light durations...")
        # Add your logic to adjust the traffic light durations here

        # Wait for the next cycle
        time.sleep(5)  # Adjust the sleep duration based on the desired frequency

# Run the traffic light controller
traffic_light_controller()
