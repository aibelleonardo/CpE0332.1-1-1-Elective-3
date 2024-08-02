import cv2
import numpy as np

# Original Image
img = cv2.imread('flower.jpg')

# Convert to grayscale if the image is BGR  
if img.shape[2] == 3:
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
else:
        grayImg = img

# Contrast Enhanced Image
enhance = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))  # CLAHE: Contrast Limited Adaptive Histogram Equalization
contrastEnhImg = enhance.apply(grayImg)

# Equalized Image
equalizedImg = cv2.equalizeHist(grayImg)

# Filtering using average filter with updated kernel size
kernelSize = (10, 10)  # Updated to 10 pixels wide and 10 pixels tall
aveFilImg = cv2.blur(grayImg, kernelSize)

# Median Filter with an odd kernel size
kernelSizeMF = 11  # Must be an odd number
medFilImg = cv2.medianBlur(grayImg, kernelSizeMF)

# Function to create histogram with white background, blue bars, border, and axis labels
def create_histogram(hist):
    # Define the size of the histogram image
    histImageWidth = 600  
    histImageHeight = 500  
    histImage = np.ones((histImageHeight, histImageWidth, 3), dtype=np.uint8) * 255
    
    # Normalize the histogram
    max_val = np.max(hist)
    cv2.normalize(hist, hist, 0, histImageHeight - 40, cv2.NORM_MINMAX)
    
    # Draw the histogram with blue bars
    for i in range(256):
        height = int(hist[i])
        cv2.line(histImage, (i * 2 + 50, histImageHeight - 30), 
                 (i * 2 + 50, histImageHeight - 30 - height), (255, 0, 0), 2)
    
    # Draw border
    cv2.rectangle(histImage, (0, 0), (histImageWidth - 1, histImageHeight - 1), (0, 0, 0), 2)
    
    # Draw x-axis line
    cv2.line(histImage, (50, histImageHeight - 30), (histImageWidth - 10, histImageHeight - 30), (0, 0, 0), 2)
    
    # Draw y-axis line
    cv2.line(histImage, (50, histImageHeight - 30), (50, 10), (0, 0, 0), 2)
    
    # Add x-axis values and lines
    for i in range(0, 256, 50):  # x-axis ticks every 50 pixels
        x = i * 2 + 50
        if x < histImageWidth - 30:  # Ensure label fits within image width
            cv2.putText(histImage, str(i), (x, histImageHeight - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            # Draw vertical lines for x-axis ticks
            cv2.line(histImage, (x, histImageHeight - 30), 
                     (x, histImageHeight - 35), (0, 0, 0), 1)
    
    # Add y-axis values and lines
    for i in range(0, 1200, 200):  # y-axis ticks every 200 frequency values
        y = histImageHeight - 30 - int(i * (histImageHeight - 40) / 1000)
        if y > 20:  # Ensure label fits within image height
            cv2.putText(histImage, str(i), (10, y + 5), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            # Draw horizontal lines for y-axis ticks
            cv2.line(histImage, (45, y), 
                     (50, y), (0, 0, 0), 1)
    
    return histImage

# Calculation of Histograms
histGrayImg = cv2.calcHist([grayImg], [0], None, [256], [0, 256])
histEnhImg = cv2.calcHist([contrastEnhImg], [0], None, [256], [0, 256])
histEqualizedImg = cv2.calcHist([equalizedImg], [0], None, [256], [0, 256])
histAveFilImg = cv2.calcHist([aveFilImg], [0], None, [256], [0, 256])
histMedFilImg = cv2.calcHist([medFilImg], [0], None, [256], [0, 256])

# Create histogram images
histogramOfGrayImg = create_histogram(histGrayImg)
histogramOfEnhImg = create_histogram(histEnhImg)
histogramOfEqualImg = create_histogram(histEqualizedImg)
histogramOfAveFilImg = create_histogram(histAveFilImg)
histogramOfMedFilImg = create_histogram(histMedFilImg)

# Display images and histograms 
cv2.imshow('Original Image', img)
cv2.imshow('Grayscale Image', grayImg)
cv2.imshow('Contrast Enhanced Image', contrastEnhImg)
cv2.imshow('Equalized Image', equalizedImg)
cv2.imshow('Filtered Image (Using Average but Different values)', aveFilImg)
cv2.imshow('Experimented Filtered Image (Median)', medFilImg)
cv2.imshow('Histogram of Grayscale Image', histogramOfGrayImg)
cv2.imshow('Histogram of Enhanced Image', histogramOfEnhImg)
cv2.imshow('Histogram of Equalized Image', histogramOfEqualImg)
cv2.imshow('Histogram of Average Filtered', histogramOfAveFilImg)
cv2.imshow('Histogram of Experimented Median Filtered', histogramOfMedFilImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
