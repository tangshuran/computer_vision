function I = compute_In(img)
I=cumsum(cumsum(img,1),2);
   
end