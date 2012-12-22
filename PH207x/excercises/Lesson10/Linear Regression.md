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



