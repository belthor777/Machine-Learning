# Inference for proportions #
> According to Fergusson et al. (2012), acutely ill patients, including neonatal infants, often receive red blood cell transfusions. However, the consequences of the use of red blood cells that have been stored for prolonged periods on health outcomes in premature infants are not well understood. In a double-blinded, randomized controlled trial, the authors looked at health outcomes in neonatal infants who underwent red blood cell transfusions, comparing the standard protocol (transfusions of blood stored for prolonged periods) with fresh blood transfusions (transfusions of blood store for less than seven days).  
>  
> The authors examined five outcomes listed below, as well as a composite outcome, defined as at least one of the five outcomes. In this question, we focus primarily on the composite outcome. The results of the study are shown in the following table: 

Outcome                     | Standard Protocol | Fresh Blood
--------------------------- | ----------------- | ------------
Necrotizing enterocolitis   | 15                | 15
Intraventricular hemorrhae  | 11                | 18
Retinopathy of prematurity  | 26                | 23
Bronchopulmonary dysplasia  | 63                | 60
Death                       | 31                | 30
Composite Outcome           | 100               | 99
Total Sample Size           | 189               | 188

> A dataset hw7.dta is also available on this webpage, which contains individual-level data for the composite outcome and for the group assignment, if you would rather not use the "immediate" commands in Stata. 


#### 1. Construct a 95% confidence interval for the proportion of infants experiencing the composite outcome in the fresh red blood cell group, using the following methods: #### 
> **Hint1:** For lower CI exact and wilson i calculate using the dropdown menu confidence intervals, for upper CI i use the comand cii and i got it right, but i'm really sure that this can't be possible- please explain  
> **Hint2** A lot are having problems with the confidence intervals. When you get one right and the other wrong, it is probably because the values you gave Stata are wrong. There is an error allowance of 2% built in to the answers. So your "correct" answer was really wrong, but within 2% of being right.  
Using cii you should have been correct, if you gave the right sample size and cell size. Looking at help cii:  cii #obs #succ [, ciib_options]  
So you want the number of observations, then the number of "successes". In this case success is the number that fall into the desire category of fresh composite.  
You just enter the name of the required confidence interval as an option - don't include the brackets  
> **Hint3:** The question asks you to construct a 95% confidence interval for the proportion of infants experiencing the composite outcome in the group that received fresh red blood cell group. For this reason the variable should be the outcome. You are right, you need put the fresh variable in the by/if/in to be able to pick only the infants who received fresh blood. 

> Exact binomial: **[0.4526364,0.5997032]**  

> I used:

	ci outcome if fresh==1, binomial


> Wilson normal approximation: **[0.455408,0.5967184]**

> I used:

	ci outcome if fresh==1, binomial wilson

#### 2. Is the normal approximation to the binomial appropriate in this setting? ####
> Yes  
> No

#### 3. Suppose you wanted to calculate a 95% confidence interval for infants experiencing intraventricular hemorrhage after receiving a fresh blood transfusion as well. Examine the table above. Is the Wilson confidence interval still appropriate? #### 
> **Hint1:** One of the answers is above 5 while the other is less than 5. Should we have both of them above 5 to say that Wilson confidence interval still appropriate? I got this answer wrong and really did upset me. *Both needs to be > 5:*
> **Hint2:** Wilson can be used if np(the mean)>5, and n(1-p)>5. You don't need Stata here. To calculate p you use our formula: P = X(exposed)/N(total sample size) From the table n is known and x is known.  

	csi #a #b #c #d [, csi_options]

> Yes  
> No


#### 4. Estimate and construct a large-sample 95% confidence interval for the risk difference for experiencing the composite outcome for those with fresh blood versus the standard protocol blood. **Calculate the risk difference as the estimated proportion in the fresh blood group minus estimated proportion in the standard blood group.** #### 

	cs outcome fresh


> Estimate of risk difference: **-0.0025048**

> 95% Confidence Interval: **[-0.1032915,0.0982819]**


#### 5. Use a two-sample test of proportions to test whether there is a difference in the proportion of infants experiencing the composite outcome between fresh blood group and the standard protocol group at the alpha=0.05 level of significance. ####

> Proportion (percent) 

	tabulate fresh

      fresh |      Freq.   |   Percent |       Cum.
----------- | ------------ | --------- | -----------
          0 |        189   |     50.13 |      50.13
          1 |        188   |     49.87 |     100.00
      Total |        377   |    100.00 |


	prtesti (fresh#proportion of fresh # Standart # proporiton of Standard) 
	prtesti 188 0.4987 189 0.5013


###### What is the value of the test statistic? ######
> z =  -0.0505

##### What is the null distribution of the test statistic? ######
> Standard normal distribution 
> Binomial distribution 


##### What is the p-value? ######
> p-value is Pr(|Z| < |z|) = **0.9718**

	prtesti 99 .52659574 100 .52910053

##### What is the conclusion? ######
> => **No evidence that the risk difference is not equal to 0**  
> Evidence that the risk difference is greater than 0  
> Evidence that the risk difference is less than 0 

