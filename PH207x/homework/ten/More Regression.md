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

```stata
	regress nickel vanadium
```

##### 4. How much does nickel increase, on average, for a 10 mg/kg increase in vanadium? #####

```stata
	regress nickel vanadium
```

##### 5. In Models 1 and 2 we saw that nickel levels seemed to increase each month. Does adding month to the model with vanadium as an explanatory covariate substantially improve the fit? #####

```stata
	regress nickel vanadium
	regress nickel month vanadium
```

##### 6. Think about the results from the various models. Compare the adjusted R-squared for Model 2 with that from Model 5. Does it appear that vanadium is a stronger predictor of nickel levels than month?  #####

```stata
	regress nickel month
	regress nickel month vanadium
```

