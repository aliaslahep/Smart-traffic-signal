import cv2
import glob
from vehicle_detector import VehicleDetector

# Load Veichle Detector
vd = VehicleDetector()

# Load images from a folder
images_folder = glob.glob("img2.jpg")

bike_count = 0
car_count = 0
bus_count = 0

# Loop through all the images
for img_path in images_folder:
    print("Img path", img_path)
    img = cv2.imread(img_path)

    vehicle_boxes,vehicle_boxes1,vehicle_boxes2 = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)
    vehicle_count1 = len(vehicle_boxes1)
    vehicle_count2 = len(vehicle_boxes2)


    # Update total count
    bike_count += vehicle_count
    car_count += vehicle_count1
    bus_count += vehicle_count2


    for box in vehicle_boxes:
        x, y, w, h = box

        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

        cv2.putText(img, "Number of bikes: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

    for box in vehicle_boxes1:
        x, y, w, h = box

        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

        cv2.putText(img, "Number of car: " + str(vehicle_count1), (20, 50), 0, 2, (100, 200, 0), 3)

    for box in vehicle_boxes2:
        x, y, w, h = box

        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

        cv2.putText(img, "Number of bus: " + str(vehicle_count2), (20, 50), 0, 2, (100, 200, 0), 3)

    cv2.imshow("Cars", img)
    cv2.waitKey(1)

print("Total bike count", bike_count)
print("Total car count", car_count)
print("Total bus count", bus_count)

