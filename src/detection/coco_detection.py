import cv2
import torch
import pyttsx3
import time
import numpy as np
import threading
from ultralytics import YOLO

model = YOLO('yolo11n.pt')
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak_async(text):
    thread = threading.Thread(target=lambda: (engine.say(text), engine.runAndWait()))
    thread.daemon = True
    thread.start()

KNOWN_HEIGHTS = {
    "person": 1.7, "bicycle": 1.0, "car": 1.5, "motorcycle": 1.2,
    "chair": 0.8, "bottle": 0.3, "pen": 0.14
}

CALIBRATION_OBJECT = "bottle"
CALIBRATION_DISTANCE = 1.0
FOCAL_LENGTH = 700

def estimate_focal_length(pixel_height, real_height, real_distance):
    return (pixel_height * real_distance) / real_height

def get_distance(y1, y2, class_name):
    global FOCAL_LENGTH
    pixel_height = abs(y2 - y1)

    if class_name == CALIBRATION_OBJECT and FOCAL_LENGTH == 700:
        FOCAL_LENGTH = estimate_focal_length(
            pixel_height,
            KNOWN_HEIGHTS[CALIBRATION_OBJECT],
            CALIBRATION_DISTANCE
        )

    if class_name in KNOWN_HEIGHTS:
        return round((FOCAL_LENGTH * KNOWN_HEIGHTS[class_name]) / (pixel_height + 1e-6), 2)

    return -1

cap = cv2.VideoCapture(0)
last_spoken_time = time.time()
speech_delay = 2

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    resized_frame = cv2.resize(frame, (640, 640))
    results = model.predict(resized_frame, conf=0.3, device=device, verbose=False)

    speech_data = []

    for result in results:
        for box in result.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = box
            class_name = model.names[int(class_id)]

            if (x2 - x1) * (y2 - y1) < 500:
                continue

            distance = get_distance(y1, y2, class_name)
            if distance > 0:
                speech_data.append(f"{class_name} {distance} meters away")

            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 255), 2)
            cv2.putText(frame, f"{class_name} {distance}m",
                        (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (255, 255, 255), 2)

    if speech_data and time.time() - last_spoken_time > speech_delay:
        speak_async("Warning! " + ", ".join(speech_data))
        last_spoken_time = time.time()

    cv2.imshow("COCO Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
