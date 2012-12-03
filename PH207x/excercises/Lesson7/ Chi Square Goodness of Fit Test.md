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


