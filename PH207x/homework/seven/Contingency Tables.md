# Contingency Tables #
> Continue using the Fergusson et al. (2012) clinical trial data to complete the following questions. Again, use either the dataset from the previous question, hw7.dta, or the study results in the table below.

Outcome                     | Standard Protocol | Fresh Blood
--------------------------- | ----------------- | ------------
Necrotizing enterocolitis   | 15                | 15
Intraventricular hemorrhae  | 11                | 18
Retinopathy of prematurity  | 26                | 23
Bronchopulmonary dysplasia  | 63                | 60
Death                       | 31                | 30
Composite Outcome           | 100               | 99
Total Sample Size           | 189               | 188

#### 1. Estimate the odds ratio and a 95% confidence interval for experiencing the composite outcome for those in the fresh blood group versus standard protocol blood group. #### 
> **Hint1:** exposed = fresh blood unexposed = standard protocol  
> **Hint2:** composite outcome not composite outcome (all the other entries)

> OR Estimate: **0.99**

> 95% Confidence Interval: **[0.6607011,1.483424 ]**


> I used: 

	cs fresh outcome, or woolf



##### Is there evidence of an association between blood group and the composite outcome (at the 0.05 level of significance). ##### 
> Yes  
> => **No** 

	tabulate outcome fresh, expected chi2


#### 2. Construct a 2x2 table for the composite outcome versus blood group. Are the expected cell counts large enough to conduct a Pearson Chi-square test? #### 

	tabplot outcome fresh

#### 3. Using the Pearson chi-square test, determine if there is evidence of an association between blood group and the composite outcome at the   level of significance. #### 
> (To answer this question, either use the hw7.dta dataset OR explore using the csi command by typing "db csi.")  

	tabulate outcome fresh, expected
	csi 100 99 98 98, or woolf

##### What is the value of the test statistic? Round your answer to two decimal places. ######
> chi2(1) = **0.00**

##### What is the null distribution of the test statistic? ##### 
> => **Chi-square distribution with 1 degree of freedom**
> Binomial distribution

##### What is the p-value? ##### 
> Pr>chi2 = **0.9602**

##### What is the conclusion? #####
> => **No evidence of an association between fresh and standard groups**
> Evidence of an association between fresh and standard groups 




