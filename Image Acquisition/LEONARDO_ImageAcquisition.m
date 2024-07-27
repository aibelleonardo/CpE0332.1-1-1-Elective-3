img = imread('orange.png');

figure(1);
imshow(img);


redImg = img;
redImg(:, :, 2) = 0;
redImg(:, :, 3) = 0;
figure(2);
imshow(redImg);


greenImg = img;
greenImg(:, :, 1) = 0;
greenImg(:, :, 3) = 0;
figure(3);
imshow(greenImg);


blueImg = img;
blueImg(:, :, 1) = 0;
blueImg(:, :, 2) = 0;
figure(4);
imshow(blueImg);


grayImg = rgb2gray(img);
figure(5);
imshow(grayImg);

whos img;
whos redImg;
whos greenImg;
whos blueImg;
whos grayImg;

imwrite(img, 'orange.png');
imwrite(redImg, 'redImg.png');
imwrite(greenImg, 'greenImg.png');
imwrite(blueImg, 'blueImg.png');
imwrite(grayImg, 'grayImg.png');

imwrite(img, 'orange.png', 'jpg', 'Quality', 100);
imwrite(redImg, 'redImg.png', 'jpg', 'Quality', 100);
imwrite(greenImg, 'greenImg.png', 'jpg', 'Quality', 100)
imwrite(blueImg, 'blueImg.png', 'jpg', 'Quality', 100);
imwrite(grayImg, 'grayImg.png', 'jpg', 'Quality', 100);