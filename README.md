# OpenCV_Lect1
To install OpenCV :- pip install opencv-python

Reading Images
To read the images cv2.imread() method is used. This method loads an image from the specified file. If the image cannot be read (because of the missing file, improper permissions, unsupported or invalid format) then this method returns an empty matrix.

Saving Images
cv2.imwrite() method is used to save an image to any storage device. This will save the image according to the specified format in the current working directory.

Displaying Images
cv2.imshow() method is used to display an image in a window. The window automatically fits the image size.

Rotate images

cv2.roate() method is used to rotate a 2D array in multiples of 90 degrees. The function cv::rotate rotates the array in three different ways.

Resizing Image
Image resizing refers to the scaling of images. It helps in reducing the number of pixels from an image and that has several advantages e.g. It can reduce the time of training of a neural network as more is the number of pixels in an image more is the number of input nodes that in turn increases the complexity of the model. It also helps in zooming in images. Many times we need to resize the image i.e. either shrink it or scale up to meet the size requirements.

OpenCV provides us with several interpolation methods for resizing an image. Choice of Interpolation Method for Resizing -

cv2.INTER_AREA: This is used when we need to shrink an image.
cv2.INTER_CUBIC: This is slow but more efficient.
cv2.INTER_LINEAR: This is primarily used when zooming is required. This is the default interpolation technique in OpenCV.

Color Spaces
Color spaces are a way to represent the color channels present in the image that gives the image that particular hue. There are several different color spaces and each has its own significance. Some of the popular color spaces are RGB (Red, Green, Blue), CMYK (Cyan, Magenta, Yellow, Black), HSV (Hue, Saturation, Value), etc.

 cv2.cvtColor() method is used to convert an image from one color space to another. There are more than 150 color-space conversion methods available in OpenCV.

 To add images: - weightedSum = cv2.addWeighted(image1, 0.5, image2,0.4, 0)

 To Substract images:- cv2.subtract(image1, image2)

 OpenCV Image Translation :- Translation refers to the rectilinear shift of an object i.e. an image from one location to another. If we know the amount of shift in horizontal and the vertical direction, say (tx, ty) then we can make a transformation matrix. Now, we can use the cv2.wrapAffine() function to implement the translations. This function requires a 2×3 array. The numpy array should be of float type.

 Edge Detection
The process of image detection involves detecting sharp edges in the image. This edge detection is essential in the context of image recognition or object localization/detection.

Image blurring

Image Blurring refers to making the image less clear or distinct. It is done with the help of various low pass filter kernels. Important types of blurring:

Gaussian Blurring: Gaussian blur is the result of blurring an image by a Gaussian function. It is a widely used effect in graphics software, typically to reduce image noise and reduce detail. It is also used as a preprocessing stage before applying our machine learning or deep learning models. E.g. of a Gaussian kernel(3×3)

Median Blur: The Median Filter is a non-linear digital filtering technique, often used to remove noise from an image or signal. Median filtering is very widely used in digital image processing because, under certain conditions, it preserves edges while removing noise. It is one of the best algorithms to remove Salt and pepper noise.

Bilateral Blur: A bilateral filter is a non-linear, edge-preserving, and noise-reducing smoothing filter for images. It replaces the intensity of each pixel with a weighted average of intensity values from nearby pixels. This weight can be based on a Gaussian distribution. Thus, sharp edges are preserved while discarding the weak ones.

Bilateral Filtering
A bilateral filter is used for smoothening images and reducing noise while preserving edges. However, these convolutions often result in a loss of important edge information, since they blur out everything, irrespective of it being noise or an edge. 
OpenCV has a function called bilateralFilter() with the following arguments:

d: Diameter of each pixel neighborhood.
sigmaColor: Value of 
σ
    
σ     in the color space. The greater the value, the colors farther to each other will start to get mixed.
sigmaColor: Value of 
σ
    
σ     in the coordinate space. The greater its value, the more further pixels will mix together, given that their colors lie within the sigmaColor range.
