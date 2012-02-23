# Uniform-Probability-Quiz 
# Robot Localization

# We have 5 different cells where each cell has the same probability that the robot might be in that cell.
# So probabilities add up to 1
# Quiz from x1 to x5
# -> What is the probability of any of those x's?
import decimal

n = decimal.Decimal(5)
p_xi = 1/n
print "-> The probability of any of x's is %f" % p_xi
