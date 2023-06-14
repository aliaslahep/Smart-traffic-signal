import cv2
import glob
from vehicle_detector import VehicleDetector
from screenshot import  *

vd= VehicleDetector()

print("LANE 1")
#FOR LANE 1
b=0
c=0
bs=0
img=cv2.imread('Frame0.jpg')
bike_boxes, car_boxes, bus_boxes = vd.detect_vehicles(img)
bike_count = len(bike_boxes)
b += bike_count
car_count = len(car_boxes)
c += car_count
bus_count = len(bus_boxes)
bs += bus_count

for box in bike_boxes:
    x, y, w, h = box
    cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
    cv2.putText(img, "bike: " + str(bike_count), (20, 50), 0, 2, (100, 200, 0), 3)
    cv2.imshow("bike", img)
    cv2.waitKey(1)
print("Total bike :", b)
for box in car_boxes:
    x, y, w, h = box
    cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
    cv2.putText(img, "car: " + str(car_count), (20, 100), 0, 2, (100, 200, 0), 3)
    cv2.imshow("Cars", img)
    cv2.waitKey(1)
print("Total car :", c)
for box in bus_boxes:
    x, y, w, h = box
    cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
    cv2.putText(img, "bus: " + str(bus_count), (20, 150), 0, 2, (100, 200, 0), 3)
    cv2.imshow("bus", img)
    cv2.waitKey(1)
print("Total bus :", bs)

print("LANE 2")
#FOR LANE 2
b1=0
c1=0
bs1=0
img=cv2.imread('Frame1.jpg')
bike_boxes1, car_boxes1, bus_boxes1 = vd.detect_vehicles(img)
bike_count1 = len(bike_boxes1)
b1 += bike_count1
car_count1 = len(car_boxes1)
c1 += car_count1
bus_count1 = len(bus_boxes1)
bs1 += bus_count1

for box in bike_boxes1:
    x, y, w, h = box
    cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
    cv2.putText(img, "bike: " + str(bike_count1), (20, 50), 0, 2, (100, 200, 0), 3)
    cv2.imshow("bike", img)
    cv2.waitKey(1)
print("Total bike :", b1)
for box in car_boxes1:
    x, y, w, h = box
    cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
    cv2.putText(img, "car: " + str(car_count1), (20, 100), 0, 2, (100, 200, 0), 3)
    cv2.imshow("Cars", img)
    cv2.waitKey(1)
print("Total car :", c1)
for box in bus_boxes1:
    x, y, w, h = box
    cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
    cv2.putText(img, "bus: " + str(bus_count1), (20, 150), 0, 2, (100, 200, 0), 3)
    cv2.imshow("bus", img)
    cv2.waitKey(1)
print("Total bus :", bs1)

print("LANE 3")
#FOR LANE 3
b2=0
c2=0
bs2=0
img=cv2.imread('Frame2.jpg')
bike_boxes2, car_boxes2, bus_boxes2 = vd.detect_vehicles(img)
bike_count2 = len(bike_boxes2)
b2 += bike_count2
car_count2 = len(car_boxes2)
c2 += car_count2
bus_count2 = len(bus_boxes2)
bs2 += bus_count2

for box in bike_boxes2:
    x, y, w, h = box
    cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
    cv2.putText(img, "bike: " + str(bike_count2), (20, 50), 0, 2, (100, 200, 0), 3)
    cv2.imshow("bike", img)
    cv2.waitKey(1)
print("Total bike :", b2)
for box in car_boxes2:
    x, y, w, h = box
    cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
    cv2.putText(img, "car: " + str(car_count2), (20, 100), 0, 2, (100, 200, 0), 3)
    cv2.imshow("Cars", img)
    cv2.waitKey(1)
print("Total car :", c2)
for box in bus_boxes2:
    x, y, w, h = box
    cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
    cv2.putText(img, "bus: " + str(bus_count2), (20, 150), 0, 2, (100, 200, 0), 3)
    cv2.imshow("bus", img)
    cv2.waitKey(1)
print("Total bus :", bs2)
print("LANE 4")
#FOR LANE 4
b3=0
c3=0
bs3=0
img=cv2.imread('Frame3.jpg')
bike_boxes3, car_boxes3, bus_boxes3 = vd.detect_vehicles(img)
bike_count3 = len(bike_boxes3)
b3 += bike_count3
car_count3 = len(car_boxes3)
c3 += car_count3
bus_count3 = len(bus_boxes3)
bs3 += bus_count3

for box in bike_boxes3:
    x, y, w, h = box
    cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
    cv2.putText(img, "bike: " + str(bike_count3), (20, 50), 0, 2, (100, 200, 0), 3)
    cv2.imshow("bike", img)
    cv2.waitKey(1)
print("Total bike :", b3)
for box in car_boxes3:
    x, y, w, h = box
    cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
    cv2.putText(img, "car: " + str(car_count3), (20, 100), 0, 2, (100, 200, 0), 3)
    cv2.imshow("Cars", img)
    cv2.waitKey(1)
print("Total car :", c3)
for box in bus_boxes3:
    x, y, w, h = box
    cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
    cv2.putText(img, "bus: " + str(bus_count3), (20, 150), 0, 2, (100, 200, 0), 3)
    cv2.imshow("bus", img)
    cv2.waitKey(1)
print("Total bus :", bs3)