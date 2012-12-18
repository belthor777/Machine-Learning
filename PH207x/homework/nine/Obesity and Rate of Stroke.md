## Obesity and Rate of Stroke  ##
> In the Framingham dataset that can be downloaded from the course website, we would like to examine the association between obesity and the rate of stroke. Since people with hypertension may have a higher body mass index and they are also at greater risk of a stroke, you may be concerned about confounding by hypertension.

#### 1. Use the Framingham dataset and Stata to calculate the incidence rate ratio of stroke comparing obese participants (bmi1>=30) to all other participants. The variable for incident stroke in this dataset is “stroke” and number of years a person was followed for stroke is recorded in the “timestrk” variable in the NHLBI dataset. ####
> => **1.79188**

```stata
	use "framingham_dataset.dta", clear

	gen bmi4cat=.
	replace bmi4cat=0 if (bmi1<30)
	replace bmi4cat=01 if (bmi1>=30)

	ir stroke bmi4cat timestrk
```

```stata
                 | bmi4cat                |
                 |   Exposed   Unexposed  |      Total
-----------------+------------------------+------------
Incident Stroke  |        85         330  |        415
Time [years] to  |  11144.75    77530.79  |   88675.54
-----------------+------------------------+------------
                 |                        |
  Incidence rate |  .0076269    .0042564  |     .00468
                 |                        |
                 |      Point estimate    |    [95% Conf. Interval]
                 |------------------------+------------------------
 Inc. rate diff. |         .0033705       |    .0016854    .0050557 
 Inc. rate ratio |          1.79188       |    1.394785    2.280687 (exact)
 Attr. frac. ex. |          .441927       |    .2830436    .5615356 (exact)
 Attr. frac. pop |         .0905152       |
                 +-------------------------------------------------
                     (midp)   Pr(k>=85) =                    0.0000 (exact)
                     (midp) 2*Pr(k>=85) =                    0.0000 (exact)
```


#### 2. Using the Framingham dataset and Stata, what is the incidence rate ratio (round to two decimal points) of stroke among obese participants (bmi1>=30) compared to all other participants after adjusting for prevalent hypertension at visit 1 (prevhyp1)? ####
> **Hint1:** Are you entering the correct number? You should have two to choose from, one you have already used and the other is the required adjusted value.
> => **1.197284**

```stata
	use "framingham_dataset.dta", clear

	gen bmi4cat=.
	replace bmi4cat=0 if (bmi1<30)
	replace bmi4cat=01 if (bmi1>=30)

	ir stroke bmi4cat timestrk, by(prevhyp1)
```

```stata
Prevalent hypert |      IRR       [95% Conf. Interval]   M-H Weight
-----------------+-------------------------------------------------
              No |   1.484769      .8687724   2.403521     11.75885 (exact)
             Yes |   1.121565      .8335983   1.493098     44.64521 (exact)
-----------------+-------------------------------------------------
           Crude |    1.79188      1.394785   2.280687              (exact)
    M-H combined |   1.197284       .939728    1.52543
-------------------------------------------------------------------
 Test of homogeneity (M-H)    chi2(1) =      0.99  Pr>chi2 = 0.3208
```


#### 3. Based on your results above, which option for reporting the association between obesity and stroke is best? ####
> **Hint1:** In option B you give as an answer the *adjusted measure of association for all*, only one number. In option C, the answer is two different numbers, one for each strata. 

* A. The crude incidence rate ratio for the association between obesity and stroke 
* B. The incidence rate ratio for the association between obesity and stroke adjusted for prevalent hypertension using the Mantel-Haenszel formula.
* C. The incidence rate ratio for the association between obesity and stroke stratified by prevalent hypertension (ie calculate two incidence rate ratios – one among those with prevalent hypertension and one among those without prevalent hypertension). 
* => **B or C**


