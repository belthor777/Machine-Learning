% P(x) = P(x|A) * P(A) + P(x|!A) * P(!A)
function tpx = totalprob(p_of_x_given_A, p_of_x_given_not_A, p_of_A)
	tpx = p_of_x_given_A * p_of_A + p_of_x_given_not_A * (1 - p_of_A);
end