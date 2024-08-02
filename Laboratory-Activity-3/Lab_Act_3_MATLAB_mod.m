% Convert to grayscale if the image is RGB  
if size(img, 3) == 3 
img_gray = rgb2gray(img);  
else 
img_gray = img; 
end 
% Filtering using average filter but different values  
h_avg = fspecial('average', [10, 10]); % Original is [5,5]  
img_avg_filtered = imfilter(img_gray, h_avg); 
% Show the experimented image  
figure;  
imshow(img_avg_filtered); 
title('Filtered Image (Using Average but Different values)'); 
% Filtering using median filter 
img_median_filtered = medfilt2(img_gray, [1, 10]); % Original is [5,5] 
% Display the median filtered image  
figure; imshow(img_median_filtered); 
title('Experimented Filtered Image (Median)'); 
% Show the Histogram  
figure; 
imhist(img_median_filtered); 
title('Histogram of Experimented Median Filtered)'); 
