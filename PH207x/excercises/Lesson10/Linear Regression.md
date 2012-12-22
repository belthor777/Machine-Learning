# Linear Regression #
ρ

```math
	m*x + b
```


## Simple Linear Regression ##
> m= slope

|video|(http://www.youtube.com/watch?v=fFO-Y7NfqMg&feature=g-all-u)

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



