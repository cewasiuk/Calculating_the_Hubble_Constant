
bb = 29; % block size
nn = numel(hbig);
cc = mat2cell(hbig,diff([0:bb:nn-1,nn]));
zz = cellfun(@median,cc);