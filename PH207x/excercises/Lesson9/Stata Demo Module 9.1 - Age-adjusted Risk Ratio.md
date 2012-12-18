## Stata Demo Module 9.1: Age-adjusted Risk Ratio  ##
* Calculate the crude risk ratio if death for smokers compared to nonsmokers in Stata
* Calculate the age-adjusted risk ratio of death for smokers compared to nonsmokers in Stata

```stata
	use "framingham_dataset.dta"
	cs death cursmoke1
```

```stata
                 | Current smoker, exam 1 |
                 |   Exposed   Unexposed  |      Total
-----------------+------------------------+------------
           Cases |       788         762  |       1550
        Noncases |      1393        1491  |       2884
-----------------+------------------------+------------
           Total |      2181        2253  |       4434
                 |                        |
            Risk |  .3613022    .3382157  |   .3495715
                 |                        |
                 |      Point estimate    |    [95% Conf. Interval]
                 |------------------------+------------------------
 Risk difference |         .0230864       |   -.0049864    .0511592 
      Risk ratio |          1.06826       |    .9858212    1.157592 
 Attr. frac. ex. |         .0638979       |   -.0143828    .1361376 
 Attr. frac. pop |         .0324849       |
                 +-------------------------------------------------
                               chi2(1) =     2.60  Pr>chi2 = 0.1070
```

```stata
	gen age4cat=.
	replace age4cat=0 if (age1<=40)
	replace age4cat=1 if (age1>40 & age1 <=50)
	replace age4cat=2 if (age1>50 & age1 <=60)
	replace age4cat=3 if (age1>60 & age1 < .)
```

```stata
	 cs death cursmoke1, by(age4cat)
```

```stata
         age4cat |       RR       [95% Conf. Interval]   M-H Weight
-----------------+-------------------------------------------------
               0 |    1.790619     1.158273   2.768188     14.98674 
               1 |    1.731975     1.418997   2.113985     64.09396 
               2 |    1.312757     1.165099   1.479129     128.2843 
               3 |    1.179281     1.078835   1.289079     98.49698 
-----------------+-------------------------------------------------
           Crude |     1.06826     .9858212   1.157592              
    M-H combined |    1.381036     1.279253   1.490917
-------------------------------------------------------------------
Test of homogeneity (M-H)      chi2(3) =   19.107  Pr>chi2 = 0.0003
```


