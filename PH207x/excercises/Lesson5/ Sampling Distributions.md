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
is a 95% confidence interval for μ


