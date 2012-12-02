# Categorical Data #

## One Sample Binomial Model  ##
> p = probability of success  
> n = number of trials
> mean = n*p  
> sd = sqrt( mean*(1-p) )
> X = number of successess

> We have to calculate the left probability!

### Estimator of p ###
> n trials, x successes= SUM i=1 to n d_i
> where d_i = 1 if i_th trial is a success,  
>           = 0 if i_th trial is a failure  
>  
> ^p= x/n= 1/n * SUM i=1 to n d_i


## Inference for p ##
Is approximately normal with mean p and standard deviation sqrt(p*(1-p)/n)

### Standardization ###
> Z = (^p - p) / sqrt(p*(1-p)/n)


### Wald Estimator ###
> Z = (^p - p) / sqrt(^p*(1-^p)/n)

### Exact ###
We will do this later

### Confidence Intervals (Wilson Methode) ###
> So approximate CI, solve for ps that satisfy

	summ death angina hospmi stroke cvd hyperten diabetes1

## Hypothesis Testing for P  ##

> H_0: p=0.082  
> n= 52  
> p-value= 0.384
>  
> Z= (^p - p) / sqrt(p*(1-p)/n)  
>  = 0.115 - 0.082 / sqrt(0.082*(1-0.082)/52)  
  
> 6= 6 successes  
  
	prtesti 52 6 0.082 , count

### Exact test ###

	bintesti 52 6 0.082


##  Sample Size Estimation  ##
> Suppose we wish to test the hypothesis H_0: p <= 0.082 at the alpha=0.01 level, and we want power of 0.95 at p=0.2. How big a sample do we need?

> For alpha=0.01 the z=2.32. So since  
> Z= (^p - p) / sqrt(p*(1-p)/n)  
> ^p= ? and n=?  
  
> a Z of 2.32 corresonds to a ^p of:  
> ^p = 0.082 + 2.32*sqrt(0.082*0.918/n)

	sampsi 0.082, alpha(0.01) power(0.95) onesamp oneside





