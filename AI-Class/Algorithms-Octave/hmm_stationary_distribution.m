%{
	Pardon the crude ASCII art but this is supposed to be a hidden Markov model
	
   .--. .----.     .--.
   `->(A)<-.  `->(B)<-'
            `----'
			
	Derivation:
	
	X = P(A_t) = P(A_t-1) = p_of_A_inf
	X = p_of_A_given_A * X + p_of_A_given_B * ( 1 - X)
	X = p_of_A_given_A * X + p_of_A_given_B - p_of_A_given_B * X
	X =  * X + p_of_A_given_B
	(1 - (p_of_A_given_A  - p_of_A_given_B)) * X = p_of_A_given_B
	X = p_of_A_given_B / (1 - (p_of_A_given_A - p_of_A_given_B))
%}
function p_of_A_inf = hmm_stationary_distribution(p_of_A_given_A, p_of_A_given_B)
	p_of_A_inf = p_of_A_given_B / ( 1 - ( p_of_A_given_A - p_of_A_given_B ) );
end