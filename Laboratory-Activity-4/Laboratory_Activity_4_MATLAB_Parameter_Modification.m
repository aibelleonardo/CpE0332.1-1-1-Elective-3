

img = imread('flower.jpg'); 

figure(1);
imshow(img);
title('Original Image');

if size(img, 3) == 3
    img_gray = rgb2gray(img); 
else
    img_gray = img;
end

figure(2);
imshow(img_gray); title('Grayscale');

h_gaussian = fspecial('gaussian', [5, 5], 10); 
img_gaussian_filtered = imfilter(img_gray, h_gaussian);

figure; 
imshow(img_gaussian_filtered);
title('Filtered Image with Experimented Value (Gaussian)');

figure; 
imhist(img_gaussian_filtered);
title('Histogram of the Experimented Value (Gaussian Filtered)');

img_noisy_exp1 = imnoise(img_gray, 'gaussian', 0.5);
img_noisy_exp2 = imnoise(img_gray, 'gaussian', 0.1);

figure; 
imshow(img_noisy_exp1);
title('Noisy Using Experimented Value (Gaussian is 0.5)');

figure; 
imshow(img_noisy_exp2);
title('Noisy Using Experimented Value (Gaussian is 0.1)');

figure;
imhist(img_noisy_exp1);
title('Histogram of Noisy Image Experimented Value 1');

figure; 
imhist(img_noisy_exp2);
title('Histogram of Noisy Image Experimented Value 2');