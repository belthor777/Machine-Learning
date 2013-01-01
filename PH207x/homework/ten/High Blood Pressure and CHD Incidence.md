# High Blood Pressure and CHD Incidence #
Use Stata and the NHLBI data set to create the two categories of high blood pressure (highbp1) 

```stata
	generate highbp1=.
	replace highbp1=1 if (sysbp1>=140 | diabp1 >= 90)
	replace highbp1=0 if (sysbp1<140 & diabp1<90)
```

**(Note: There are no missing data on sysbp1 and diabp1. If data were missing on both sysbp1 and diabp1 then it should also be missing for highbp1. If data were missing on diabp1 only and sysbp1 >= 140 then highbp1 =1, otherwise highbp1 should be missing. Similarly, if data were missing on sysbp1 only and diabp1 >= 90 then highbp1 =1, otherwise highbp1 should be missing.)**

##### 1. What is the incidence rate ratio of stroke comparing those with high blood pressure to those without high blood pressure? Hint: The variable for stroke in the dataset is “stroke” and the number of years a person was followed for stroke is recorded in the “timestrk” variable. #####
> **Hint1:** Just a hint (I had this problem) - make sure you put data for the right sex in the right field (somehow I was putting results for males into Q3 and females into Q2 :))

```stata
	ir stroke highbp1 timestrk ir stroke highbp1 timestrk, by(sex1)
```

##### 2. What is the incidence rate ratio (rounded to two decimal points) for the association between high blood pressure (highbp1) and the rate of stroke among men? Hint: Use the variable (sex1). #####

##### 3. What is the incidence rate ratio (rounded to two decimal points) for the association between high blood pressure (highbp1) and the rate of stroke among women? #####

##### 4. Conduct a test of homogeneity to evaluate whether the association between high blood pressure (highbp1) and the rate of stroke is different by sex. Based on this test, is there evidence that the difference between the sex-specific incidence rate ratios are more than just random sampling variability? #####
* Yes
* No

##### 5. Based on these results, what are the options for properly reporting the association between high blood pressure (highbp1) and the rate of stroke? #####
* A. Sex-specific incidence rate ratios 
* B. Pooled (Mantel-Haenszel) incidence rate ratio 
* C. Standardized incidence rate ratio 
* D. Choices A or B 
* E. Choices A or C 
