b = 617; % block size
n = numel(h);
c = mat2cell(h,diff([0:b:n-1,n]));
z = cellfun(@median,c);