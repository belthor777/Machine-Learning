#  Multiple Linear Regression #
Again, we model the amount of nickel found in the sediment. Now, we model nickel as a function of both time (month) and location (longitude). The Gulf Coast in Louisiana is somewhat horizontal, so for simplicity we will ignore  longitude in this problem.  
  
Fit a linear regression model with nickel as the outcome and with month and longitude as explanatory covariates. Model month as a continuous variable, as in Model 2 from the previous question. Call this Model 3. Assume the assumptions of linear regression hold.   
  
https://maps.google.com/maps/ms?msid=205190672353608758732.0004d1dab620c7540a566&msa=0&ll=29.544788,-91.384277&spn=4.758846,7.613525  
  
  
**TODO:**
* Fit a linear regression model with nickel as the outcome and with month and longitude as explanatory covariates

```stata
	regress nickel month longitude
	regress nickel longitude
	twoway (scatter nickel longitude)
```

##### 1. Compare the adjusted R-squared from Models 2 and 3. Does the addition of longitude improve the adjusted R-square? #####
* Yes
* No 

##### 2. Test whether the coefficient for longitude in the model is equal to 0 at the 0.05 level of significance. #####

1. What is the estimated coefficient? 

2. The estimated standard error of the estimated coefficient?

3. The estimate of the test statistic?

4. The number of degrees of freedom of the distribution of the test statistic under the null hypothesis? 
> **Hint1:** n-k-1: n is the sample size k is the number of variables 1 is 1, obviously

5. The p-value?

6. Your conclusion?
	- We have no evidence that, for a given month, average nickel levels have a linear relationship with longitude. 
	- We have evidence that, for a given month, average nickel levels have a linear relationship with longitude. 


##### 3. For each month, make a scatter plot with longitude on the x-axis and nickel on the y-axis to assess the linearity assumption. Conditional on month, does the relationship between nickel and longitude appear to be linear? (Hint: try the example problems in the lecture sequence to help with constructing the scatter plot.) #####
* Yes
* No 

In this example, our regression results show that we cannot assume a linear relationship between nickel levels and longitude, conditional on month. Incorporating location into statistical models is a whole genre of what is conveniently called spatial statistics. It is well beyond the scope of this course, but this is a brief introduction into “thinking spatially”. We need a more flexible model to reflect spatial heterogeneity.
