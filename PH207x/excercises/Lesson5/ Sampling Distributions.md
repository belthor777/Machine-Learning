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
        bmi1 |      4415  |  25.84616  |  4.101821   |   15.54   |    56.8


>	di  25.84616  - invnormal(0.95)*4.101821/sqrt(10)
>	di  25.84616  + invnormal(0.95)*4.101821/sqrt(10)
> => **[23.712604, 27.979716]**


#### Q3. For normally distributed random variables with known variance, the width of the 90% predictive interval for the sample mean is equal to the width of a 90% confidence interval for the population mean. ####
> => **True**
> False 

	ci bmi1, level(90)


>    Variable |        Obs  |      Mean |   Std. Err.  |     min [95% Conf. Interval] | max [95% Conf. Interval] 
> ------------|-------------|-----------|--------------|------------------------------|--------------------------
>       bmi1  |         20  |   25.0295 |    .712055   |     23.79826                 |   26.26074               


## Introduction to Hypothesis Testing ##

### Example ###
We know that total cholesterol levels in *our* Framingham population are distributed with mean μ = 237 mg/100ml and standard deviation σ = 44.7 mg/100ml.

#### Q1. We have a sample of 49 total cholesterol levels and their average is x⁻= 230 mg/100ml?

>	sd= σ/sqrt(n)= 44.7/7= 6.3857143  
> => So 230 is one standard error away from 237, and so the central limit theorem tells us that what we're talking about is quite possible.


### Is it reasonable to assume that this is a sample from our population? ###
> Use of 95% confidence interval to infer value of mean μ (μ=237)  
> [ x⁻ +- 1.96 σ/sqrt(n) -> x⁻ +- 1.96 47.7/sqrt(49) ->  **x⁻ +- 13.356**  
> has a 95% chance of including μ.


if x⁻   | 95% Conf. Interval  | Include μ?
------ | ------------------- | -----------------------------
230    | [216.6, 243.4]      | yes, depends on 243.4 > 237
223    | [209.6, 236.4]      | no, depends on 236.4 < 237
215    | [201.6, 228.4]      | no, depends on 228.4 < 237


### Formalism of Hypothesis Testing ###

* Propability of **Type I** error is **α**  
i.e. the probability of rejecting the null hypothesis when it is true

* Propability of **Type II** error is **β**  
i.e. the probability of **not** rejecting the null hypothesis when it is true

* **1-β** is the power of the test


### Testing for the population mean: one vs. two-sided tests  ###

1. Hypothesize a value (μ_0)
2. Take a random sample (n)
3. Is it *likely* that the sample came from a population with mean μ_0 (α=0.05)?  
Look at (x⁻-μ_0)/σ and decide. One sided or two: Decide the difference between the sample mean and the hypothesized mean. Is it too large or not!


Need to set up 2 hypotheses to cover all possibilities for μ. Choose one of three possibilities:

Hypotheses  | Formular
----------- | ------------
 Two-side   | H_0: μ = μ_0
 Two-side   | H_A: μ != μ_0

Hypotheses  | Formular
----------- | ------------
 One-sided  | H_0: μ >= μ_0
 One-sided  | H_A: μ < μ_0

Hypotheses  | Formular
----------- | ------------
 One-sided  | H_0: μ <= μ_0
 One-sided  | H_A: μ > μ_0

> H_0 - Null hypothesis  
> H_A - Alternative hypothesis


### P-values and examples ###
Look if the data are looking consonant. Look at z= (x⁻ - μ_0) / (σ/SQRT(n)) and reject H_0 if Z is too large, + or -.

Hypotheses     | 
-------------- | 
H_0: μ = μ_0   | 
H_A: μ != μ_0  | 

Example: Reject if Z is > 1.96 or < -1.96, then Pr(reject H_0 when true) = α = 0.05

#### Example ####

Hypotheses     | 
-------------- | 
H_0: μ = 237   | 
H_A: μ != 237  | 

> μ_0= 237 mg/ml  
> σ= 47.7 mg/100ml  
> n= 49 non-hypertensives  
> x⁻= 221.9 mg/100ml

> z= (x⁻ - μ_0) / (σ/SQRT(n))= (221.9 - 237) / (47.7/sqrt(49))= -2.2159329

> => **-2.2159329 is less than 1.96**  
> => So we reject the null hypothesis

#### P-value  ####
Some prefer to quote the p-value. The p-value answers the question: "What is the probability of getting as large, or larger, a discrepancy?" (μ- x⁻)

> z= (x⁻ - μ_0) / (σ/SQRT(n))= (221.9 - 237) / (44.7/sqrt(49))= -2.3646532= -2.37
> P_r( z>2.37 or z < -2.37 )= 2*P_r( z>2.37 )= 2*0.0222= 0.044

	di normal( -2.0106348 )
> => **0.02218202**  
> => 0.044 < 0.05, which means I would reject the null hypothesis

> *Hint:* normal(z) returns the cumulative standard normal distribution, so you can **NOT** take di 1-normal(2.37). if you do that, you will get the probability to get a result smaller than 2.37 standard deviations above μ.


## Example: Atherosclerosis and Physical Activity ##
> Oxidation of components of LDL cholesterol (the bad cholesterol) can result in atherosclerosis, or hardening of the arteries. Elosua et. al (2002) examine the impact of a 16 week physical activity program on LDL resistance to oxidation in 17 healthy young adults. After completing the program, the average maximum oxidation rate in the study participants xˉ was 8.2 μmol/min/g, and the sample standard deviation of the maximum oxidation rate was s=2.5 μmol/min/g. Assume that the oxidation rate is normally distributed.

### Continuous data ###

  population standard deviation      |  test type         | how to                                                                          
------------------------------------ | ------------------ | ---------------------------------------------------------------------------------
σ known, large n                     | One-sample Z-test  | Central Limit Theorem (CLT) - Normal
σ known, normally distributed data   | One-sample Z-test  | x⁻~N - Normal - Z-test based on the normal distribution - z= (x⁻-μ) / (σ/SQRT(n))
σ unknown, normally distributed data | One-sample t-test  | t-distribution - t= (x⁻-μ)/(s/SQRT(n)) - t~t_n-1





