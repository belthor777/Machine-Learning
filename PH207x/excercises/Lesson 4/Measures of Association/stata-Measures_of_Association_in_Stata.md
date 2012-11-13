# Measures of Association in Stata 

Q1.) Examine the association between smoking status at visit 1 (cursmoke1) and death (death)

 * Risk Difference
 * Risk Ratio
 * Attributable Fraction Among the Exposed
 * Attributable Fraction Among the Total Population
 * Odds Ratio

=> cs death cursmoke1, or

                 | Current smoker, exam 1 |
                 |   Exposed   Unexposed  |      Total
-----------------+------------------------+------------
           Cases |       788         762  |       1550
        Noncases |      1393        1491  |       2884
-----------------+------------------------+------------
           Total |      2181        2253  |       4434
            Risk |  .3613022    .3382157  |   .3495715
                 |      Point estimate    |    [95% Conf. Interval]
                 |------------------------+------------------------
 Risk difference |         .0230864       |   -.0049864    .0511592 
      Risk ratio |          1.06826       |    .9858212    1.157592 
 Attr. frac. ex. |         .0638979       |   -.0143828    .1361376 
 Attr. frac. pop |         .0324849       |
      Odds ratio |         1.106873       |    .9783102    1.252331 (Cornfield)
                 +-------------------------------------------------
                               chi2(1) =     2.60  Pr>chi2 = 0.1070

## Calculate the association between smoking status at visit 1 (cursmoke1) and the rate of death (death).
=> ir death cursmoke1 timedth

                 | Current smoker, exam 1 |
                 |   Exposed   Unexposed  |      Total
-----------------+------------------------+------------
 Death indicator |       788         762  |       1550
Time [years] to  |  44440.38     46675.2  |   91115.58
-----------------+------------------------+------------
  Incidence rate |  .0177316    .0163256  |   .0170114
                 |      Point estimate    |    [95% Conf. Interval]
                 |------------------------+------------------------
 Inc. rate diff. |          .001406       |   -.0002899     .003102 
 Inc. rate ratio |         1.086125       |    .9819268    1.201432 (exact)
 Attr. frac. ex. |         .0792955       |   -.0184058    .1676598 (exact)
 Attr. frac. pop |         .0403128       |
                 +-------------------------------------------------
                     (midp)   Pr(k>=788) =                   0.0520 (exact)
                     (midp) 2*Pr(k>=788) =                   0.1040 (exact)

## Calculate the association between smoking status at visit 1 (cursmoke1) and the rate of CHD (anychd).
=> ir anychd cursmoke1 timechd

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

# Conclusions
## Severak measures of disease frequency
 * risks: assume no competing risk or loss to follow-up
 * rates: person-time data accounts for dynamic population
 * odds: case-control studies

## Several ways to describe association between exposure and outcome
 * difference measures
 * ratio measures
 * attributable fractions

## In this study, smoking is associated with
 * a higher risk, odds and rate of death compared to non-smokers
 * a higher rate of CHD compared to non-smokers


