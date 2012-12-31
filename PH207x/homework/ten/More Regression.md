# More Regression #

``stata
	regress nickel vanadium
	twoway (scatter nickel vanadium)
```

##### 1. Examine the relationship between vanadium (another marker of oil in sediment) and nickel using a scatter plot. Does this relationship appear linear? #####
* Yes
* No 

##### 2. How many outliers do you observe in this scatterplot? #####
As the investigator, it is important to determine the true cause of any observed outliers. If these are a result of error they should be removed, however outliers may also be indicators of a real but unusual occurrence that warrants further investigation. 

##### 3. How much does nickel increase, on average, for a one mg/kg increase in vanadium? #####
Fit a linear regression model with nickel as the outcome and vanadium as the explanatory covariate (Model 4). Use this model to answer questions 3 and 4.
