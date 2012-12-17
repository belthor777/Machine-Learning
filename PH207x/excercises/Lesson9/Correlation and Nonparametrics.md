# Correlation and Nonparametrics #
> Links:

1. http://istics.net/stat/correlations/
2. http://data.worldbank.org
3. http://www.google.com/publicdata/directory/


## Pearson's Correlation Coefficient ##
## Inference on Rho  ##
> Sampling distribution:  
> If X & Y are normally distributed and rho=0, then  
>  
> t_n-2= r/sqrt( (1-r²) / (n-2) )  

### Example ###
> r=-0.829 for DPT example  
> t= r*sqrt( (n-2) / (1-r²) )  
> t= -0.829*sqrt( (20-2) / (1-(-0.829)^2) )= -6.29  
>  
> versus t with 18 degrees of fredom, so p<0.001.  
> So reject J_0: rho=0

```stata
	pwcorr diabp1 sysbp1 if _n<51 , sig
```

## Missconceptions ##
## Spearman's Rank Correlation Coefficient ##
> When you have any doubts about the distribution of your x's and your y's -whether they're normal or not- go with the Spearman's.  
> And now the other beauty of Spearman's is that this word linear doesn't appear here. This is truly a test for independence of these two characteristics.  
> Rank the Data:

i        | x   | y    | x_r  | y_r  | d      | d²
-------- | --- | ---- | ---- | ---- | ------ | -------
 1       | 1.3 | 14.3 | 2    | 2    | 0      | 0
 2       | 1.7 | 14.7 | 4    | 3    | 1      | 1
 3       | 0.8 | 18.0 | 1    | 4    | -3     | 9
 4       | 1.4 | 12.1 | 3    | 1    | 2      | 4

> x and y are Raw Data  
> x_r and y_r are Ranks  
> d is the difference between x_r and y_r by using:

	r_s= ( 1 / (n-1) ) * n sum from 1 to n ( ( x_ri - x⁻_r ) / s_x_r ) ( ( y_ri - y⁻_r ) / s_y_r  )

## Tutorial: Correlation Analysis ##

```stata
	use "WorldBank.dta"
	pwcorr
```

> Results:

             |     year  |    dpt | measles
------------ | --------- | ------ | ----------
        year |   1.0000  |        | 
         dpt |   0.9476  | 1.0000 | 
     measles |   0.9387  | 0.9973 | 1.0000

> Alternative the follow can be used:

```stata
	correlate
```

> Plot correlation:

```stata
	twoway (scatter measles year, sort) (scatter dpt year, sort)
```

> Remember that the **Pearson correlation coefficient** is a measure of the strength of the linear relationship between two variables. So what we're going to do is we're going to test the null hypothesis that rho is equal to zero, our correlation coefficient, against the alternative, that rho is not equal to zero.  
> H_0: p=0  
> H_A: p != 0

```stata
	pwcorr year measles, sig
```

> Results:

             |     year  |  measles
------------ | --------- | --------
        year |   1.0000  | 
     measles |   0.9387  | 1.0000 
             |   0.0000  | 


> And what that does is it gives me the correlation coefficient in this top line. And on the bottom line, that gives me a **p value**. So what I can say here is that my p value is very small. It's less than 0.001. So in this case, I would reject my null hypothesis, and conclude that there is a positive relationship between time and measles vaccination coverage. p < 0.001

```stata
	spearman year measles
```

## Another Correlation Example  ##
> In the HealthExpensesbyCountry.dta dataset, we assess temporal trends in health expenditures per capita and in number of hospital beds (per 1,000 individuals) in four countries: the United States, Great Britain, Japan, and Canada.  
>  
> However, in the following questions, we focus on the United States, but we encourage you to look at the other countries on your own! Health expenditures per capita in the United States are only available after 1995 and up until 2010. Please restrict your analysis to the years 1995-2010 for the questions below.  
>  
> Open the dataset HealthExpensesbyCountry.dta. In this question, you need to restrict to certain subsets of the data when performing your analysis. To do so, it is easiest to use "if" statements in Stata. For instance, to calculate the correlation beteen year and number of hospital beds in the United States between 1995 and 2010, you can type:

```stata
	use "HealthExpensesbyCountry.dta"
	pwcorr hospitalbeds year if country == "United States" & year > 1994, sig
```

> Results:

              | hospit~s | year 
------------- | -------- | --------
 hospitalbeds | 1.0000   | 
         year | -0.9802  | 1.0000 
              |   0.0000 | 


> (You do not need to specify that year <= 2010 because the dataset only contains data through 2010.)

### Consider the following questions: ###
####1. Do the following relationships appear linear (use scatterplots to help answer the question)?####
> **Health expenditures per capita and year from 1995-2010 in the United States**
* => **Yes**
* No

```stata
	graph matrix healthpercapita year if country == "United States" & year > 1994
```

> **Number of hospital beds and year from 1995-2010 in the United States**
* => **Yes**
* No

```stata
	graph matrix hospitalbeds year if country == "United States" & year > 1994
```

####2. Calculate the Pearson correlations for:####
> **Health expenditures per capita and year from 1995-2010 in the United States**  
> => **0.9879**

```stata
	pwcorr year healthpercapita if country == "United States" & year > 1994, sig
```

> Results:

                | year   | healthpercapita 
--------------- | ------ | ---------------- 
           year | 1.0000 | 
healthpercapita | 0.9879 | 1.0000 
                | 0.0000 | 


> **Number of hospital beds and year from 1995-2010 in the United States**  
> => **-0.9802**

```stata
	pwcorr year hospitalbeds if country == "United States" & year > 1994, sig
```

> Results:

             | year    | hospitalbeds 
------------ | ------- | -------------- 
        year | 1.0000  | 
hospitalbeds | -0.9802 | 1.0000 
             | 0.0000  | 


####3.Based on these results (and without doing any further calculations), would you expect annual health expenditures per capita and annual number of hospital beds in the United States between 1995 and 2010 to be positively correlated, negatively correlated, or uncorrelated?####
* positive
* => **negative**
* no correlation

> Plot:

```stata
	twoway (connected healthpercapita hospitalbeds if country=="United States") if year > 1994
```

####4. Based on the scatter plots in question 1 (and without doing any further calculations), would you expect the Spearman and Pearson correlations for health expenditures per capita and year from 1995-2010 in the United States to be similar?####
* => **Yes**
* No

####5. Calculate the Spearman correlation for health expenditures per capita and year from 1995-2010 in the United States and compare to question 2.####
> **1.0000**

```stata
	spearman healthpercapita year if country == "United States" & year > 1994
```

> **Results:**  
> Number of obs = 16  
> Spearman's rho = 1.0000  
> Test of Ho: healthpercapita and year are independent  
> Prob > |t| = 0.0000


####6. True or False: Using the answer from question 5, we can conclude that health expenditures per capita have increased every year since 1995.####
* => **True**
* False


####7. These data are ecological. How does this play a role in the interpretation of the data? (Please discuss on the discussion boards.)####


####8. Examine trends in health per capita, number of hospital beds, and time in the other countries in this dataset. (Please discuss on the discussion boards.)####




> Source: Created from: World Bank, World Development Indicators and Global Development Finance.  
>  
> Hospital Beds: Data after 2005 are extracted from the World Health Statistics Table 6 published by WHO. WHS data is based on PAHO basic indicators 2011. Washington, DC, Pan American Health Organization, 2011 (www.paho.org/English/SHA/coredata/tabulator/newTabulator.htm); European health for all database (HFA-DB). Copenhagen, WHO Regional Office for Europe, 2011 (http://data.euro.who.int/hfadb); Western Pacific Country Health Information Profiles 2011 Revision. Manila, WHO Regional Office for the Western Pacific, 2010 (www.wpro.who.int/countries/countries.htm); Demographic, social and health indicators for countries of the Eastern Mediterranean. Cairo, WHO Regional Office for the Eastern Mediterranean, 2011; additional data compiled as of January 2011 by the WHO Regional Office for Africa and the WHO Regional Office for South-East Asia. Some data are supplemented by country data.  
>  
> Health per Capita: World Health Organization National Health Account database (see http://apps.who.int/nha/database for the most recent updates).

## Sign test ##
> So if we look at the signs, we've got 11 positive signs and two negative signs. And if we test the hypothesis, that this difference is just as likely to
be positive as negative --in other words, that median is 0--then we can ask the question, how often do you do a study with 13 signs and get only two negatives?

```stata
	signtest CF = Healthy
```

## Wilcoxon Signed Rank Test - One Sample ##
> We look at the difference. We could do our sign test on these differences. But Wilcoxon said, no, here's what we'll do. We'll rank the differences. So here it is, we'll just rank them, ignoring the sign.  
> So look at all the ranks associated with negative numbers, and then look at the ranks associated with positive numbers, positive differences.  
> So that's the Wilcoxon signed-rank test, which is the same as --we could do it on one sample, the one I showed you here was on the two sample correlated or dependent situations.

```stata
	signrank placebo = drug
```

## Wilcoxon Rank Sum Test - Two Sample ##
> Throw all samples in one list and rank them.  
> Then look at the total ranks in the one sample, look at the total ranks in
the other sample. If the two samples are the same size, then these two should be roughly the same. If the null hypothesis of no difference is correct. That's exactly like we did with the t.  
> With the ranks, we've got much more control about the variances.

```stata
	ranksum ment_age, by(ind)
```

### In summary, when should we use the Wilcoxon, when should we use student's t? ###
> *Advantage:* Well, the advantage of the Wilcoxon is, we don't need to assume anything about the parent or population distribution of the variable in question. So we do not need to assume normality.   
> We do not need to assume that the population is Normal distributed for Wilcoxon to be applicable.  
> => **So Wilcoxon is more robust than student's t test.**  
>  
> *Disadvantage:* If in fact you were justified in making your normality assumption. So if in fact you could use the t, how much do you lose? And the answer is not that much. **When in fact you have normal data, the Wilcoxon is about 95% efficient.**


## Tutorial: Nonparametrics for Paired Data ##
> Are the data independent or dependent?  
> What parametric and nonparametric tests are available for this type of data?  
> What type of statistical test is most appropriate for this data and why?


### Sign Test ###
#### What are the null and alternative hypotheses? ####
> For the t-test we would use mean but we are using a Nonparametrics test which is using the median.  
> H_0: Median of difference = 0  
> H_A: Median is not equal to 0

```stata
	use "CVOS.dta"
	signtest t6=t0
```

> Results:

        sign | observed | expected
------------ | -------- | ---------
    positive | 8        |  5
    negative | 2        |  5
        zero | 0        |  0
   **TOTAL** | **10**   | **10**

```stata
One-sided tests:  
	Ho: median of t6 - t0 = 0 vs.  
	Ha: median of t6 - t0 > 0  
		Pr(#positive >= 8) =  
		Binomial(n = 10, x >= 8, p = 0.5) =  0.0547

	Ho: median of t6 - t0 = 0 vs.  
	Ha: median of t6 - t0 < 0  
		Pr(#negative >= 2) =  
		Binomial(n = 10, x >= 2, p = 0.5) =  0.9893

Two-sided test:  
	Ho: median of t6 - t0 = 0 vs.  
	Ha: median of t6 - t0 != 0  
		Pr(#positive >= 8 or #negative >= 8) =  
		min(1, 2*Binomial(n = 10, x >= 8, p = 0.5)) =  0.1094
```

> How many positiv and how many negative signs are expected under the null hypotheses. That mean, that the median of the differences is equal to 0.  
> The particularly that it is positiv is 1/2.  
> p-value= **0.1094**

### Signed-Rank Test ###
#### Suppose that instead of conducting the sign test we conduct the Wilcoxon signed-rank test. Which test has more power? Why? ####
> Signed-Rank Test is more powerful. Incorporates the magnitude of the differences via the rank  
> It ranks the magnitude.

## State the null and alternative hypothesis for the Wilcoxon signed-rank test ##
> H_0: Median of difference = 0  
> H_A: Median is not equal to 0


```stata
	signrank t6=t0
```

 sign      | obs    | sum ranks | expected
---------- | ------ | --------- | --------
 positive  | 8      | 50        | 27.5
 negative  | 2      | 5         | 27.5
 zero      | 0      | 0         | 0
 **TOTAL** | **10** | **55**    | **55**

```stata
unadjusted variance       96.25
adjustment for ties        0.00
adjustment for zeros       0.00
                     ----------
adjusted variance         96.25

Ho: t6 = t0
             z =   2.293
    Prob > |z| =   0.0218
```

> p-value= 0.0218 (is less than 0.5)  
> We have more power to detect the difference 


### Summary ###

* Sign test
	* Uses the signs (+ or -) of the differences only
	* Not used often
	* For small n, use binomial distribution to calculate p-value for D (D is a binomial random variable with parameters n and p=1/2 under H_0) - D is not equal to positive signs
* Wilcoxon Signed-Rank Test
	* Nonparametric analogue to the paried t-test
	* Incorporates the magnitude of differences via ranks
	* More powerful than the Sign Test and generally should be used if given a choice between the two


## Tutorial: Nonparametrics for independent samples  ##
> In this tutorial we will use data from the Digitalis Investigation Group.
* The DIG Trial was a randomized, double blind, multicenter trial with more than 300 centers in the US and Canada participating.
* The purpose of the trial was to examine the safety and efficacy of Digoxin in treating patients with congestive heart failure in sinus rhythm.
* The main paper can be found in the New England Journal of Medicine

> The Wilcoxon rank-sum test was used to determine if there were any differences between groups in the number of hospitalizations  
> Examine the distribution of number of hospitalization by treatment group. Are they similar? Are they symmetric?


```stata
	use "dig.dta"
	hist nhosp, by(trtmt)
```




