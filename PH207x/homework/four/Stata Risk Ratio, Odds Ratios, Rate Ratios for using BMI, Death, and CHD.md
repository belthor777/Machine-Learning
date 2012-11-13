# Stata Risk Ratio, Odds Ratios, Rate Ratios for using BMI, Death, and CHD
The following table displays categories of body mass index for the participants at the 1956 exam. (Note: 19 of the 4434 participants are excluded from this table because of missing data on bmi1)

## BMI and Number of People in Each BMI Category
>  BMI Category  | Range of BMI  | Frequency
>  ------------- | ------------- | -------------
>  Underweight   | BMI<18.5      | 57
>  Normalweight  | 18.5≤BMI<25   | 1936
>  Overweight    | 25≤BMI<30     | 1845
>  Obese         | 30≤BMI        | 577

Use Stata to perform the following calculations. Hint: All of the following questions ask you to compare obese subjects to normal weight subjects. Create a new binary variable using bmi1 which equals 1 if the person is obese and 0 if the person is normal weight. Anyone who is underweight or overweight should be missing a value for the new binary variable you create.

	gen newbmi1=.
	replace newbmi1=1 if bmi1>=30 & bmi1 <. 
	replace newbmi1=0 if bmi1>=18.5 & bmi1 <25
	cs death newbmi1, or


>        newbmi1 | Exposed   | Unexposed | Total
> -------------- | --------- | --------- | ------------- 
>          Cases |     259   |       571 | 830
>       Noncases |     318   |      1365 | 1683
>                |                       | 
>          Total |     577   |      1936 | 2513
>                |                       | 
>           Risk |  .4488735 |  .294938  | .3302825
>                |                       | 

>                 |      Point estimate    | [95% Conf. Interval]      
> --------------- | ---------------------- | ------------- | -------------
> Risk difference |         .1539355       |    .1085524   | .1993186 
>      Risk ratio |         1.521925       |    1.358417   | 1.705113 
> Attr. frac. ex. |         .3429373       |    .2638491   | .4135287 
> Attr. frac. pop |          .107013       |
>      Odds ratio |         1.947015       |    1.608816   | 2.35632 (Cornfield)
>                               chi2(1) =    47.62  Pr>chi2 = 0.0000


##### Q1. Calculate the 24-year Risk Ratio for death comparing obese subjects (exposed group, n=577) to normal weight subjects (non-exposed group, n=1936). #####
Hint1 - Is the same procedure as shown in the video at 1:45-3:10
=> Risk Ratio= 1.521925 


##### Q2. Calculate the 24-year Odds Ratio for death comparing obese subjects (exposed group, n=577) to normal weight subjects (non-exposed group, n=1936). #####
Hint1 - Is the same procedure as shown in the video at 1:45-3:10
=> Odds Ratio= 1.947015


##### Q3. Calculate the 24-year Rate Ratio for death comparing obese subjects (exposed group, n=577) to normal weight subjects (non-exposed group, n=1936). #####
Hint1 - Uses the same variables as Q1 and Q2 and the procedure is at 6:39-8:00 of the video.
=> Rate Ratio= 1.632792

ir death newbmi1 timedth

                 | newbmi1                |
                 |   Exposed   Unexposed  |      Total
-----------------+------------------------+------------
 Death indicator |       259         571  |        830
Time [years] to  |   11308.9    40708.74  |   52017.64
-----------------+------------------------+------------
                 |                        |
  Incidence rate |  .0229023    .0140265  |   .0159561
                 |                        |
                 |      Point estimate    |    [95% Conf. Interval]
                 |------------------------+------------------------
 Inc. rate diff. |         .0088758       |    .0058587     .011893 
 Inc. rate ratio |         1.632792       |    1.404331    1.894337 (exact)
 Attr. frac. ex. |         .3875522       |    .2879172    .4721108 (exact)
 Attr. frac. pop |          .120935       |
                 +-------------------------------------------------
                     (midp)   Pr(k>=259) =                   0.0000 (exact)
                     (midp) 2*Pr(k>=259) =                   0.0000 (exact)


##### Q4. Calculate the 24-year Rate Ratio for developing coronary heart disease comparing obese subjects (exposed group) to normal weight (non-exposed group), excluding subjects with prevalent CHD at the 1956 exam. Hint: Use the if/in tab options to restrict the sample to those without prevalent CHD at the 1956 exam (prevchd1 = = 0). #####
Hint1 - Different variables from the previous 3 questions and the procedure is shown at 8:55-10:15 of the video.
=> Rate Ratio= 2.050572

ir anychd newbmi1 timechd if (prevchd1 == 0) 

                 | newbmi1                |
                 |   Exposed   Unexposed  |      Total
-----------------+------------------------+------------
Incident Hosp MI |       180         349  |        529
Time [years] to  |  9387.737    37324.05  |   46711.79
-----------------+------------------------+------------
                 |                        |
  Incidence rate |  .0191739    .0093505  |   .0113248
                 |                        |
                 |      Point estimate    |    [95% Conf. Interval]
                 |------------------------+------------------------
 Inc. rate diff. |         .0098234       |    .0068555    .0127913 
 Inc. rate ratio |         2.050572       |    1.703396     2.46163 (exact)
 Attr. frac. ex. |         .5123311       |    .4129373     .593765 (exact)
 Attr. frac. pop |         .1743282       |
                 +-------------------------------------------------
                     (midp)   Pr(k>=180) =                   0.0000 (exact)
                     (midp) 2*Pr(k>=180) =                   0.0000 (exact)



##### Q5. Calculate the 24-year Rate Ratio for developing coronary heart disease comparing (obese or overweight) subjects (exposed group) to normal weight (non-exposed group), excluding subjects with prevalent CHD at the 1956 exam. #####
Hint1 - Different variables from the previous 3 questions and the procedure is shown at 8:55-10:15 of the video.
=> Rate Ratio= 1.736394


gen newbmi3=.
replace newbmi3=1 if ( bmi1>=30 & bmi1 <. ) | ( bmi1>=25 & bmi1 <30 )
replace newbmi3=0 if bmi1>=18.5 & bmi1 <25
ir anychd newbmi3 timechd if (prevchd1 == 0) 

                 | newbmi3                |
                 |   Exposed   Unexposed  |      Total
-----------------+------------------------+------------
Incident Hosp MI |       686         349  |       1035
Time [years] to  |  42251.22    37324.05  |   79575.28
-----------------+------------------------+------------
                 |                        |
  Incidence rate |  .0162362    .0093505  |   .0130066
                 |                        |
                 |      Point estimate    |    [95% Conf. Interval]
                 |------------------------+------------------------
 Inc. rate diff. |         .0068857       |    .0053241    .0084473 
 Inc. rate ratio |         1.736394       |    1.524219    1.980922 (exact)
 Attr. frac. ex. |         .4240938       |    .3439265    .4951846 (exact)
 Attr. frac. pop |         .2810902       |
                 +-------------------------------------------------
                     (midp)   Pr(k>=686) =                   0.0000 (exact)
                     (midp) 2*Pr(k>=686) =                   0.0000 (exact)


##### Q6. Calculate the 24-year Rate Ratio for developing coronary heart disease comparing underweight subjects (exposed group) to normal weight (non-exposed group), excluding subjects with prevalent CHD at the 1956 exam. #####
=> Rate Ratio= 0.5731434

gen newbmi2=.
replace newbmi2=1 if bmi1<18.5 & bmi1 >0
replace newbmi2=0 if bmi1>=18.5 & bmi1 <25
ir anychd newbmi2 timechd if (prevchd1 == 0) 

                 | newbmi2                |
                 |   Exposed   Unexposed  |      Total
-----------------+------------------------+------------
Incident Hosp MI |         6         349  |        355
Time [years] to  |   1119.57    37324.05  |   38443.62
-----------------+------------------------+------------
                 |                        |
  Incidence rate |  .0053592    .0093505  |   .0092343
                 |                        |
                 |      Point estimate    |    [95% Conf. Interval]
                 |------------------------+------------------------
 Inc. rate diff. |        -.0039913       |   -.0083903    .0004076 
 Inc. rate ratio |         .5731434       |    .2089001    1.260145 (exact)
 Prev. frac. ex. |         .4268566       |   -.2601451    .7910999 (exact)
 Prev. frac. pop |         .0124311       |
                 +-------------------------------------------------
                     (midp)   Pr(k<=6) =                     0.0798 (exact)
                     (midp) 2*Pr(k<=6) =                     0.1596 (exact)



