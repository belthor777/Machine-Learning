# Central Limit Theorem and Confidence Intervals #
According to the WHO Global Database on Anaemia, the mean hemoglobin levels among primary school children in Delhi were estimated at μ=108 g/L, with standard deviation σ=12.5 g/L. (Source: http://who.int/vmnis/anaemia/data/database/countries/ind_ida.pdf)

Suppose we took a random sample of 75 primary school children in Delhi. Denote the mean hemoglobin levels in this sample as xˉ. Throughout this question, assume that the sample size is large enough that the Central Limit Theorem is applicable and that σ is known. 

> μ=population= 108 g/L  
> σ=standard deviation= 12.5 g/L  
> n=sample size= 75  
> xˉ= mean hemoglobin levels= ?

1. According to the Central Limit Theorem, what is the expected value (mean) of xˉ?
Hints: see https://www.edx.org/static/content-harvard-id270x/handouts/JotterWeek5.390aec581f74.pdf in which it is written that as per the CLT, in the xˉdistribution μ is the mean.
Hint2: check SAMPLING DISTRIBUTIONS 10:50

> x ̄ ∼ N (μ, σ/ n)  
> x ̄ ~ N( 108, 1.4433757 )  
> x ̄ ~ **108**


2. According to the Central Limit Theorem, what is the standard deviation of xˉ?
Hints: The standard deviation of the sample mean is also known as standard error, see the hyperlink given in Q1.
Hint2: check SAMPLING DISTRIBUTIONS 11:04

sd= σ/SQRT(n)= 12.5/sqrt(75)= **1.4433757**


3. Suppose we take a large number of samples of size 75. What proportion of the samples would we expect to have a sample mean xˉ that lies between 106 and 110 g/L?
Hints:  [106 < xbar < 110]= (110-108)/σ/sqrt(n) > Z > (106-108)/σ/sqrt(n)  
Then use di normal( value of(110-108)/σ/sqrt(n)) - normal(value of (106-108)/σ/sqrt(n))

> z= (x⁻ +- μ) / ( σ/SQRT(n) )  
> (110-108) / ( σ/SQRT(n) ) > z  
> (106-108) / ( σ/SQRT(n) ) < z

	di normal( (110-108) / 1.4433757 ) - normal( (106-108) / 1.4433757 )
> => **0.83414333**



4. Suppose instead we repeatedly took random samples of size 25. What proportion of the samples would we expect to have a sample mean xˉ that lies between 106 and 110 g/L?
Hints: Q4 same as Q3 only the value of n is changed.

> n= 25  
> sd= 12.5/sqrt(25)= 2.5  
> z= (x⁻ +- μ) / ( σ/SQRT(n) )

	di normal( (110-108) / 2.5 ) - normal( (106-108) / 2.5 )
> => **0.5762892**


5. Again, suppose we repeatedly took samples of size 75. What proportion of the samples would we expect to have a mean less than xˉ=103?
Hints: Xbar < 103 = Z < (103-108)/σ/sqrt(n), then di normal(value of (103-108)/σ/sqrt(n))
Hint2: In (103-108)/σ/sqrt(n), σ = 12.5, n= 75 then di normal()

> n= 75  
> xˉ <= 103  
> sd= 1.4433757  
> z= (103-108)/1.4433757= -3.4641016

	di normal( -3.4641016 )
> => **0.000266**


6. If we repeatedly took samples of size 75, we would expect that, in 20% of the samples, xˉ would be greater than ____?
(Hint: Use invnormal(0.8) to find the P(Z>z∗)=1−0.8=0.2, where Z∼N(0,1).
Hint2: di invnormal(0.8)= (x bar - μ)/σ/sqrt(n) and then find the value of X bar

	di invnormal(0.8)
> => **0.84162123**

> 0.84162123= (xˉ-108)/1.4433757  
> => xˉ= 0.84162123*1.4433757+108= **109.21478**

7. After taking a sample of size 75, we found that the sample mean was xˉ=103. Construct a 95% confidence interval for μ.
Hints: See the Confidence Interval section in https://www.edx.org/static/content-harvard-id270x/handouts/HandoutWeek5Review.2a666d8d60ca.pdf

> xˉ=103  
> [ x⁻-1.96*σ/SQRT(n), x⁻+1.96*σ/SQRT(n), ]

	di 103 - 1.96*1.4433757  
	di 103 + 1.96*1.4433757

> Lower Bound:  
> => **100.17098**

> Upper Bound:  
> => **105.82902**


8. Based on the above interval, we can say that the probability that xˉ lies in the interval is 0.95.

> True  
> => False 


9. Suppose we were also interested in the mean of the highly right skewed indicator of iron absorption, ferritin. Compared to the relatively symmetrically distributed indicator hemoglobin, do you think a larger or smaller sample size would be required to apply the central limit theorem?

> Smaller  
> => Larger 

