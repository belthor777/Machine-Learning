# Tutorial: Gender and Visiting the Doctor #
> Rather than examining the health disparities question of the relationship between poverty and doctor visits, let’s switch gears and look at the relationship between gender and visiting the doctor within the past 12 months. Use chis_healthdisparities.dta dataset.  
>  
> To answer these questions, you can use the cs command in Stata. (Note: make sure you don't get the order of the case and exposed variables mixed up if you work from the command-line in Stata). To use the cs command, we need for the exposed variable to be coded as 0 or 1.  
>  
>  First, generate an indicator that is equal to 1 if a participant is female and 0 if the participant male. Note that gender is coded as 2 for females, 1 for males. To generate the new indicator, type:


	gen female = gender - 1


## 1. Estimate the risk difference for visiting the doctor in the past 12 months for self-reported female versus male study participants (using the female variable). Calculate risk difference using proportion in females minus proportion in males.##
>  Estimate of risk difference: **  **  
>  
> 95% Confidence Interval: [, ]  


## 2. Estimate the odds ratio for visiting the doctor in the past 12 months for self-reported female versus male study participants. ##
> Estimate of odds ratio: ** **  
>  
> 95% Confidence Interval: [, ]  


## 3. Examine your estimated risk difference and estimated odds ratio, and their respective confidence intervals. Do you reach the same conclusion about the association between gender and visiting the doctor using these two measures of association?  ##
> Yes  
> No


