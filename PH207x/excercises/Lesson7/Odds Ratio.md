# Odds Ratio #
> Suppose we have a disease (e.g. lung cancer)  
> And two groups (e.g. smokers, non-smokers)  
>  
> => Odds Ratio quantifies the relationship  
>  
> Relative odds (OR)= ( P(D|S)/(1-P(D|S)) ) / ( P(D|S_c) / (1-P(D|S_c)) )  
> D is equal to disease  
> S is equal to smokers  
> S_c is equal to non-smokers

## Theory for odds ratio ##

           | Exposed | Unexposed | Total
---------- | ------- | --------- | ----- 
Disease    |  a      |  b        | a+b
No Disease |  c      |  d        | c+d
Total      | a+c     | b+d       | n

> Relative odds (OR)= ( ^P(D|E)/(1-P^(D|E)) ) / ( ^P(D|E_c) / (1-^P(D|E_c)) )  
> = (a/(a+c))/(c/(a+c)) / (b/(b+d))/(d/(b+d))  

