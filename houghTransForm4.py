import cv2
import numpy as np


def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    return edged


def detect_circles(image_path):
    # Load image
    image = cv2.imread(image_path)
    output = image.copy()

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Blur the image to reduce noise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detection
    edges = auto_canny(gray)

    # Define the range for the radii
    h, w = edges.shape
    min_radius = int(h / 50)
    max_radius = int(h / 15)

    # Perform Hough Circle Transform
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=int(w / 20),
                               param1=40, param2=60, minRadius=min_radius, maxRadius=max_radius)

    # If circles are detected
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        # Loop over circles and draw them
        for (x, y, r) in circles:
            cv2.circle(output, (x, y), r, (0, 255, 0), 2)
            cv2.circle(output, (x, y), 2, (0, 255, 0), 3)
        # Show the output image with detected circles
        cv2.imshow("output", np.hstack([output]))
        cv2.waitKey(0)
    else:
        print("No circles were found in the image.")


# Call the function with the image path
detect_circles('E:/Unscene_Company/WorkSpace/CircleDetection/Pics/circles2.jpg')
