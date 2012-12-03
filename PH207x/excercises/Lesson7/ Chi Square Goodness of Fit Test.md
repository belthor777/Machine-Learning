#  Chi Square Goodness of Fit Test - x² statistics #
>  
> x²= SUM of all cells [ ( obs- exp )² / exp ]  
> d.f.=(#rows-1)(#columns-1)  
>  

	tab diabetes1 sex1, chi col
	tab diabetes3 sex1, chi col
	tab diabetes3 sex1, chi col miss


## Continuity correction factor ##
> In 2x2 tables (only) we apply a continuity correction factor:  
> x²= SUM of all cells [ ( |obs-exp|-0.5 )² / exp ]  
>  
> So x² is an idea of how far these expecteds are from these observed.  

	cci 358 229 2492 2745

# R X C Tables  #
> e.g. Accuracy of Death Certificates
> CS= Certificate Status

	tabi 157 18 54\268 44 34

Hospital | CS Conf. Accur. | CS Inacc. No. Ch. | CS Incorr. Recode | Total
-------- | --------------- | ----------------- | ----------------- | --------
Comm.    | 157             | 18                | 54                | 229
Teach.   | 268             | 44                | 34                | 346
Total    | 425             | 62                | 88                | 575

	tab diabetes3 sex1, chi col miss

> Now the null hypothesis is that it doesn't matter. The row classification is independent of the column classification.That means that take these 88, roughly a third of them should go up
here and a third of them should come down here.

	tabplot hospital status [iw=frequency],perc(status)
	tabplot hospital status [iw=frequency],perc(hospital)

> When we submit this to Stata we get that the p-value is 0.001.That's telling us that when we compare this to that, 18 to the 24.7, 54 to the 35, to 268 and compare that to 255.7, when we compare what we actually observed to what we expect to see if there is no relationship between the row and column classifications, then the value we get is much bigger than we would expect purely by chance.  
>  
> And the p-value is there, less than 0.005. So we would reject this null hypothesis at the 0.05 level. And that is how we test an r by c. It's a simple extension of the two by two table except, remember, we don't do a continuity correction. We only do that with the two by two tables.


