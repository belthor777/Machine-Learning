# Linear Regression #
ρ

```math
	y= m*x + b
```


## Simple Linear Regression ##
> m= slope

### Correlation and slope ###
> If X & Y are jointly normal (for each fixed X(Y) then Y(X) is normal) then

```math
	μ_x|y= α + β*x
```

> and

```math
	β= ( σ_y / σ_x ) * ρ
```

> **which shows the relation between correlation and slope of regression**  
> **=> The correlation coefficient is the slope of the regression line. If we're looking at the standardized variates.**

### Equivalence ###
> So with normal data the following 3 hypotheses are equivalent:

```math
	H_0: ρ=0  
	 <=>  
	H_0: β=0  
	 <=>  
	H_0: σ_y=σ_y|x
```

## Least Squares ##
> Applet: http://illuminations.nctm.org/LessonDetail.aspx?id=L455  
> Stata Command:

```stata
	regress headcirc gestage
```

> Fitted (least squares) regression line: 

```math
	headcirc= 3.914 + 0.78*gestage + e
```

> where standard dev of e = 1.59

## Transformations ##
> Options for running the regression in such cases_

1. Do a non-linear regression
2. Transform the ys or the xs: i.e. look at y^p or x^p e.g.  
	y^-2, y^-1,y^-0.5, ln(y), y^0.5, y, y^2  
	x^-2, x^-1,x^-0.5, ln(x), x^0.5, x, x^2

* going up the ladder -> (going to the right)
* goin down the ladder <- (going to the left)

##  More on Transformations ##
> This applet will give you some experience with transformations and what happens to curve shapes. Remember, we are here because we know how to handle linear regression. So if we are faced with a non-linear relationship then if we can linearize it then use the tools we have for linear regression.  
>  
> As you learnt, we can transform the y variable or the x variable. You have that capability by pressing any one of the green arrow heads in the top left-hand corner of the plot below. Pushing the up arrow makes you climb the appropriate ladder on the right of the graph. Clicking the down arrow makes you go down the ladder. The dot on the ladder tells you where you are. You always start at x, y.  
> When you look at the plot you will see a series of points on the graph paper. You can generate a new set of points by clicking on either the "ideal" or "realistic" data buttons near the bottom. The latter button shows noisy data more like what you'd encounter in the real world.  
>  
> Once you have your data, the challenge is to try and choose the y or x (or both) transform to straighten out the x y relationship. Try it first with no noise and once you get the hang of it, try it with noise added.  
>  
> The green dots are the original data, the blue dots are the transformed data. The straight lines are the least squares lines through the points.  

> Link: https://www.edx.org/courses/HarvardX/PH207x/2012_Fall/courseware/Week_10/week10:bio10/19

## Multiple Linear Regression ##

```math
	y= α + β_1*x_1 + β_2*x_2 ... + β_q*x_q + ε
```
> Asume:  

* For fixes x_1, ..., x_q, y is **normally** distributed with mean μ_y|x_1 ...., x_q and standard deviation σ_y|x1, ...., x_q
* μ_y|x_1, ...., x_q is linear in x_1, ...., x_q   
i.e. μ_y|x_1, ...., x_q= α + β_1*x_1 + ... + β_q*x_q
* Homoscedasticity  
i.e. μ_y|x_1, ..., x_q is constant
* The y's are independent

> => **Minimize SUM from i=1 to n (y_i - a - b_1*x_1... -b_q*x_q)^2**

```stata
	regress headcirc gestage weight
```

```math
	headcirc= 8.3 + 0.45*gestage + 0.0047*weight + e
```
> where standard dev of e = 1.27


## Indicator Variables  ##
> Sometimes in the literature you'll see them called dummy variables, but why inflict that on them.  
> So for example, let's look at tomexia. 

* So if the mother was toxemic at delivery, then we say 1 this variable will take on the value 1.  - **yes**
* If the mother was not, then this variable will take on the value 0. **no**

### Estimated regression equation ###

```math
	ŷ= 1.50 + 0.874*gestage - 1.41*tox
```

> *For toxemics:*
```math
	ŷ= 0.83 + 0.874*gestage
```

> *For non-toxemics:*
```math
	ŷ= 1.50 + 0.874*gestage
```

```stata
	regression headcirc gestage tox
```

#### Test with T-Test  #####
> And so here's the t-test for head circumference by toxemia. And we see that we have 79 observations who are non toxemic and 21 who are toxemic. And we see that the t-test is not significant.

```stata
	ttest headcirc, by(tox) unequal
```

> So all of this is very complex. How do all of these things work together? So what we can do is we can generate a variable called gestational age times toxemia.

```stata
	gen gestox = gestage*tox
	regression headcirc gestage tox gestox
```

## Subset Regression ##
> So what you're doing when you're investigating is making sure that you're measuring everything, but then, you know that all these things, everything under the sun is interrelated with each other. And so that's not what you're looking for, you're looking to see is there a parsimonious way of explaining what's going on in terms of the more important, most important variables, and this we can generically label or umbrella, if you will, as the subset regression problem.  
>  
> So you've got outcome variable here, in this case, head circumference, and then you've got a whole bunch of variables that you can use to explain this. Which ones do you use in what combinations, et cetera, that's called the subset regression problem.

* **All possible models**  
If q sizeable, 2^q huge

* **Forward Selection**  
(i)Choose one Variable, (ii) push this into the model and then (iii) look at the other variables

* **Backward Selection**  
(i) Fit "all", (ii) Drop least signicant and then (iii) go back to (i)

> So there are **q** variables, then we can do all two to the q. Turns out it's two to the q model fits. Now, apart from the fact that if you've got thousands of observations and q is sizable, it's going to take you the rest of your life to do all  

### Collinear Problem - Multi-Collinearity ###
> So if you have a high correlation, you might run into interpretation problems and fitting problems. That's the collinear problem.  
> **collinear= Variables are perfectly correlated with each other.**  

> Results:

           | No interaction term | Interaction term 
---------- | ------------------- | ------------------ 
Coeff      | -1.412              | -2.815 
Std. Err.  | 0.406               | 4.985 
T-Stat     | -3.477              | -0.565 
P-Value    | 0.001               | 0.574 
R²         | 0.653               | 0.653 
Adj. R²    | 0.646               | 0.642 

> **Hint:** Look at the Standard Error, T-Statistics and R-Squares.  
* Look at the standard error, there's a tenfold increase in the standard error, and that's usually a tip-off that you've got some **multi-collinearity** possibly.  
* The T statistic went from a significant to quite insignificant. By adding one term you shouldn't be seeing this big a difference, unless it's very highly related to before.  
* And look at the P value went from 0.001 to 0.574, and the R-squared didn't change. 
* The R-squares didn't change at all. They're basically the same thing. Tip-off that you've got **multi-collinearity**.

## Example: Hospital Ratings ##
> In the tutorial sequence this week, we examine predictors of hospital ratings using publicly available hospital-level survey information from https://data.medicare.gov . The dataset contains "a list of hospital ratings for the Hospital Consumer Assessment of Healthcare Providers and Systems (HCAHPS). HCAHPS (http://www.hcahpsonline.org/home.aspx) is a national, standardized survey of hospital patients about their experiences during a recent inpatient hospital stay." To access this dataset online, go here (https://data.medicare.gov/dataset/Survey-of-Patients-Hospital-Experiences-HCAHPS-/rj76-22dk).  
>  
> We excluded any hospitals with missing data (complete case analysis). We aim to examine trends in hospitals, and assume that this sample is representative of hospitals in the United States. Each line in this dataset represents one hospital. The variables are continuous, representing percentages from patient respondents.  
>  
> Hospitals aiming to improve their ratings could use this database to find the areas that are influential for patient ratings. They could examine synergies between variables to pinpoint exactly where they should invest their improvements to provide the best patient experience. Linear regression is a tool that facilitates such analyses.  
>  
> On the boards below, discuss any advantages to using linear regression, rather than simple calculating correlations, in this application.  
>  
> (The dataset is included below, if you would like to further familiarize yourself with the data before beginning the tutorial sequence.)

```stata
	use "hospitaldata.dta"
```

## Tutorial: Simple Linear Regression ##
> We examine predictors of hospital ratings using publicly available *hospital-level* survey information from https://data.medicare.gov .

* **nursealways** - percent of patients in a hospital who said their nurse always communicated well (*explanatory*)
* **recommendyes** - percent of patients who would always recommend the hospital (*outcome*)

```stata
	use "hospitaldata.dta"
	twoway (scatter recommendyes nursealways)
	pwcorr recommendyes nursealways
```

             | recommendyes  | nursealways
------------ | ------------- | ------------
recommendyes |   1.0000      | 
 nursealways |   0.6580      | 1.0000 

> I find that the correlation between these two variables is **p=0.66**. So it does appear that they are positively correlated.

### State your model ###
> Y_i= % patients in hospital i who would always recommend this hospital. | i=1,2,...,n  
> X_i= % patients in hospital i who say that their nurse always communicated well.  
> ε_i= residual error -> ε_i ~ N(0, T²)  
> y_i= α + β_1*x_i + ε_i
> μ_y_i|x_i= E(y_i|x_i)= α + β*x   | Y_i ~ N(μ_y_i|x_i, σ²)

### Assumptions ###

* We can assume that the **hospitals are independent** of each other, and so it seems reasonable to say that we have independent observations, or independent hospitals.
* We need to assume that there's a **linear relationship between the outcome in covariate**. And we looked at the scatter plot and this looked pretty reasonable.
* The next two assumptions are the ones that are a little bit hairier to try to interpret in practice:
	+ The first is that **Y_i|X_i ~ N** - So the outcome given the covariate is **normally distributed**.
	+ The next assumption we need to make is **homoskedasticity**, and this is just a very long word that means constant variance.

```stata
	regress recommendyes nursealways
```

```
      Source |       SS       df       MS              Number of obs =    3570
-------------+------------------------------           F(  1,  3568) = 2723.72
       Model |  144368.851     1  144368.851           Prob > F      =  0.0000
    Residual |  189118.972  3568  53.0041962           R-squared     =  0.4329
-------------+------------------------------           Adj R-squared =  0.4327
       Total |  333487.823  3569  93.4401297           Root MSE      =  7.2804

------------------------------------------------------------------------------
recommendyes |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
 nursealways |   1.159487   .0222169    52.19   0.000     1.115928    1.203046
       _cons |  -19.21559   1.712829   -11.22   0.000    -22.57381   -15.85737
------------------------------------------------------------------------------
```

```stata
	sum nursealways
```

    Variable |       Obs   |       Mean  |    Std. Dev.  |  Min   | Max
------------ | ----------- | ----------- | ------------- | ------ | ------
 nursealways |      3570   |   76.90028  |    5.485264   |   48   |  98


```math
	y_i= -19.21559 + 1.159487*x_i + ε_i
	ε_i ~ N(0, 7.2804²)
```

> **Important:** It is a very important aspect of linear regression that you always need to keep in mind that we can't extrapolate beyond the minimum value (here: 48).

### Test that hypothesis β= 0 vs β !=0 ###
> The next thing I want to do is I want to test the hypothesis that beta is equal to 0 versus the alternative the beta is not equal to 0.  
> H_0: β= 0  
> H_A: β != 0  
>  
> ^β=1.16  
> ^σ(β)=Std. Err.= 0.02  
> t=t-test=52.19


> Now I know that under my null hypothesis that my t statistic follows a t distribution with **Z=n-2** degrees of freedom. And I see up here that my number of observations is **n=3,570**, so it would be **3,568 degrees** of freedom.  
> Z ~H_o t_3568 => p-value < 0.001

> **Conclusion:** I would reject my null hypothesis and conclude that the percent of patients who say that a nurse always communicates well is positively correlated with a percent of patients who would always recommend
a hospital.

### Amount of variability explained by my covariate ###
> I can look at the **r²**. For this model my **r²=0.4329**.  
> r² is known as the coefficient of determination, and in this example it tells us:
> * that 43% of the variability among the observed values of *recommendyes*, 
> * the outcome, 40% of that variability is explained by the linear relationship with *nursealways*.
> * the remaining 57% of the variability is unexplained, implying that there are other factors that contribute to whether the percent of patients
> * the remaining 57% of the variability is unexplained, implying that there are other factors that contribute to the variability in this *recommendyes* outcome.

### Analyze by plot ###

#### Residual versus fitted plot ####
```stata
	rvfplot
```

> What I'm looking for here is I don't want to see any trends in these residuals.
> * I see that they're about means 0.
> * I don't see any weird trends going on.
> * If I saw any U shapes or the residuals getting larger over time, these would be problems.
>  
> So as long as you don't see any patterns in that residual plot, that **means your model's probably doing OK**.

#### Residual versus predictor plot ####
```stata
	rvpplot nursealways
```

> So I can look at the residuals now as a function of the covariate in the model.  
> And again, I don't see any major trends in this residual plot. Things look OK, so I can assume that the fit of my model looks OK. 
> * I don't see any major outliers.
> * I don't see anywhere trends in my residuals.
>  
> However, there's really typically never a definitive answer to whether your **model fit is good**.

#### Predict the expected percent of patients ####
> The next thing I want to do is I want to predict the expected percent of patients who will always recommend the hospital when the percent of nurses who always communicate well is 80%

> ⁻y_i|x_i=80  

> So what I want to do is I want to look at the average value of Yi when Xi is equal to 80. And the way that I can estimate that guy is I can say this is equal to alpha hat plus beta hat times, and I just plug in 80 for Xi.

> y_i= ^α + ^β*80=73.54339

```stata
	lincom _cons + nursealways*80
```

 recommendyes | Coef.      |   Std. Err. |      t  |   P>|t| |  [95% Conf.  | Interval]
------------- | ---------- | ----------- | ------- | ------- | ------------ | -----------
 1            | 73.54339   | 0.1399631   | 525.45  | 0.000   | 73.26897     | 73.8178


## Simple Linear Regression ##
Consider the following linear regression model. We have a continuous outcome and a continuous explanatory covariate for *n* different independent observations. Notation:
* Y_i = outcome for i = 1,...,n
* X_i = covariate for i = 1,...,n

We fit the linear regression model: 
```math
	Y_i = α + β*X_i + ε_i
```
where ε_i ~ N(0,σ²).  
  
Asume the assumptions for simple linear regression are met.

True or false:

#### 1. If β is positive, the Pearson correlation will always be positive. ####
* True
* False

#### 2. If β is positive, the Spearman correlation will always be positive. ####
* True
* False

#### 3. α is defined as the value of Y_i when X_i=0. ####
* True
* False

#### 4. We can predict the expected value of Y_i given X_i. ####
* True
* False

#### 5. The variance of Y_i is σ². ####
* True
* False


