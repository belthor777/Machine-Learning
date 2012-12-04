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
> = a*d / b*c

> Approx. Normal:  
> ^se[ln(^OR)]= sqrt( 1/a + 1/b + 1/c + 1/d )

## Berkson's Fallacy ##
He quantified the fallacy (sampling error)


## Yule Effect (Simpson's Paradox) ##
> Woman who could be classified as smokers/non-smokers in a 20 year follow-up of a one-in-six survey of the electoral roll in 1972-1974 in Whickham, UK.

           | Smokers | Non-Smokers | Total
---------- | ------- | ----------- | ----- 
Dead       |  139    | 230         | 369
Alive      |  443    | 502         | 945
Mortality  |  0.239  | 0.314       | 0.281

> Use Decomposition Rule / Proportion / Mean  
> The composition is the story: You should not compare the means of two groups if the composition are different. Because you might just be confounding a lot of things together and blurring the issue at stake

### Yule Effect Demonstration  ###
> Imagine you are a researcher studying YSS and the drugs that might prevent it. You decide to perform an experiment to test whether or not the promising drug Twoohsevenex is effective at preventing YSS.  
>  
> You perform a study by taking 200 men and 200 women, all of whom are at risk but do not currently have YSS, and separating them randomly into two groups. The "treated" group receives Twoohsevenex, while the control group recieves a placebo.  
>  
> At a follow up exam 5 years later, you observe the following results (Patients with YSS/All Patients in Category):   
>  
> Your results:

       | Treated | Control
------ | ------- | -------- 
Men    | 40/100  | 45/100
Woman  | 25/100  | 30/100
Total  | 65/200  | 75/200

> Your colleague, Doctor Drummond, insists that the results of his study of 2000 patients show that untreated patients do better on average than those recieving Twoohsevenex.  
>  
> Being a diligent statistician, you explore his results and find that within each sex/treatment group, his patients fared similarly to your own. Still, on the whole, his study showed that the untreated group did better.  
>  
> Use the sliders below to adjust the proportions of men and women in each group in a study of 2,000 people and find a case in which the aggregate performance of each treatment category makes it appear that Twoohsevenex is worse for patients than the placebo even though within each gender category, Twoohsevenex patients clearly fared better.  


