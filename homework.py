import cv2
import numpy as np

def apply_filter(frame, filter_type):
    filtered_frame = frame.copy()

    if filter_type == "red_tint":
        filtered_frame[:, :, 1] = 0
        filtered_frame[:, :, 0] = 0
    elif filter_type == "green_tint":
        filtered_frame[:, :, 0] = 0
        filtered_frame[:, :, 2] = 0
    elif filter_type == "blue_tint":
        filtered_frame[:, :, 1] = 0
        filtered_frame[:, :, 2] = 0
    elif filter_type == "sobel":
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        combined = cv2.bitwise_or(sobelx.astype('uint8'), sobely.astype('uint8'))
        filtered_frame = cv2.cvtColor(combined, cv2.COLOR_GRAY2BGR)
    elif filter_type == "canny":
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        filtered_frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    return filtered_frame

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access camera")
else:
    filter_type = "original"

    print("r - Red | g - Green | b - Blue | s - Sobel | c - Canny | q - Quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        filtered_frame = apply_filter(frame, filter_type)
        cv2.imshow("Video Filter", filtered_frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('s'):
            filter_type = "sobel"
        elif key == ord('c'):
            filter_type = "canny"
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()