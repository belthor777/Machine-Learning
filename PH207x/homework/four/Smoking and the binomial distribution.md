# Smoking and the binomial distribution
According to data from the CDC in 2010, 19.3% of adults age eighteen and older smoke cigarettes. In the year 2008, the incidence rate of lung cancer was 65.1 cases per 100,000 people per year.

Suppose you are conducting a lung cancer study in the United States, and you obtain a random sample of 2,000 adults (over 18 years of age) who do not have lung cancer. You plan to follow this study cohort over a period of 5 years and observe incident cases of lung cancer.

## Smoking and the binomial distribution. 
Smoking status is an important predictor of lung cancer incidence. Therefore, as the study designer, it is important to think about baseline smoking rates in your study cohort. We first model the number of smokers in the study cohort using the binomial distribution, and assume that this cohort is representative sample from the US population. Use the binomial distribution to answer the parts below. 

 * 2010: 19.3% of >18 years smoke cigarettes
 * 2008: 65.1/100,000 people= 0.0000655
 * p= prevalence= 0.193
 * n= sample size= 2000
 * observation: 5 years

##### Q1. How many smokers would you expect to see in the study cohort, on average? #####
	   
>	E(x)= n*p= ?  

	di 0.193*2000  

>	=> E(x)= 386

##### Q2. What is the standard deviation of the number of smokers in the study cohort? #####
	   
>	sd(x)= sqrt(number of people*prevalence*(1-prevalance))  
>	sd(x)= SQRT( n*p*(1-p) )= SQRT( 2000*0.193*(1-0.193) )  

>	=> sd(x)= 17.6494192539

##### Q3. What is the probability that you observe exactly 386 smokers? #####
	   
>	P(X=386)= binomialp(2000,386,0.193)  

	di binomialp(2000,386,0.193)

>	=> P(X=386)= 0.0225986

##### Q4. What is the probability that greater than or equal to 25% of the study population are smokers? Please round your answer to 4 decimal places. #####
	   
>	P( X >= 500 )= binomialtail(2000,500,0.193)
di binomialtail(2000,500,0.193)
=> 0.0000000002403

##### Q5. What is the probability that less than or equal to 20% of the study population are smokers? #####
	   
>	P( X <= 400 )= binomial(2000,400,0.193)
di binomial(2000,400,0.193)
=> 0.79487415

