import cv2
import numpy as np

# Read image.
img = cv2.imread('E:/Unscene_Company/WorkSpace/CircleDetection/Pics/circles2.jpg', cv2.IMREAD_COLOR)

# Convert to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur using 3 * 3 kernel.
gray_blurred = cv2.medianBlur(gray, 3)

# Estimate minRadius and maxRadius based on image dimensions.
minRadius = int(0.01 * img.shape[1])  # 1% of image width
maxRadius = int(0.3 * img.shape[1])   # 30% of image width

# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20,
                                    param1=100, param2=30, minRadius=1, maxRadius=40)

# If circles are detected, draw them.
if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        # Draw the circumference of the circle.
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)

        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

cv2.imshow("Detected Circle", img)
cv2.waitKey(0)
