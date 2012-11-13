# Incidence Rate Ratio Blood Pressure and CHD
The following table uses data from the NHLBI teaching data set and displays the blood pressure distribution for 4,434 participants in the Framingham Heart Study attending an examination in 1956.

For each blood pressure category, the table displays the number of subjects with existing Coronary Heart Disease (CHD) at that exam (Prevalent Cases of CHD). It also shows, for those subjects who did not have CHD at the 1956 exam, the number of new cases of CHD during a 24 year follow-up period and the total amount of person-years of follow-up. Follow-up for each subject began in 1956 and ended with the development CHD (fatal or non-fatal), death from another cause, loss to follow-up, or the end of the follow-up period (whichever came first).

## Blood Pressure and CHD
>  Group         | Blood Pressure Category    | # of subjects | Prevalent cases of CHD | # developing CHD during follow-up | Total Years of follow-up
>  ------------- | -------------------------- | ------------- | ---------------------- | --------------------------------- | -------------------------
>  I             | SBP<140 and DBP<9          | 2815          | 88                     | 547                               | 55384.42
>  II            | 140<=SBP<160 or 90<=DBP<95 | 781           | 39                     | 214                               | 13191.79
>  III           | 160<=SBP or 95<=DBP        | 838           | 67                     | 285                               | 12348.94

##### Q1. What is the Incidence Rate Ratio for developing CHD for participants in Blood Pressure Groups II or III combined (exposed group) compared to participants in the Blood Pressure Group I (non-exposed group)? #####

=> Rate Ratio= 1.9781878281

>  Group         | Incidence Rate
>  ------------- | -------------
>  II or III     | (214+285)/(12348.94+13191.79)= 0.0195374212
>  I             | 547/55384.42=0.00987642

Rate Ratio: RR=  0.0195374212 / 0.00987642


##### Q2. What is the Incidence Rate Ratio for developing CHD for participants in Blood Pressure Group III (exposed group) compared to participants in the Blood Pressure Group I (non-exposed group)? #####

Incidence Rate Ratio= ?

| Group | Incidence Rate
| III   | 285/12348.94=0.0230789
| I     | 547/55384.42=0.00987642
Rate Ratio: RR= 0.0230789 / 0.00987642= 2.3367678


Q3.) What is the Incidence Rate Ratio for developing CHD for participants in Blood Pressure Group II (exposed group) compared to participants in the Blood Pressure Group I (non-exposed group)?
Incidence Rate Ratio= ?

| Group | Incidence Rate
| II    | 214/13191.79=0.01622221
| I     | 547/55384.42=0.00987642
Rate Ratio: RR= 0.01622221 / 0.00987642= 1.6425193
