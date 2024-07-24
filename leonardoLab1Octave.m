pkg load image;

image_path = 'C:\\Users\\AIBEL\\Desktop\\Elective 3 Lab';
img = imread('flower.jpg');

rotated_img = imrotate(img, 30);

flipped_img = fliplr(rotated_img);

figure(1);
imshow(img);
title('Original Image');

figure(2);
imshow(rotated_img);
title('Rotated 30°');

figure(3);
imshow(flipped_img);
title('Rotated & Flipped');
