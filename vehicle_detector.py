import cv2
import numpy as np

class VehicleDetector:

    def __init__(self):
        # Load Network
        net = cv2.dnn.readNet("dnn_model/yolov4.weights", "dnn_model/yolov4.cfg")
        self.model = cv2.dnn_DetectionModel(net)
        self.model.setInputParams(size=(832, 832), scale=1 / 255)


        # Allow classes containing Vehicles only
        self.classes_allowed = [2, 3, 5, 7]


    def detect_vehicles(self, img):
        # Detect Objects
        vehicles_boxes = []
        vehicles_boxes1 = []
        vehicles_boxes2 = []

        class_ids, scores, boxes = self.model.detect(img, nmsThreshold=0.4)
        for class_id, score, box in zip(class_ids, scores, boxes):
            if score < 0.5:
                # Skip detection with low confidence
                continue

            #if class_id in self.classes_allowed:
             #   vehicles_boxes.append(box)

            if class_id == 3:
                vehicles_boxes.append(box)

            if class_id == 2:
                vehicles_boxes1.append(box)

            if class_id == 5:
                vehicles_boxes2.append(box)

            if class_id == 7:
                vehicles_boxes2.append(box)

        return vehicles_boxes, vehicles_boxes1, vehicles_boxes2

