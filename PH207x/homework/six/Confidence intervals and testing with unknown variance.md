#Confidence intervals and testing with unknown variance#
Suppose now that we are interested in the distribution of hemoglobin levels in Mumbai. We decide that it is unreasonable to extrapolate the Delhi results to Mumbai, and therefore the population standard deviation is unknown. We take a random sample of 15 children in Mumbai. The sample mean is xˉ=115 g/L, with sample standard deviation s=10.2 g/L. Assume hemoglobin levels in Mumbai are normally distributed (we could check this by looking at the distribution of hemoglobin levels in other similar populations). 

> n= 15  
> xˉ= sample mean= 115 g/L
> s= sample standard deviation= 10.2 g/L


1. Construct a two-sided 95% confidence interval for μ.
> t_15-1,0.995= 1.96  
> x⁻ +- t_15-1,0.9955 * s/SQRT(n)= 115 +- 1.96*10.2/sqrt(15)

	di 115+1.96*10.2/sqrt(15)
	di 115-1.96*10.2/sqrt(15)
> => **[ 109.83809, 120.16191 ]**

> test: cii 15 115 10.2, level(95)


2. Use the confidence interval in question 1 above to answer the following questions:

* Would you reject the null hypothesis that the mean hemoglobin level is equal to 108 g/L, versus the alternative that the mean is not equal to 108 g/L, at the **α=0.05** level?

> μ_0= 108  
> Reject if Z is > 1.96 or < -1.96, then Pr(reject H_0 when true) = α = 0.05
> z= (x⁻ - μ_0) / (s/SQRT(n))= (115 - 108) / (10.2/sqrt(15))= **2.6579297**

> z > 1.96

> => **yes**  
> no  
> not enough information 


* Would you reject the null hypothesis that the mean hemoglobin level is equal to 108 g/L, versus the alternative that the mean is not equal to 108 g/L, at the **α=0.01** level?

> yes  
> no  
> => **not enough information**


* Would you reject the null hypothesis that the mean hemoglobin level is equal to 108 g/L, versus the alternative that the mean is not equal to 108 g/L, at the **α=0.1** level?

> => **yes**  
> no  
> not enough information 


3. Conduct a one-sample t-test to test the null hypothesis that the mean hemoglobin level is equal to 108 g/L, versus the alternative that the mean is not equal to 108 g/L, at the α=0.01 level.
> μ_0= 108  

	ttesti 15 115 10.2 108


* What is your test statistic? 
> => **t = 2.6579**

* Under the null hypothesis, the test statistic follows a t-distribution with how many degrees of freedom? 
> => **degrees of freedom = 14**

* What is your p-value?
> => **0.0187**

* What do you conclude?
> => **fail to reject the null hypothesis**


