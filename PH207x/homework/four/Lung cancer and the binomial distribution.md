# Lung cancer and the binomial distribution

Recall: According to data from the CDC in 2010, 19.3% of adults age eighteen and older smoke cigarettes. In the year 2008, the incidence rate of lung cancer was 65.1 cases per 100,000 people per year.

Suppose you are conducting a lung cancer study in the United States, and you obtain a random sample of 2,000 adults (over 18 years of age) who do not have lung cancer. You plan to follow this study cohort over a period of 5 years and observe incident cases of lung cancer.

Lung cancer and the binomial distribution. You also need to carefully consider how many cases of lung cancer you expect to observe in your study over time. We first model the number of lung cancer cases observed in the first year using the binomial distribution.

- 2010: 19.3% of >18 years smoke cigarettes
- p= 0.193
- n= 2000 have no lung cancer
- observation 5 years
- 2008: incidence rate of lung cancer was 65.1 cases per 100,000 people per year -> = 0.0000655

**Q1. What proportion of the study population would you expect, on average, to be diagnosed with lung cancer in the first year?**
	   
>	=> Prevalence Proportion is the total number of persons with lung cancer  
>
>	p= prevalence = incidence * duration= 65.1/100000 * 1= 0.000651  
>	n= sample size= 2000  
>	sd(X)= standard deviation= SQRT( n*p*(1-p) )= SQRT( 2000*65.1/100000*(1-65.1/100000) )= 1.1406806731  
>
>	proportion= prevalence / duration= 65.1/100000 / 1= **0.000651**

**Q2. How many cases of lung cancer would we expect to observe in the first year?**
*Hint1: The expected value E(x) of a binomial distribution can be with decimals, but the actual number of alive people can only be a whole number (0, 1, 2, 3...).*   
	   
>	p= 65.1/100000  
>	n= 2000  
>	E(x)= n*p= 65.1/100000*2000  

	di 65.1/100000*2000  

>	=> **1.302**

**Q3. Why would you expect the mean and variance to be similar in this example?**
- **the event is rare**
- the mean is close to 1 
- we are dealing with incidence rates 
- both (a) and (b)

**Q4. What is the probability that you observe more than 1 lung cancer case in the first year?**

>	P(X>1)= ?

>	k=1  
>	n=2000  
>	p=0.00065  

>	P(X>1)= P(X>=1)-P(X=1)
>	P(X>1)= binomialtail(2000,1,0.00065)-binomialp(2000,1,0.00065)

	di binomialtail(2000,1,0.00065)-binomialp(2000,1,0.00065)

>	=> **0.37321143**


**Q5. What is the probability that you observe no lung cancer cases in the first year?**

>	P(X=0)= ?

>	k=0
>	n=2000
>	p=0.00065

>	P(X=0)= binomialp(2000,0,0.00065)

	di binomialp(2000,0,0.00065)

>	=> **0.27241662**

* **Table in Stata**

	clear all
	set obs 5
	gen x=_n-1
	gen p = binomialp(2000,x,0.00065)
	list x p`


	   +--------------+  
	   | x          p |  
	   |--------------|  
	1. | 0   .2724166 |  
	2. | 1    .354372 |  
	3. | 2   .2303763 |  
	4. | 3   .0997948 |  
	5. | 4   .0324057 |  
	   +--------------+



