import cv2
import matplotlib.pyplot as plt
import numpy as np

path = r'C:\Users\alokk\Documents\OpenCV\OpenCV_Lect1\test_CV_image.jpg'  # Replace with your image path
image = cv2.imread(path,1)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# window_name = 'Image Display'
# cv2.imshow(window_name, image)
# image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
# cv2.imshow(window_name, image)
# cv2.waitKey(0)

# (row,cols)= image.shape[:2]
# print("Rows:", row)
# print("Cols:", cols)

# M = cv2.getRotationMatrix2D((cols/2, row/2), 45, 1)
# rotated_image = cv2.warpAffine(image, M, (cols, row))
# cv2.imshow('Rotated Image', rotated_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# half = cv2.resize(image, (0,0), fx=0.1, fy=0.1)
# bigger = cv2.resize(image,(1050,1610))

# strech_near = cv2.resize(image,(780,540), interpolation=cv2.INTER_NEAREST)

# Titles = ['Original Image', 'Half Size', 'Bigger Size', 'Strech Nearest']
# images = [image, half, bigger, strech_near]
# count = 4

# for i in range(count):
#     plt.subplot(2, 2, i+1)
#     plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
# plt.show()

height, width = image.shape[:2]
print("Height:", height)   
print("Width:", width)

quarter_height, quarter_width = height // 4, width // 4
print("Quarter Height:", quarter_height)
print("Quarter Width:", quarter_width)
T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])
image_translation = cv2.warpAffine(image, T, (width, height))

cv2.imshow("Translated Image", image_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Canny edge detection
edges = cv2.Canny(image, 100, 200)
cv2.imshow("Canny Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
