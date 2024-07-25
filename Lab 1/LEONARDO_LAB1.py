import cv2
import numpy as np

img = cv2.imread('flower.jpg')

(h, w) = img.shape[:2]
center = (w / 2, h / 2)
M = cv2.getRotationMatrix2D(center, 30, 1.0)
rotated_img = cv2.warpAffine(img, M, (w, h))

flipped_img = cv2.flip(rotated_img, 1)

max_height = max(img.shape[0], rotated_img.shape[0], flipped_img.shape[0])

combined_width = img.shape[1] + rotated_img.shape[1] + flipped_img.shape[1]
combined_img = np.zeros((max_height, combined_width, 3), dtype = np.uint8)

combined_img[:img.shape[0], :img.shape[1]] = img
combined_img[:rotated_img.shape[0], img.shape[1]:img.shape[1] + rotated_img.shape[1]] = rotated_img
combined_img[:flipped_img.shape[0], img.shape[1] + rotated_img.shape[1]:] = flipped_img

cv2.imshow('Combined Image', combined_img)

cv2.imwrite('combined_image.jpg', combined_img)

cv2.waitKey(0)
cv2.destroyAllWindows()