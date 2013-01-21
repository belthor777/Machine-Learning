# Infant Cry Time #
In this series of questions, we examine data from a study of 158 infants who visited Northbay Healthcare in Solano County, California for a Vitamin K shot. Assume that the infants in the study are a representative random sample from all infants in Northbay Healthcare.  
  
Nurses administered a Vitamin K shot to each infant. Infants were randomized to two different protocols to study how to reduce pain experienced by the infants due to the shot. The infants were divided into two groups – the control group, where standard protocol for handling the infants was used; and an intervention group, where mothers held their infants prior to, during, and after administration of the shot. Pain was measured using the Neonatal Infant Pain Score (NIPS) (Lawrence et. al 1993). The variables in the dataset are described below:  

* id – unique identifier for each infant
* group – 1 if intervention group, 0 if control
* pain0 – NIPS score 0 seconds after shot
* pain30 – NIPS score 30 seconds after shot
* pain60 – NIPS score 60 seconds after shot
* pain120 – NIPS score 120 seconds after shot
* crytime – total time that the infant cried in seconds
  
These data were made available through SOCR . (www.socr.ucla.edu/)  
  
Source: Lawrence J, Alcock D, McGrath P, Kay J, MacMurray SB, Dulberg C. (1993) The development of a tool to assess neonatal pain, Neonatal Network, 12:59-66.


## Exploratory Analysis ##
Before jumping into analyzing the babies.dta dataset, first explore the dataset using summary statistics and graphical analyses. 

1. Make a boxplot of cry time by group. According to the boxplot, which group has more variability in cry time?  
* **control**
* intervention 

```stata
	graph box crytime, by(group)
```

2. Using the central limit theorem, construct a 95% confidence interval for the average total cry time for infants in the control group and infants in the intervention group. For this question only, assume that the standard deviation of cry time within each group is known and is equal to 22 seconds.  
  

n=sample size= 158  
  
```stata
	mean crytime, over(group)
```
> [ x⁻-1.96*σ/SQRT(n), x⁻+1.96*σ/SQRT(n), ]  
  
**Control**  
> Construct a 95% confidence interval for average total cry time for infants in the control group  
  
* Lower Bound: 34.351151  
* Upper Bound: 44.053909  
  
n=sample size= 79  
σ=standard deviation= 22s  
x⁻=39.20253  
```stata
	di 39.20253 - 1.96*22/sqrt(79)
	di 39.20253 + 1.96*22/sqrt(79)
	ci crytime if group==0
```
  
**Intervention**
> Construct a 95% confidence interval for infants in the intervention group  
  
* Lower Bound: 24.756211  
* Upper Bound: 34.458969  
  
```stata
	di 29.60759 - 1.96*22/sqrt(79)
	di 29.60759 + 1.96*22/sqrt(79)
```

## Two-sample Non-parametric Test ##
Now, we examine the relationship between cry time and group among infants at Northbay.  

1. Suppose we wish to perform a two-sample test, but we do not want to make any normality (or other strong parametric) assumptions. Conduct an appropriate non-parametric test to test whether the distribution of cry time is the same in both groups at the 0.05 level of significance.  
  
```stata
	ranksum crytime, by(group)
```
=> What is your p-value: **0.0080**  
  
**Your conclusion from the test?**  
* there is evidence that the *means* of the two groups are different (specifically, there is evidence that the mean is higher in the control group) 
* there is not evidence that the *means* of the two groups are different 
* none of the above 

2. Assuming randomization was successful and all participants complied with their assigned exposure, which of the following should we be concerned about: 
* Confounding by sex of the infant 
* Confounding by the amount of pain experienced by the infant 
* Effect modification by sex of the infant 
* Misclassification of the exposure status of the infant 


## Linear Regression ##
In the babies.dta full dataset, generate a covariate called painind defined as 1 if the infant experienced severe pain upon receiving the shot (pain0 = 7) and as 0 otherwise. In Stata, you can use the commands:  
  
```stata
	generate painind = 0
	replace painind = 1 if pain0 == 7
```
  
Fit a linear regression model with total cry time as the outcome; and with group and painind (the severe pain indicator) as covariates. The regression model is:  
  
> Y_i = β_0 + β_1*group_i + β_2*painind_i + ε_i  
> where ε_i ~ N(0,σ²).

1. **Using the notation from the model above, what are your estimates of the regression coefficients and residual standard deviation?**  
  
```stata
	regress crytime group painind
```
  
* β_0= **29.78**
* β_1= **-7.679168**
* β_2= **12.61215**
* σ= **21.766**

2. **Using the fitted regression model, estimate the average change in cry time for infants with severe pain versus those without severe pain, holding group constant. Provide a 95% confidence interval for this estimate.**  
  
```stata
	regress crytime group painind
```
  
* Estimate: **12.61215**  
* 95% Confidence interval Lower Bound: **5.235661**
* 95% Confidence interval Upper Bound: **19.98863**

3. **Again, use the notation above for the regression model. The correct interpretation for β_1 is:**
  
* Infants in the intervention group have β_1 times the risk of experiencing an increase in cry time compared to infants in the control group 
* Infants in the intervention group have β_1 times the risk of experiencing an increase in cry time compared to infants in the control group after controlling for pain experienced by the infant 
* Infants in the intervention group on average have β_1 change in cry time compared to the control group. 
* Infants in the intervention group on average have β_1 change in cry time compared to the control group, after controlling for severity of pain experienced by the infant upon receiving the shot.


4. **Using the regression model, estimate the average cry time in the following groups:**
  
* Control group infants with severe pain upon receiving the shot: **42.3955**
```stata
	regress crytime group if group==0 & painind==1
```
* Control group infants without severe pain upon receiving the shot: **29.7833**
```stata
	regress crytime group if group==0 & painind==0
```
* Intervention group infants with severe pain upon receiving the shot: **34.7163**
```stata
	regress crytime group if group==1 & painind==1
```
* Intervention group infants without severe pain upon receiving the shot: **22.1042**
```stata
	regress crytime group if group==1 & painind==0
```


5. **Without using the regression model, estimate the mean cry time in the following groups:**
  
* Control group infants with severe pain upon receiving the shot: **40.64407**
```stata
	regress crytime group if group==0 & painind==1
```
* Control group infants without severe pain upon receiving the shot: **34.95**
```stata
	regress crytime group if group==0 & painind==0
```
* Intervention group infants with severe pain upon receiving the shot: **36.91489**
```stata
	regress crytime group if group==1 & painind==1
```
* Intervention group infants without severe pain upon receiving the shot: **18.875**
```stata
	regress crytime group if group==1 & painind==0
```



