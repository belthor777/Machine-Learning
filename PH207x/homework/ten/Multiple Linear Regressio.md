#  Multiple Linear Regression #
Again, we model the amount of nickel found in the sediment. Now, we model nickel as a function of both time (month) and location (longitude). The Gulf Coast in Louisiana is somewhat horizontal, so for simplicity we will ignore latitude in this problem.

Fit a linear regression model with nickel as the outcome and with month and longitude as explanatory covariates. Model month as a continuous variable, as in Model 2 from the previous question. Call this Model 3. Assume the assumptions of linear regression hold. 

##### 1. Compare the adjusted R-squared from Models 2 and 3. Does the addition of longitude improve the adjusted R-square? #####
* Yes
* No 

##### 2. Test whether the coefficient for longitude in the model is equal to 0 at the 0.05 level of significance. #####

1. What is the estimated coefficient? 

2. 


##### 3. For each month, make a scatter plot with longitude on the x-axis and nickel on the y-axis to assess the linearity assumption. Conditional on month, does the relationship between nickel and longitude appear to be linear? (Hint: try the example problems in the lecture sequence to help with constructing the scatter plot.) #####
* Yes
* No 

In this example, our regression results show that we cannot assume a linear relationship between nickel levels and longitude, conditional on month. Incorporating location into statistical models is a whole genre of what is conveniently called spatial statistics. It is well beyond the scope of this course, but this is a brief introduction into “thinking spatially”. We need a more flexible model to reflect spatial heterogeneity.
