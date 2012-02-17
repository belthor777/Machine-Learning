%    A
%   / \
%  B   C
% P(B|C) = P(B|A) * P(A|C) + P(C|!A) * P(!A|C)
function p_of_B_given_C = bayesruleci(...
	p_of_A, ...
	p_of_B_given_A, ...
	p_of_B_given_not_A, ...
	p_of_C_given_A, ...
	p_of_C_given_not_A)
	
	p_of_C = totalprob(p_of_C_given_A, p_of_C_given_not_A, p_of_A)
	
	p_of_A_given_C = bayesrule(p_of_C_given_A, p_of_C, p_of_A)
	p_of_not_A_given_C = bayesrule(p_of_C_given_not_A, p_of_C, (1 - p_of_A))
	
	p_of_B_given_C = p_of_B_given_A * p_of_A_given_C + p_of_B_given_not_A * p_of_not_A_given_C
end