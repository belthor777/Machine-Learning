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



