# Simple Linear Regression #
 We use data from the Environmental Protection Agency (EPA) to track the BP oil spill in Louisiana between May and September 2010. The oil well exploded on April 20, 2010, was capped in July and was declared dead in September 2010. The oil spill killed wildlife in the Gulf of Mexico and posed a significant public health risk to clean-up workers and residents of the Gulf Coast (Solomon and Janssen 2010). The EPA monitored air quality and took samples of sediment to measure the impact of the oil spill. For more information from the EPA, visit http://www.epa.gov/bpspill/sediment.html#understanding.   
  
Use the dataset oilspill.dta to answer the following questions.  
  
Simple Linear Regression. In this example, we track changes in the amount of nickel found in sediment along the Louisiana coast between May and September 2010 (note that there is no data from July). Nickel is a metal that is found in sediment contaminated with oil. We model the amount of nickel as a function of time (month) using linear regression.  
  
Fit a linear regression model with nickel as the outcome and month as the explanatory variable. Using indicator variables, model month as a categorical covariate (i.e. for the variable "month", it is coded numerically as May = 5, June = 6, August = 8, September = 9). Call this Model 1.   
  
Assume the assumptions of linear regression are met for this model. You can make histograms of nickel by month to visually verify that the data does not appear to be skewed or any other evidence that would suggest a violation of the assumptions necessary to analyze this data using linear regression.  
  
**TODO:**
* Fit a linear regression model with nickel as the outcome and month as the explanatory variable. 
* model month as a categorical covariate

```stata
	histogram nickel, by(month)
	xi: regress nickel i.month

	predict r, residuals
	qnorm r
	swilk r
	estat hettest
```

##### 1. Does the amount of nickel in the soil tend to increase over the four month period? #####
* Yes
* No

##### 2. Examine the regression coefficients. Compare how the average nickel amount changes by month. Is it reasonable to assume that average amount of nickel increases linearly by month? #####
* Yes
* No

##### 3. Make a residual plot. #####

1. Is there any evidence of outliers? 
	* Yes
	* No

2. Is there any evidence of heteroscedasticity?
	* Yes
	* No

##### 4. Using Model 2, it is estimated that, on average, nickel increases by ______ each month, from May to September.. #####
Now, assume the amount of nickel increases linearly by month, and the assumptions of linear regression continue to hold. Fit a model with nickel as the outcome and month modeled as a continuous explanatory variable. Call this Model 2. 
> **Hint1:** Read the interpretation of q4 given in Tutorial: Simple Linear Regression pdf . the ans is in the sme table 

```stata
	histogram nickel, by(month)
	xi: regress nickel i.month
	regress nickel month
```


##### 5. What is the 95% confidence interval for the average increase in nickel each month? #####
Lower Bound  
Upper Bound  

##### 6. Given that the relationship between month and nickel appears to be linear, is it reasonable to use Model 2 to predict the amount of nickel in the soil in July 2010? #####
* Yes
* No

##### 7. Given that the relationship between month and nickel appears to be linear, is it reasonable to use Model 2 to predict the amount of nickel in the soil in October 2010? #####
* Yes
* No

##### 8. What is the average amount of nickel in the soil during August 2010?  #####

1. According to model 1 (Hint: Think about how dummy/indicator variables are coded.)
2. According to model 2

##### 9. True or False: Model 1 makes stronger modeling assumptions than Model 2. #####
* Yes
* No



