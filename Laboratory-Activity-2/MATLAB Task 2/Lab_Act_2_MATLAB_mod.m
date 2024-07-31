% Read an image
img = imread('flower.jpg');
figure(1);
imshow(img); 
title('Original Image');

% Using different arithmetic operations (-, *)
subImg = img - 50;
mulImg = img * 50; 

% Geometric operations (imrotate)
angle = 45;
rotImg = imrotate(img, angle);

% Displaying individual color channels for RGB images
% Red channel
figure(2);
imshow(img(:, :, 1)); 
title ('Red Channel');

% Green channel
figure(3);
imshow(img(:, :, 2));
title('Green Channel');

% Blue channel
figure(4);
imshow(img(:, :, 3));
title('Blue Channel');

% Display rotated image
figure(5);
imshow(rotImg);
title('Rotated Image');

% Display subtracted image
figure(6);
imshow(subImg);
title('Subtracted Image');

% Display multiplied image
figure(7);
imshow(mulImg);
title('Multiplied Image');


