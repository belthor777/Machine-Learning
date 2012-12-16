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



