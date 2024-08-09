import cv2
import numpy as np

#Original
img = cv2.imread('flower.jpg')

# Convert to grayscale if the image is BGR  
if img.shape[2] == 3:
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
else:
        grayImg = img

#Motion Blur
def motionBlurKernel(size):
    kernel = np.zeros((size, size))
    kernel[int((size - 1) / 2), :] = np.ones(size)
    kernel = kernel / size
    return kernel
motionBlurredImg = cv2.filter2D(grayImg, -2, motionBlurKernel(15))

#Gaussian Blur
gaussianImg = cv2.GaussianBlur(grayImg, (15, 15), 0)

#Sharpen
sharpen = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpenedImg = cv2.filter2D(grayImg, -1, sharpen)

#Noisy
noise = np.random.normal(0, 1, grayImg.shape).astype('uint8')
noisyImg = cv2.add(grayImg, noise)

#Denoise
denoisedImg = cv2.medianBlur(noisyImg, 5)

cv2.imshow('Original Image', img)
cv2.imshow('Grayscale', grayImg)
cv2.imshow('Motion Blurred Image', motionBlurredImg)
cv2.imshow('Filtered Image (Gaussian)', gaussianImg)
cv2.imshow('Sharpened Image', sharpenedImg)
cv2.imshow('Noisy', noisyImg)
cv2.imshow('Noise Removed', denoisedImg)

#Deblurred
motionBlurredImg = cv2.filter2D(grayImg, -2, motionBlurKernel(8))
cv2.imshow('Deblurred Image', motionBlurredImg)


cv2.waitKey(0)