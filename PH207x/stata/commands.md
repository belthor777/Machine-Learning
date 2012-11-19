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
>	di 25.84616 + 1.96*4.101821
> [17.806591, 33.885729 ]

##### Q2. Suppose we now draw repeated samples of size 100 from the Framingham cohort. What is a 95% predictive interval for the sample mean? #####
	   
>	di 25.84616 - 1.96*4.101821/sqrt(100)
>	di 25.84616 + 1.96*4.101821/sqrt(100)
> [ 25.042203, 26.650117 ]

##### Q3. Take a sample of size 100. Construct a 95% configence interval for μ. #####
	   
>	sample 100, count
>	sum bmi1

>	di 25.84616 + 1.96*4.101821/sqrt(100)
>	di 25.84616 - 1.96*4.101821/sqrt(100)
> [ 25.042203, 26.650117 ]

## Confidence intervals and t-distribution
> X~Normal(μ, σ²)  
> CI= Confidence Interval

### σ is known ###
> 95% x⁻ +- Z_(1-2/2) * σ/sqrt(n)
> Z= 0.975

### σ is unknown ###
> 95% CI x⁻ +- t_n-1,0.975 * σ/sqrt(n)

> Note that if "normal(z)=p", then "invnormal(p)=z"

	set seed 2  
	sample 20, count  
	sum bmi1


>     Variable |       Obs   |     Mean  |  Std. Dev.  |     Min  |      Max
> -------------|-------------|-----------|-------------|----------|---------
>         bmi1 |        20   |  25.0295  |  3.184407   |   20.19  |    32.29

> *95%:*  
>	di 25.0295 - 1.96*3.184407  
>	di 25.0295 + 1.96*3.184407  
> => **[ 18.788062, 31.270938 ]**

> *Z= 0.975*  
>	di 25.0295 - invnormal(0.975)*3.184407  
>	di 25.0295 + invnormal(0.975)*3.184407  
> => **[ 18.788177, 31.270823 ]**

> *99%:*  
>	di 25.0295 - invnormal(0.995)*3.184407  
>	di 25.0295 + invnormal(0.995)*3.184407  
> => **[ 16.827011, 33.231989 ]**


### 95% confidence interval for μ where σ is known###
> σ is known and it is σ= 4.1 for the framingham cohort
> invnormal(0.975) ~ 1.96


	set seed 2
	sample 20, count
	sum bmi1

>     Variable |       Obs   |     Mean  |  Std. Dev.  |     Min  |      Max
> -------------|-------------|-----------|-------------|----------|---------
>         bmi1 |        20   |  25.0295  |  3.184407   |   20.19  |    32.29


>	di 25.029-1.96*4.1/sqrt(20)  
>	di 25.029+1.96*4.1/sqrt(20)  
> => **[23.232096, 26.825904]**

> *97.5%:*
>	di 25.029-invnormal(0.975)*4.1/sqrt(20)  
>	di 25.029+invnormal(0.975)*4.1/sqrt(20)  
> => **[23.232129, 26.825871]**


### 95% for μ with invttail where σ is unknown ###
> σ is unknown  
> x⁻ +- t_n-1 * σ/sqrt(n)  
> t-tail= 0.025  
> n-1= 19  
>  
>	di 25.029-invttail(19,0.025)*3.184407/sqrt(20)  
>	di 25.029+invttail(19,0.025)*3.184407/sqrt(20)  
> => **[ 23.538652, 26.519348 ]**

#### Easy Stata command to calculate invttail where σ is unknown ####

	set seed 2
	sample 20, count
	sum bmi1

>     Variable |       Obs   |     Mean  |  Std. Dev.  |     Min  |      Max
> -------------|-------------|-----------|-------------|----------|---------
>         bmi1 |        20   |  25.0295  |  3.184407   |   20.19  |    32.29


	cii 20 25.0295 3.184407


>    Variable |        Obs  |      Mean |   Std. Err.  |     min [95% Conf. Interval] | max [95% Conf. Interval] 
> ------------|-------------|-----------|--------------|------------------------------|--------------------------
>             |         20  |   25.0295 |   .7120551   |     23.53915                 |  26.51985                


#### Easy Stata command to calculate confidence intervals ####

	ci bmi1

>    Variable |        Obs  |      Mean |   Std. Err.  |     min [95% Conf. Interval] | max [95% Conf. Interval] 
> ------------|-------------|-----------|--------------|------------------------------|--------------------------
>        bmi1 |         20  |   25.0295 |   .712055    |    23.53915                  |  26.51985                

## P-values and examples  ##
> μ_0= 237 mg/ml  
> σ= 47.7 mg/100ml  
> n= 49 non-hypertensives  
> z= (x⁻ - μ_0) / (σ/SQRT(n))

	set seed 725764662
	drop if hyperten==1
	sample 49, count
	mean totchol1

> We could use the standard error (Std. Err.), if we are using t instead of z. Now we are using z!

>              |       Mean   | Std. Err.  | min [95% Conf. Interval]  | max [95% Conf. Interval]
> -------------|------------- | ---------- | ------------------------- | -------------------------
>     totchol1 |   221.8776   | 4.614348   |    212.5998               |   231.1553
> Mean estimation                     Number of obs    =      49

	di (221.8776-237) / (44.7/7)
> => -2.3681611

## Hypothesis Testing ##

### Example: Inference about heart rates in healthy young adults ###
> In adults over 15 years of age, a resting heart rate around 80bpm is usually considered average. Using a subset of the Framingham cohort, we are going to attempt to make inference about heart rate among "healthy young" adults."

> Specifically, we restrict our analysis to adults with the following characteristics at baseline: non-smoker, younger than 40, BMI less than 25 and systolic blood pressure less than 120. There are 61 participants who meet our criteria.

> **We hypothesize that heart rate at follow up would be lower than 80bpm, the resting heart rate for adults with average health.**

> We are making the somewhat strong assumption that these Framingham participants are generalizable to the broader population of healthy young adults (this assumotion is necessary if we want to make inference about heart rate in healty young adults.)

1. Choose a test (e.g. one-sample t-test)

> Hypotheses     | 
> -------------- | 
> H_0: μ = 80    | 
> H_A: μ != 80   | 

* One sample t-test
* Normally distributed

> Stata commands:

	use healthyyoungadults.dta
	histogram heartrte2
	histogram heartrte2 if heartrte2 < 200


2. State null or alternative hypothesis
3. Do the tests

> Stata commands for "One-sample t test":

	db ttest
	ttest heartrte2 == 80

> Variable |     Obs  |      Mean  |  Std. Err. |  Std. Dev. | min [95% Conf. Interval] | max [95% Conf. Interval] 
> -------- | -------- | ---------- | ---------- | ---------- | ------------------------ | -------------------------
> heartr~2 |      61  |  76.55738  |  2.800032  |  21.86895  |  70.95648                |  82.15827


> mean = mean(heartrte2)                                        t =  -1.2295  
> Ho: mean = 80                                    degrees of freedom =       60  
> Ha: mean < 80               Ha: mean != 80                 Ha: mean > 80  
> Pr(T < t) = 0.1118         Pr(|T| > |t|) = 0.2237          Pr(T > t) = 0.8882



4. Present your results - test statistic, p-valu...
5. Conclusion reject the null or fail to reject the null
6. Make a conclusion about your data









