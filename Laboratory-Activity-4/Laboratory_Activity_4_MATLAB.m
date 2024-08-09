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

len = 21;
theta = 11;
psf = fspecial('motion', len, theta);
img_blur = imfilter(img_gray, psf, 'conv', 'circular');

figure(3); 
imshow(img_blur);
title('Motion Blurred Image');

h_gaussian = fspecial('gaussian', [5, 5], 1); 
img_gaussian_filtered = imfilter(img_blur, h_gaussian);

figure(4); 
imshow(img_gaussian_filtered); 
title('Filtered Image (Gaussian)');

img_sharpened = imsharpen(img_blur);

figure(5); 
imshow(img_sharpened); 
title('Sharpened Image');

img_noisy = imnoise(img_gray, 'gaussian', 0.02); 
img_noisy_removed = medfilt2(img_noisy, [5, 5]);

figure(6);
imshow(img_noisy); 
title('Noisy');

figure(7); 
imshow(img_noisy_removed); 
title('Noise Removed');

estimated_nsr = 0.01;
img_deblurred = deconvwnr(img_blur, psf, estimated_nsr); 

figure(8);
imshow(img_deblurred);
title("Deblurred Image");