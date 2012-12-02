#  Tutorial: One-sample proportions #

## Confidence Intervals ##
> *ci* and *cii* calculate **binomial confidence** intervals

## Hypothesis Tests ##
> *bitest* and *bitesti* **exact binomial** one-sample proportion hypothesis test  
> *prtest* and *prtesti* **large sample one sample** proportion hypothesis test

### 1. We're going to do is estimate the proportion of California residents who visit the doctor at least once in the previous year. Lets denote this p. ###
> For small samples use exact and for big samples use Wald methods.  

	ci doctor, binomial
	ci doctor, binomial wald
	ci doctor, binomial wilson


#### Is it reasonable to use the wald interval? ####
> n*p > 5  
> 500*0.804= 402   
> **So its higher than 5!**  
> **It is the easted to calculate, so we see this in reality very often**


#### We'll look at these confidence intervals and decide whether there's evidence that at the 95% confidence level, do we think that at least 80% of the population visits the doctor once per year. ####



