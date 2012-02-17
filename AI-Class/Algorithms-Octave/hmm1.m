%{
    Pardon the crude ASCII art but this is supposed to be a hidden Markov model

   .--. .----.     .--.
   `->(A)<-.  `->(B)<-'
      / \   `---'/ \
     x   y      x   y

%}
function p_of_A1_given_x1 = hmm1(...
	p_of_A0, ...
	p_of_A_given_A, ...
	p_of_A_given_B, ...
	p_of_x_given_A, ...
	p_of_x_given_B)	
	
	p_of_A1 = totalprob(p_of_A_given_A, p_of_A_given_B, p_of_A0);
	p_of_x1 = totalprob(p_of_x_given_A, p_of_x_given_B, p_of_A1);
	p_of_A1_given_x1 = bayesrule(p_of_x_given_A, p_of_x1, p_of_A1);
end