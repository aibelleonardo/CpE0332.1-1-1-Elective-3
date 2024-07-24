img = imread('flower.jpg');

% Rotate by 45 degrees
rotImg = imrotate(img, 45);

% Flip horizontally
flipImg = fliplr(rotImg);

% Display results
figure(1);
plot(1, 1);
imshow(img);
title('Original Image');

figure(2);
plot(1, 1);
imshow(rotImg);
title('Rotated 45°'); 

figure(3); 
plot(1, 1);
imshow(flipImg); 
title('Rotated & Flipped');