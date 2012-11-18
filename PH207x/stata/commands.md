# Commands in Stata

## Distribution - Binomial, Poisson and Normal

### Suppose X ~ Binomial(n,p)  
> binomialp(n,k,p) - returns the probability of observing k successess - P(X=k)  
> binomial(n,k,p) - returns the probability of observing k or fewer successes - P(X<=k)  
> binomialtail(n,k,p) - return the probability of observing floor(k) or more successes - P(X>=k)

### Suppose X ∼ Poisson(m)  
> poissonp(m,k) - returns the probability of observing floor(k) or fewer successes - P(X=k)  
> poisson(m,k) - returns the probability of observing floor(k) or fewer successes - P(X<=k)  
> poissontail(m,k) - returns the probability of observing floor(k) or more successes - P(X>=k)

### Suppose Z ~ Normal(0,1)  
> normal(z) - return the cumulative standard normal distribution - P( Z<z )  
> normalden(z) - returns the standard normal density

### Distribution Table in Stata

	clear all
	set obs 5
	gen k=_n-1
	gen p = binomialp(2000,k,0.00065)
	list k p


 x | p 
---|-----------
 0 |  .2724166
 1 |   .354372
 2 |  .2303763
 3 |  .0997948
 4 |  .0324057


## Sampling Distribution

	set seed 7234234234
	sample 49, count

	use "framingham_dataset.dta"
	summ death angina totchol1 sysbp1 diabp1 bmi1 glucose1

### Central Limit Theorem

#### First Sample Set ####

	sum bmi1
	drop if bmi1 == .
	keep bmi1
	preserve
	sample 20, count
	summarize

#### Second Sample Set ####

	. restore
	. preserve
	sample 20, count
	sum bmi1

#### Third Sample Set ####

	. restore
	. preserve
	sample 100, count
	sum bmi1

#### Fourth Sample Set - Check again ####

	. restore
	. preserve
	sample 100, count
	sum bmi1

#### Compare Histograms (Continued vs. Binary) ####

	use "framingham_dataset.dta"
	. histogram bmi1
	. histogram prevmi1


## Confidence and Predictive Intervals

### Example: BMI in Framingham
X~Normal(μ, σ²)

##### Q1. Construct a 95% predictive interval for X #####
	   

>	sum bmi1

    Variable |       Obs  |      Mean  |  Std. Dev.  |     Min   |     Max
-------------|------------|------------|-------------|-----------|---------
        bmi1 |      4415  |  25.84616  |  4.101821   |   15.54   |    56.8

> [ x⁻-1.96*σ/SQRT(n), x⁻+1.96*σ/SQRT(n), ]  
>	di 25.84616  
> 25.84616

>	di 25.84616 - 1.96*4.101821  
> 17.806591

>	di 25.84616 + 1.96*4.101821
> 33.885729





##### Q2. Suppose we now draw repeated samples of size 100 from the Framingham cohort. What is a 95% predictive interval for the sample mean? #####
	   

##### Q3. Take a sample of size 100. Construct a 95% configence interval for μ. #####
	   


##### Q1. Construct a 95% predictive interval for X #####
	   

