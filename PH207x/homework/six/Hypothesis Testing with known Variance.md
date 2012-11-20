#Hypothesis Testing with known Variance#
Now, let's switch gears and assume that we didn't know the true population mean μ, and we only observed a sample of 25 school children in Delhi. Let's use the sample mean from this set of children to make inference about the true population mean μ.

For this question, assume that σ=12.5 is known and that the sample size of 25 is large enough to use the Central Limit Theorem. So, for this question, we will base our inferences off of the normal distribution, not the t-distribution).

In this scenario, we can conduct a one-sample Z-test for inference about μ in a population with known variance σ2. To test H0:μ=μ0, we can use the test statistic: Z^∗= (xˉ−μ_0) / (σ/sqrt(n) )

Under the null hypothesis, Z∗∼N(0,1). So, we can use the standard normal distribution to calculate a p-value for this hypothesis test:

* For the one-sided test with alternative hypothesis Ha:μ>μ0, we can calculate a p-value using the formula p=P(Z>Z∗).
* For the one-sided test with alternative hypothesis Ha:μ≤μ0, we can calculate a p-value using the formula p=P(Z≤Z∗).
* For the two-sided test with alternative hypothesis Ha:μ≠μ0, we can calculate a p-value using the formula p=2∗P(Z≤−|Z∗|).

Note: there is no command for directly conducting this one-sample Z-test in Stata. However, you can use the normal function in Stata to calculate the p-values. 

> μ= population mean= ?  
> n= sample size= 25  
> σ= 12.5
> p-value= ?


> We can use the Central Limit Theorem  
> We will use the *normal distribution*
> Use one-sample Z-test with known variance

1. In a sample of size 25, what is the value of the test statistic testing whether the mean hemoglobin level is equal to 108 g/L versus the alternative that it is not equal to 108 g/L, when xˉ=103. Use a one-sample Z-test. What is the p-value corresponding to this two-sided hypothesis test?

Hypotheses     | 
-------------- | 
H_0: μ = 108   | 
H_A: μ != 108  | 

> μ_0= 108 mg/ml  
> σ= 12.5
> n= 25
> xˉ= mean hemoglobin levels= 103

> z*= (x⁻ - μ_0) / (σ/SQRT(n))= (103 - 108) / (12.5/sqrt(25))= -2

> => **-2 is less than 1.96**  
> => So we reject the null hypothesis

Test statistic 
> => **-2**

p-value 
> 2*normal( -2 )
> => **0.04550026**
> => 

2. In a sample of size 25, what is the value of the test statistic for testing whether the mean hemoglobin level in the population is equal to 108 g/L versus the alternative that it **is less** than 108 g/L, when xˉ=103. What is the p-value corresponding to this one-sided test? 

> n= 25
> μ_0= 108 mg/ml  

Hypotheses     | 
-------------- | 
H_0: μ = 108   | 
H_A: μ < 108   | 

> z*= (x⁻ - μ_0) / (σ/SQRT(n))= (103 - 108) / (12.5/sqrt(25))= -2

> => **-2 is less than 1.96**  
> => So we reject the null hypothesis

Test statistic 
> => **-2**

p-value 
> normal( -2 )
> => **0.02275013**


3. In a sample of size 25, what is the value of the test statistic for testing whether the mean hemoglobin level in the population is equal to 108 g/L versus the alternative that it **is greater** than 108 g/L, when xˉ=103. What is the p-value corresponding to this one-sided test? 

> n= 25
> μ_0= 108 mg/ml  

Hypotheses     | 
-------------- | 
H_0: μ = 108   | 
H_A: μ > 108   | 

> z*= (x⁻ - μ_0) / (σ/SQRT(n))= (103 - 108) / (12.5/sqrt(25))= -2

Test statistic 
> => **-2**

p-value p=P(Z>Z*)
> normal( 2 )
> => **0.97724987**

