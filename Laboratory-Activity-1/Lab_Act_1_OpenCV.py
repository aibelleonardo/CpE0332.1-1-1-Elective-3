import cv2

#Acquire the image
img = cv2.imread('flower.jpg')

#Rotate the image by 30 degrees
#Get image dimensions
(h, w) = img.shape[:2] 
(centerX, centerY) = (w // 2, h // 2)

#Define the rotation matrix
angle = 30  #angle in degrees
scale = 1  #scale factor
rotation_matrix = cv2.getRotationMatrix2D((centerX, centerY), angle, scale)

#This function rotates the image by 30 degrees
rotated_image = cv2.warpAffine(img, rotation_matrix, (w, h))

#Flip the image horizontally
flipped_img = cv2.flip(rotated_image, 1)

#Display images
cv2.imshow('Original Image', img)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Rotated & Flipped Image', flipped_img)
#Wait until user presses exit
cv2.waitKey(0)