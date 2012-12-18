##  Stata Demo Module 9.2: Age-adjusted Incidence Rate ##
* Calculate the crude incidence rate ratio of CHD for smokers compared to nonsmokers in Stata
* Calculate the age-adjusted incidence rate ratio of CHD for smokers compared to nonsmokers in Stata

> Outcome like CHD we want to use incident rate ratios and incidence rates instead of risks or risk ratios. The issue with an outcome like CHD is that we might not have complete follow up for everyone. They may have dropped out of the study or suffered a competing risk before we could observe whether or not they developed CHD.  
> Because of this we're just going to use person-time. We have the amount of time that someone was followed for CHD, and we'll use the person-time and the number of CHD cases to calculate incidence rate ratios.

#### So now let's go to Stata and calculate the crude incidence rate ratio of CHD #####

```stata
	use "framingham_dataset.dta"
	ir anychd cursmoke1 timechd
```

```stata
                 | Current smoker, exam 1 |
                 |   Exposed   Unexposed  |      Total
-----------------+------------------------+------------
Incident Hosp MI |       617         623  |       1240
Time [years] to  |  39636.77    41288.39  |   80925.16
-----------------+------------------------+------------
                 |                        |
  Incidence rate |  .0155664     .015089  |   .0153228
                 |                        |
                 |      Point estimate    |    [95% Conf. Interval]
                 |------------------------+------------------------
 Inc. rate diff. |         .0004774       |   -.0012292     .002184 
 Inc. rate ratio |         1.031637       |    .9214548    1.154975 (exact)
 Attr. frac. ex. |         .0306665       |   -.0852404    .1341806 (exact)
 Attr. frac. pop |         .0152591       |
                 +-------------------------------------------------
                     (midp)   Pr(k>=617) =                   0.2917 (exact)
                     (midp) 2*Pr(k>=617) =                   0.5835 (exact)
```

> **The incidence rate ratio in this study is 1.03. That means that people who smoke have 1.03 times the rate of developing CHD compared to nonsmokers.**

### Age-adjusted incidence rate ratio of CHD ###

```stata
	gen age4cat=.
	replace age4cat=0 if (age1<=40)
	replace age4cat=1 if (age1>40 & age1 <=50)
	replace age4cat=2 if (age1>50 & age1 <=60)
	replace age4cat=3 if (age1>60 & age1 < .)

	ir anychd cursmoke1 timechd, by(age4cat)
```

```stata
         age4cat |      IRR       [95% Conf. Interval]   M-H Weight
-----------------+-------------------------------------------------
               0 |   1.270157      .8685574   1.879063      25.9039 (exact)
               1 |   1.340651      1.084671   1.662353     79.13065 (exact)
               2 |   1.280713      1.057269   1.549966     95.51036 (exact)
               3 |   1.205179      .9301212   1.552003     54.86073 (exact)
-----------------+-------------------------------------------------
           Crude |   1.031637      .9214548   1.154975              (exact)
    M-H combined |   1.281988      1.142602   1.438378
-------------------------------------------------------------------
 Test of homogeneity (M-H)    chi2(3) =      0.42  Pr>chi2 = 0.9362
```

> And this age-adjusted incidence rate ratio is right there, and it's 1.28. This means that after adjusting for age, people who are smokers have 1.28 times the rate of developing CHD compared to people who are nonsmokers. Now you can see that there's a pretty big difference in the incidence rate ratios between the crude incidence rate ratio which is 1.03, and the Mantel-Haenszel age adjusted rate ratio which is 1.28.  
> So this does support that there probably was some confounding by age. Because after we adjusted for age we're getting an effect estimate that is closer to the truth.




