function [w0, w1] = linReg(x, y)

% Function to calculate W0 and W1 of two vectors based on Ai-Class Lectures

% Initialize some useful values
m = length(y); %number of training examples

% You need to return the following variables correctly
w0 = 0;
w1 = 0;

w1 = ((m*(x'*y)) - (sum(x) * sum(y))) / ((m * sum(x.^2)) - sum(x)^2);
w0 = ((1/m) * sum(y)) - ((w1 / m) * sum(x));

w0
w1

end