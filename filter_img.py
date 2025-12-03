import cv2

path = r'C:\Users\alokk\Documents\OpenCV\OpenCV_Lect1\test_CV_image.jpg'  # Replace with your image path
# Read the image
img = cv2.imread(path)

# Apply bilateral filter with d = 30,
# sigmaColor = sigmaSpace = 100
bilateral = cv2.bilateralFilter(img, 15, 100, 100)

# Save the output
cv2.imshow('Bilateral', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()