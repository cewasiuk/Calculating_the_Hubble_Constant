%Christoffel Symbol Attempt
% Define the metric and inverse metric:
g = [-(1-rs/r) 0 0 0 ; 0 (1-rs/r)^(-1) 0 0 ; 0 0 r^2 0 ; 0 0 0 r^2*sin(theta)^2]
ginv = g^(-1)
% Define the coordinates
coords = [t ; r ; theta ; phi]
G = zeros
for i = 1:4
    for j = 1:4
        for k = 1:4
            for l = 1:4
                G(i,j,k) = 1/2*ginv(i,l)*(diff(g(l,j),coords(k))+diff(g(l,k),coords(j))-diff(g(j,k),coords(l)))
            end
        end
    end
end