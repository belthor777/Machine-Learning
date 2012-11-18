# Sampling Distributions  
## Central limit theorem

> sd= σ/SQRT(n)
> z= (x⁻ - μ) / sd

> x⁻ >= 260  
> z= 260-μ / ( σ/SQRT(25) )= 2.57

	di 1-normal(2.57)

> z= 0.00508483

> So the probability of getting a sample mean of 260 or higher when taking a sample of 25 is about 0.5%

## Sample Size  
How big a sample do we need to be 95% sure that the sample mean for total cholesterol level is within +- 25mg/100ml of the population mean?

> P_r{ -25 <= x⁻-μ <) 25 }= 0.95
> P_r{ -25/(44.7/SQRT(n)) <= (x⁻-μ)/(44.7/SQRT(n) <= 25/(44.7/SQRT(n)) }= 0.95

> => 25/(44.7/SQRT(n))= 1.96
> => n=12.3 => n= 13

> So, in general if we want to be 95% sure that the sample mean will be within +- delta of the population mean, then we need a sample of size

> n= ( (1.96*σ) / delta )^2

> where σ is the population standard deviation

##  Confidence Interval  
Is a 95% confidence interval for μ. In other words it is a rule that has a 95% chance of success - success being measured

> σ is known

> [ x⁻-1.96*σ/SQRT(n), x⁻+1.96*σ/SQRT(n), ]


## Predictive vs. Confidence Interval 

> Z= (X-μ) / σ

> So, [ μ-1.96*σ, μ+1.96*σ ]  
> is a predictive interval (95%) for X, just as  
>	[ μ-1.96*σ/SQRT(n), μ+1.96*σ/SQRT(n), ]
> is a predictive interval for x⁻, and  
>	[ x⁻-1.96*σ/SQRT(n), x⁻+1.96*σ/SQRT(n), ]
> is a confidence interval for μ


## Width of Confidence Intervals 

Length  | Formular             | width
------- | -------------------- | --------
 95%    | x⁻+-1.96*σ/SQRT(n)   | 3.92*σ/SQRT(n)
 99%    | x⁻+-2.58*σ/SQRT(n)   | 5.16*σ/SQRT(n)

n       | 95% CI for μ         | Interval width
------- | -------------------- | --------
 10     | x⁻+-0.620*σ          | 1.240*σ
 100    | x⁻+-0.196*σ          | 0.392*σ
 1000   | x⁻+-0.062*σ          | 0.124*σ

> Smaller is σ, the tighter are the bounds - more homogeneous


## Unknown variance: the t distribution - Student's T
What if is σ is unknown

> t= (x⁻-μ) / (s/sqrt(n))  
> has n-1 degrees of freedom

> **Sample**:	size n
>		sample mean x⁻
>		sample standard deviation s

> **Population**:	X is approx. normal
>		mean μ
>		standard deviation σ


## Questions to Confidence and Predictive Intervals ##
Again, let X denote BMI at baseline for a Framingham study participant. Assume X is normally distributed.


#### Q1. Calculate a 90% predictive interval for X. ####
> 90% is between -1.64 and +1.64  
> [ x⁻-1.64*σ/SQRT(n), x⁻+1.64*σ/SQRT(n), ]

	set seed 2  
	sample 20, count  
	sum bmi1


    Variable |       Obs  |      Mean  |  Std. Dev.  |     Min   |     Max
-------------|------------|------------|-------------|-----------|---------
        bmi1 |      4415  |  25.84616  |  4.101821   |   15.54   |    56.8

>	di 25.84616 - 1.64*4.101821  
>	di 25.84616 + 1.64*4.101821
> => **[19.119174, 32.573146 ]**


#### Q2. For a random sample of size 10, calculate a 90% predictive interval for the sample mean of X. ####
> n= 10  

>	sample 10, count
>	set seed 2
>	sum bmi1

    Variable |       Obs  |      Mean  |  Std. Dev.  |     Min   |     Max
-------------|------------|------------|-------------|-----------|---------
        bmi1 |        10  |    26.328  |  3.781084   |   20.88   |   32.29

>	di 26.328 - 1.64*4.101821  
>	di 26.328 + 1.64*4.101821
> => **[19.601014, 33.054986 ]**


#### Q3. For normally distributed random variables with known variance, the width of the 90% predictive interval for the sample mean is equal to the width of a 90% confidence interval for the population mean. ####
> => **True**
> False 




