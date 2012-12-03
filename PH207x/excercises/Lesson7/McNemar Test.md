# McNemar Test #
> Paired Dichotomies  
> MI= Myocardial infarction  
> e.g. Pairs matched on age & sex:

Diabetes | M.I. Yes | M.I. No | Total
-------- | -------- | ------- | ------
Yes      | 46       | 25      | 71
No       | 98       | 119     | 217
Total    | 144      | 144     | 288

> So we have 144 pairs and we want to use McNemar's Test:

                   | No M.I. - Diabetes | No M.I. - No Diabetes | Total
------------------ | ------------------ | --------------------- | ------
M.I. - Diabetes    | 9                  | 37                    | 46
M.I. - No Diabetes | 16                 | 82                    | 98
Total              | 25                 | 119                   | 144

## Chi-squared ##
> Discordant entries: 37 & 16  
> x²= SUM of all cells [ ( |obs-exp|**-1** )² / exp ]  
> **-1**: Stata ignores the correction factor, 1
>  
> x²= ( |37-16|-1 )² / (37+16)  
>   = 7.55  
>  
> x²_(1,0.010)=6.63  
> x²_(1,0.001)=10.83  
> => **0.001<p<0.010**  
>  
> p < 0.05

# Tutorial: Inference for Paired Data using McNemar’s Test #
## Part 1 ##
> Consider the following study from Dekkers et al. (2011) that compared two different screening tests for determining adrenal insufficiency. Adrenal insufficiency is a condition in which the adrenal glands do not produce adequate amounts of certain hormones. The screening test involves measuring a patient’s cortisol response after administration of an intravenous bolus of adrenocorticotropic hormone (ACTH).  
>  
> Currently, two doses of ACTH are used for diagnostic purposes in patients with suspected adrenal insufficiency: 1 μg and 250 μg (Dekkers et al. 2011). There is an ongoing debate about which dose should be used for the initial assessment of adrenal function (Dekkers et al. 2011).  
>  
> The goal of this study was to compare the cortisol response of the 1 μg and 250 μg ACTH test among patients with suspected adrenal insufficiency. Patients with cortisol concentrations of ≥550 nmol/l after ACTH stimulation (considered normal cortisol response) were classified as not having adrenal insufficiency. This was a retrospective cohort study whereby patients who received both the 1 μg and 250 μg ACTH test between January 2004 and December 2007 were included for analysis. The data can be found in the AI.dta dataset.  
>  
> Source: Dekkers OM, Timmermans JM, Smit JW, Romijn JA, Pereira AM. Comparison of the cortisol responses to testing with two doses of ACTH in patients with suspected adrenal insufficiency.Eur J Endocrinol 2011 Jan;164(1):83-7  

              | 250 μg Abnormal | 250 μg Abnormal 
------------- | --------------- | --------------- 
1 μg Abnormal |                 |                 
1 μg Normal   |                 |                 


####1. Since this is paired data, we decide to use McNemar’s test. State the null and alternative hypothesis for McNemar’s test.####
> **Null:** The proportion of patients classified as having adrenal insufficiency using the 1 μg test is the same as the proportion of patients classified as having adrenal insufficiency using the 250 μg test.  
> **Alternative:** Those proportions are not equal.  
>  
> Is this the same as testing that the proportion of patients classified as not having adrenal insufficiency using the 1 μg test is the same as the proportion of patients classified as not having adrenal insufficiency using the 250 μg test?

	use "AI.dta", replace
	tabulate one two
	mcc one two

> This test is based on the binomial distribution  

####Conclusion####
> Since our p-value is greater than 0.05 we fail to reject the null hypothesis. Thus, we have no evidence that the proportion of patients classified as having adrenal insufficiency using the 1 μg test is different from the proportion of patients classified as having adrenal insufficiency using the 250 μg test.


## Part II ##
> Rather than analyzing the random sample of 500, we  match those below poverty to someone above poverty in the sample of 500.  
> **mcc** - McNemar's test in Stata

	use "chis_matched.dta", replace

> doctor_0: above the line who goes to the doctor  
> doctor_1: below the line who goes to the doctor  
>  
> H_0: no assoc.  
> H_1: there is a association  
>  
> Dataset:  
> => poverty= 1  
> => Age gender location

	mcc doctor_0 doctor_1

> The Unexposed is interessting!  
> x² H_0~ x²_1  
> We would use the Exact Value of McNemar, which depends on the small p-value  
>  
> Gain power by matching!  


#  Summarizing the Results #
> In this example, we have assumed that we have obtained a random sample of 500 California residents. (With observational survey data, nonresponse is always an issue, so we don’t know how random the sample actually is).  
>  
#### From the Pearson Chi-Square test, can we say that poverty causes individuals to go to the doctor less frequently over the past 12 months? (Please discuss why or why not on the discussion boards). ####
> Yes  
> => **No**

#### From the matched analysis, can we say that poverty causes individuals to go to the doctor less frequently over the past 12 months? (Please discuss why or why not on the discussion boards). ####
> Yes  
> => **No**

#### Could we get a better estimate of the effect of poverty on visiting the doctor in the past 12 months if we brought in more covariates/information about the individuals in the survey? (Please discuss why or why not on the discussion boards).#### 
> Not likely   
> => **Likely**

# Some guidance #
The moral of the story is that association is not causation in observational studies, because observational studies lack treament randomization (you can't randomize people to poverty). You can bring in more individual covariate information to improve your analysis, which we will learn to do via logistic regression. 

