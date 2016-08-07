moon=im2double(rgb2gray(imread('moon.jpg')));
I =compute_In(moon);
imshow(I/I(end,end));