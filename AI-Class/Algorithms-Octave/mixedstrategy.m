% M must be 2x2 grid
% p is the Max : 1 value
% q is the Min : 1 value
% u is the U_max value
function [p,q,u] = mixedstrategy(M)

	p = (M(2,2) - M(2,1))/(M(1,1) - M(2,1) - M(1,2) + M(2,2));
	q = (M(2,2) - M(1,2))/(M(1,1) - M(1,2) - M(2,1) + M(2,2));
	u = p*q*M(1,1) + (1-p)*q*M(2,1) + p*(1-q)*M(1,2) + (1-p)*(1-q)*M(2,2);

end