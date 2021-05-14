freq = [];
maxi = [];
for i = 1:377
    mf = meanfreq(c{i,1},1/0.00025);
    freq = [freq ; mf];
    
    maxh = max(c{i,1});
    maxi = [maxi ; maxh];
   
    
end
    
    
    