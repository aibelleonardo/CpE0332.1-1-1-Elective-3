import cv2
import numpy as np

# Load the original image
img = cv2.imread('flower.jpg')

# Convert to grayscale if the image is BGR
if img.shape[2] == 3:
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
else:
    grayImg = img
    
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

# Gaussian Blur
# Define Gaussian kernel
kernel_size = (5, 5)
sigma = 10
h_gaussian = cv2.getGaussianKernel(kernel_size[0], sigma)
h_gaussian = h_gaussian * h_gaussian.T  # Convert to 2D Gaussian kernel

# Apply Gaussian filter
gaussianImg = cv2.filter2D(grayImg, -1, h_gaussian)

# Histogram of Gaussian Blur
gaussianHist = cv2.calcHist([gaussianImg], [0], None, [256], [0, 256])
gaussianHistImg = create_histogram(gaussianHist)

# Noisy Experiment 1
varNoise1 = np.sqrt(0.5)
noise1 = np.random.normal(0, varNoise1, grayImg.shape).astype('uint8')
noisyImg1 = cv2.add(grayImg, noise1)

# Histogram of Noisy Experiment 1
noisy1Hist = cv2.calcHist([noisyImg1], [0], None, [256], [0, 256])
noisy1HistImg = create_histogram(noisy1Hist)

# Noisy Experiment 2
varNoise2 = np.sqrt(0.1)
noise2 = np.random.normal(0, varNoise2, grayImg.shape).astype('uint8')
noisyImg2 = cv2.add(grayImg, noise2)

# Histogram of Noisy Experiment 2
noisy2Hist = cv2.calcHist([noisyImg2], [0], None, [256], [0, 256])
noisy2HistImg = create_histogram(noisy2Hist)

# Display images and histograms
cv2.imshow('Original Image', img)
cv2.imshow('Grayscale', grayImg)
cv2.imshow('Filtered Image with Experimented Value (Gaussian)', gaussianImg)
cv2.imshow('Histogram of the Experimented Value (Gaussian Filtered)', gaussianHistImg)
cv2.imshow('Noisy Using Experimented Value (Gaussian is 0.5)', noisyImg1)
cv2.imshow('Noisy Using Experimented Value (Gaussian is 0.1)', noisyImg2)
cv2.imshow('Histogram of Noisy Image Experimented Value 1', noisy1HistImg)
cv2.imshow('Histogram of Noisy Image Experimented Value 2', noisy2HistImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
