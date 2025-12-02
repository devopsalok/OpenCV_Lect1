import cv2
import sys

# ...existing code...
image = cv2.imread('test_image.jpg')
if image is None:
    print("Error: failed to load test_image.jpg")
    sys.exit(1)

h, w = image.shape[:2]
print("Height:", h)
print("Width:", w)

# Safe pixel access (clamp indices)
y, x = min(100, h-1), min(100, w-1)
(B, G, R) = image[y, x]
print("R = {}, G = {}, B = {}".format(R, G, B))
B_val = image[y, x, 0]
print("B = {}".format(B_val))

# Safe ROI slicing
y1, y2 = 100, 500
x1, x2 = 200, 700
y1, y2 = max(0, y1), min(h, y2)
x1, x2 = max(0, x1), min(w, x2)
if y1 < y2 and x1 < x2:
    roi = image[y1:y2, x1:x2]
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)

# Resize examples
resize = cv2.resize(image, (500, 500))
cv2.imshow("Resized Image", resize)
cv2.waitKey(0)

ratio = 800 / float(w)
dim = (800, int(h * ratio))
resize_aspect = cv2.resize(image, dim)
cv2.imshow("Resized Aspect", resize_aspect)
cv2.waitKey(0)

# Draw rectangle on a copy; compute coords relative to image size
output = image.copy()
rx1 = int(w * 0.25)
ry1 = int(h * 0.20)
rx2 = int(w * 0.75)
ry2 = int(h * 0.60)

# Use red color (BGR) to ensure visibility and reasonable thickness
cv2.rectangle(output, (rx1, ry1), (rx2, ry2), (0, 0, 255), 2)
cv2.putText(output, 'OpenCV Demo', (rx1, max(20, ry1 - 10)),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Display the output resized so it fits on screen
display = cv2.resize(output, (800, int(h * (800 / w))))
cv2.imshow("Output with Rectangle and Text", display)
cv2.waitKey(0)
# ...existing code...