import cv2

# Read an image
img = cv2.imread('flower.jpg')

# Get image dimensions (rows, columns, color channels) 
dim = img.shape

# Access individual pixels (example: center pixel) 
centerRow = dim[0] // 2
centerCol = dim[1] // 2

centerPix = img[centerRow, centerCol]

# Declaring a value for brightness
constVal = 50

# An arithmetic function (+) will increase the brightness by 50 to all pixels
brightImg = cv2.add(img, constVal)

# Flip an image horizontally (1)
flippedImg = cv2.flip(img, 1)

# Display dimensions (rows, columns, color channels) 
print("\nImage size: ", dim[0], " x ", dim[1], " x ", dim[2])

# Check and display color model
if dim[2] == 1: 
    # If the third index is equal to 1, then, the image is in grayscale
    print("Color Model: Grayscale")
else:
    # Access 3rd index to check if the image is BGR or grayscale
    print("Color Model: BGR")
# Print the center pixel
print("Center pixel: ", str(centerPix)) 

# Display the image 
cv2.imshow('Original Image', img)
cv2.imshow('Image Brightened',  brightImg)
cv2.imshow('Image Flipped Horizontally', flippedImg)
cv2.waitKey(0)