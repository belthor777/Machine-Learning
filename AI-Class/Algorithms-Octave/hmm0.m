%{
    Pardon the crude ASCII art but this is supposed to be a hidden Markov model

   .--. .----.     .--.
   `->(A)<-.  `->(B)<-'
      / \   `---'/ \
     x   y      x   y

%}
function p_of_A0_given_x0 = hmm0(...
	p_of_A0, ...
	p_of_x_given_A, ...
	p_of_x_given_B)	
	
	p_of_x0 = totalprob(p_of_x_given_A, p_of_x_given_B, p_of_A0);
	p_of_A0_given_x0 = bayesrule(p_of_x_given_A, p_of_x0, p_of_A0);
end