% P(B|A) = P(A|B) * P(B) / P(A)
function p_of_B_given_A = bayesrule(p_of_A_given_B, p_of_A, p_of_B)
	p_of_B_given_A = p_of_A_given_B * p_of_B / p_of_A;
end