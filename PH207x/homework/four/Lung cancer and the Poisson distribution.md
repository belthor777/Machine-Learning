# Lung cancer and the Poisson distribution
Recall: According to data from the CDC in 2010, 19.3% of adults age eighteen and older smoke cigarettes. In the year 2008, the incidence rate of lung cancer was 65.1 cases per 100,000 people per year.

Suppose you are conducting a lung cancer study in the United States, and you obtain a random sample of 2,000 adults (over 18 years of age) who do not have lung cancer. You plan to follow this study cohort over a period of 5 years and observe incident cases of lung cancer.

Lung cancer and the Poisson distribution. Because lung cancer is a rare disease, we can model cases of lung cancer using the Poisson distribution, with incidence rate 65.1 cases per 100,000 person-years.

1. Using the Poisson distribution, what is the probability that you observe more than 1 lung cancer case in the first year?   
Please see that it is more than 1 lung cancer. 1 is not included.   
> P(X>1)= ?  
> k=1  
> n=2000  
> p=0.00065   
> m= mean= n*P= 2000*0.000651= 1.302   
> P(X>1)= P(X>=1)-P(X=1)= poissontail(m,k) - poissonp(m,k)   

`di poissontail(1.302,1) - poissonp(1.302,1)`

=> 0.37388529


2. What is the expected number of lung cancer cases observed over the five year study period?
Hint1- It is 5 year study period. Same number of Cancer will be produced each year.
Hint2- In a year how many cancer cases will be observed among the 2000 randomly selected individuals?
incidence_rate= 0.000651
duration= 5
prevalence = incidence_rate * duration= 0.000651 * 5= 0.003255
E(x)= n*p= 0.003255*2000= 6.51


3. What is the variance of the number of lung cancer cases observed over the five year study period?
Hint1- In the formula for variance which is np(1-p) if p is too tiny tiny tiny what will (1-p)equal to and ultimately np(1-p)=???. it was already indicated that lamda = mean = np.
n=2000
p=0.00065
variance= np(1-p)= 2000*0.00325*(1-0.00325)= 6.478875


4. What is the probability that you observe more than 10 lung cancer cases over the five year period?
Hint1- It is more than 10. 10 is not included. 5 years period. In stata, di poisson(mean,X) gives result inclusive of X.
k=10
n=2000
p=0.00065
m= mean= n*P= 2000*0.000651= 1.302

P(X>10)= ?
P(X>10)= P(X>=10)-P(X=10)= poissontail(1.302,10)-poissonp(1.302,10)
`di poissontail(1.302,10)-poissonp(1.302,10)`
=> 1.392e-07

	clear all
	set obs 11
	gen k=10
	gen m=_n*2000*0.000651
	gen p = poissontail(m,k)-poissonp(m,k)
	list m p

=> 0.0673981


5. What is the probability that you observe less than 5 lung cancer cases over the five year period?

k=5

n=2000

p=0.00065

m= mean= n*P= 2000*0.000651= 1.302


P( X<5 )= P(X<=k)-P(X=k)= poisson(m,k) - poissonp(m,k)

	clear all
	set obs 11
	gen k=5
	gen m=_n*2000*65.1/100000
	gen p = poisson(m,k) - poissonp(m,k)
	list m p

=> 0.2225557
