# Correlation and Nonparametrics #
> Link: http://istics.net/stat/correlations/


## Pearson's Correlation Coefficient ##
## Inference on Rho  ##
> Sampling distribution:  
> If X & Y are normally distributed and rho=0, then  
>  
> t_n-2= r/sqrt( (1-r²) / (n-2) )  

### Example ###
> r=-0.829 for DPT example  
> t= r*sqrt( (n-2) / (1-r²) )  
> t= -0.829*sqrt( (20-2) / (1-(-0.829)^2) )= -6.29  
>  
> versus t with 18 degrees of fredom, so p<0.001.  
> So reject J_0: rho=0


	pwcorr diabp1 sysbp1 if _n<51 , sig


## Missconceptions ##
## Spearman's Rank Correlation Coefficient ##
> When you have any doubts about the distribution of your x's and your y's -whether they're normal or not- go with the Spearman's.  
> Rank the Data:


 i       | x   | y    | x_r  | y_r  | d  | d²
-------- | --- | ---- | ---- | ---- | -- | --
 1       | 1.3 | 14.3 | 2    | 2    | 0  | 0
 2       | 1.7 | 14.7 | 4    | 3    | 1  | 1
 3       | 0.8 | 18.0 | 1    | 4    | -3 | 9
 4       | 1.4 | 12.1 | 3    | 1    | 2  | 4


> x and y are Raw Data  
> x_r and y_r are Ranks  
> d is the difference between x_r and y_r by using:

	r_s= ( 1 / (n-1) ) * n sum from 1 to n ( ( x_ri - x⁻_r ) / s_x_r ) ( ( y_ri - y⁻_r ) / s_y_r  )


