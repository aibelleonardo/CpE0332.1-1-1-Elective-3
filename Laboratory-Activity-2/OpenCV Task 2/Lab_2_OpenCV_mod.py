import cv2

# Read the image
img = cv2.imread('flower.jpg')

# Get image dimensions and center
height, width = img.shape[:2]
centerX, centerY = width // 2, height // 2

# Rotate the image by an angle
angle = 45
scale = 0.7 # 0.7 is used to fit the image inside the window
rotMatrix = cv2.getRotationMatrix2D((centerX, centerY), angle, scale)
rotImg = cv2.warpAffine(img, rotMatrix, (width, height))

# Create a darkened image by subtracting a constant value
constVal = 50
darkImg = cv2.subtract(img, constVal)

# Create a multiplied image
multipliedImg = cv2.multiply(img, 50)

# Extract and display color channels (BGR is the default in OpenCV)
redChannel = img[:, :, 2]
greenChannel = img[:, :, 1]
blueChannel = img[:, :, 0]

# Display images
cv2.imshow('Original Image', img)
cv2.imshow('Red Channel Image', redChannel)
cv2.imshow('Green Channel Image', greenChannel)
cv2.imshow('Blue Channel Image', blueChannel)
cv2.imshow('Rotated Image', rotImg)
cv2.imshow('Subtracted Image', darkImg)
cv2.imshow('Multiplied Image', multipliedImg)

cv2.waitKey(0)
