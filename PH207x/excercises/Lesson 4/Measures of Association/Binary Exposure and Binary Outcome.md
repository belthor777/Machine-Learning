# Binary Exposure and Binary Outcome
| Exposure | Outcome + | Outcome - | Total | Estimated Risk
-----------------------------------------------------------
| E+       | A         | B         | N_1   | A/N_1
| E-       | C         | D         | N_0   | C/N_0

## Example with Smokers (SMK)
| Exposure  | Outcome + | Outcome -   | Total | Estimated Risk
|           | e.g. Death| e.g. Survive|       | 
------------------------------------------------------------
| E+ (SMK)  | A         | B         | N_1   | A/N_1
| E- (N-SMK)| C         | D         | N_0   | C/N_0

## Common Measures of Association
Risk Ratio: RR=R_1/R_0
Risk Difference (Attributable Risk): RD= R_1-R_0
Disease Odds Ratio: OR= (R_1/(1-R_1)) / (R_0/(1-R_0))
Odds= Risk/(1-Risk)

## Example Cumulative Incidence Data
|        | Headache | No Headache | Total | Estimated Risk
------------------------------------------------------------
| Male   | 10       | 40          | 50    | 10/50= .20
| Females| 5        | 45          | 50    | 5/50= .10

Risk Ratio: RR= (10/50) / (5/50)= .20/.10= 2.0
Risk Difference = .20 - .10= .10

## Example Incidence Rate Data
|        | Headache | Person-Days of Follow-up | Incidence Rate
------------------------------------------------------------
| Male   | 10       | 302                      | 10/302pd
| Females| 5        | 343                      | 5/343pd

Risk Ratio: RR= (10/302pd) / (5/343pd)= .20/.10= 2.27
Risk Difference = (10/302pd) - (5/343pd)= 1.85/100pd

# Odds
## Example Odds - Cumulative Incidence Data
|        | Headache | No Headache | Total | Disease Odds | Non-Disease Odds
------------------------------------------------------------
| Male   | 10       | 40          | 50    | 10/40= 0.25  | 40/10=4
| Females| 5        | 45          | 50    | 5/45= 0.11   | 45/5= 9

Odds Ratio= (10/40) / (5/45) = 2.25
Odds Ratio_2 for not developing outcome= 1/(Odds Ratio for developing outcome)
Odds Ratio_2= (40/10)/(45/5)= .4444= 1/2.25

## Illness Odds Ratio= Exposure Odds Ratio
|        | Headache | No Headache | Disease Odds
------------------------------------------------------------
| Male   | 10       | 40          | 10/40= 0.25
| Females| 5        | 45          | 5/45= 0.11
| Exposure Odds | 10/5 | 40/45 | EOR= (12/5) / (40/45)

=> For small risks OR ~ RR

# Measures of Association Problem 1 
|        | Died | Survived | Total  | Estimated Risk | Disease Odds
------------------------------------------------------------
| Male   | 843  | 1101     | 1944   | 843/1944=0.43364198  | 843/1101= 0.765667574932
| Females| 707  | 1783     | 2490   | 707/2490=0.28393574  | 707/1783= 0.396522714526

Q1.) What is the 24 year Risk Ratio for dying comparing Males (exposed group) to Females (non-exposed group)?
Risk Ratio: RR= 0.43364198 / 0.28393574= 1.5272539
di ( 0.43364198 / 0.28393574 )
=> 

Q2.) What is the 24-year Risk Difference for dying, comparing Males (exposed group) to Females (non-exposed group)?
Risk Difference = 0.43364198 - 0.28393574= 0.14970624

Q3.) What is the 24-year Odds Ratio for dying, comparing Males (exposed group) to Females (non-exposed group)?
Odds Ratio= (843/1101) / (707/1783)
di ( (843/1101) / (707/1783) )
=> 1.930955143


# Measures of Association Problem 2 
|        | Died | Person-Years of Follow-up | Incidence Rate
------------------------------------------------------------
| Male   | 843  | 38,287.33 | 842/38,287.33= 0.02199161
| Females| 707  | 52,828.15 | 707/52,828.15= 0.01338302

Rate Ratio: RR= 0.02199161 / 0.01338302= 1.6432472
Risk Difference = 0.02199161 - 0.01338302= 0.00860859

Q1.) What is the 24-year Rate Ratio for dying, comparing Males (exposed group) to Females (non-exposed group)?
Rate Ratio: RR= 0.02199161 / 0.01338302= 1.6432472

Q2.) What is the 24-year Rate Difference for dying, comparing Males (exposed group) to Females (non-exposed group)? Please express your answer in units of 100 person-years. 
Risk Difference = 100*(0.02199161 - 0.01338302)= 0.00860859*100= 0.860859

# Measures of Association AP%
## Attributable Proportion Among Exposed Subjects

 * Attributable Risk Percent Among Exposed Subjects
 * Attributable Fraction Among Exposed Subjects (Stata) - What they're asking is how much of a person's risk, if a smoker, is due to the fact that they smoke?
 * Proportion of Exposed Subject's Risk that is "attributed" to the Exposure

					R_Exposed (total risk)
R_Exposed-R_Non-Exposed (risk difference)	R_Non-Exposed (Baseline Risk)

AP%= (RR-1)/RR

## Attributable Proportion Among Total Population
AP%_Population= p(RR-1)/(1+p(RR-1))


## 24-Year Risk of Death Among Smokers and Non-Smokers
|             | Died | Survived | Total  | Estimated Risk
---------------------------------------------------------
| Smokers     | 788  | 1393     | 2181   | 788/2181=0.36 
| Non-Smokers | 762  | 1491     | 2253   | 762/2253=0.34
| Total       | 1550 | 2884     | 4434   | 1550/4434= 0.35

-> Attributable Proportion Among Exposed Subjects
Risk Ratio: RR= 0.36 / 0.34= 1.07
AP%_Exposed= (1.07-1)/1.07= 0.065

-> Attributable Proportion Among Total Population
p= prevelance of exposure in population= P(Smokers)= 2181/4434= 0.49
AP%_Population= 0.49*(1.07-1) / (1+0.49*(1.07-1))= 0.033

We come up with an answer of 0.033%. Meaning of the 3% between 3% and 4% of the average risk of dying in the entire population can be attributed to the fact that roughly half the people in the population were smoking.


# Measures of Association NNT
## Example: Rosuvastatin to Prevent Mortality in Subjects with Elevated C-Reactive Protein
| Treatment   | Deaths | Number of Subjects | Estimated Risk
---------------------------------------------------------
| Rosuvastatin| 198    | 8901               | 0.0222
| Placebo     | 247    | 8901               | 0.0277

Q1.) Suppose 10000 subjects were treated with Rosuvastatin:
Expected Number of Deaths= 10000*0.0222= 222

Q2.) Suppose 10000 subjects were treated with Placebo:
Expected Number of Deaths= 10000*0.0277= 277

=> Implications: 277-222= 55 deaths prevent for every 10000 treated subjects
=> Death prevented for every 181.8 (10000/55) treated subjects

## Number Needed to Treat (NNT)
NNT= Number of subjects needed to treat to prevent 1 outcome

Example: 181.8 treated with Rosuvastatin would prevent 1 deaths
181.8	= 1/(Risk_Placebo - Risk_Treatment)= 1/(Risk_Difference)
	= 1/(0.0277-0.0222)= 1/(55/10000)= 181.8


# Measures of Association Reg Coeff 
What is probably the most commonly used measure of association to link a risk
factor to an outcome.

## 24-Year Risk of Death by Packs of Cigarettes Smoked (FHS)
| Packs1    | Died | Survived | Total  | Estimated Risk
----------------------------------------------------
| 0         | 762  | 1491     | 2253   | 762/2253= 0.34
| 1 ( 1-20) | 573  | 1098     | 1671   | 573/1671= 0.34
| 2 (21-40) | 169  |  229     |  398   | 169/298= 0.43
| 3 (>40)   |  36  |   44     |   80   | 36/80= .45

### Regression Model Equation:
Risk= B_0 + B_1(#Packs1)

### Slope (B_1): Estimate of the Effect of Smoking
B_1= (delta in Risk)/(Smoking 1 additional pack)

## 24-Year Risk of Death by Packs of Cigarettes Smoked (FHS)
| Packs1    | Died | Survived | Total  | Log(Odds) or (Logit)
----------------------------------------------------
| 0         | 762  | 1491     | 2253   | Log(762/1491)= -0.67
| 1 ( 1-20) | 573  | 1098     | 1671   | Log(573/1098)= -0.65
| 2 (21-40) | 169  |  229     |  398   | Log(169/229)= -0.30
| 3 (>40)   |  36  |   44     |   80   | Log(36/44)= -0.20

Log(Odds)= ln(Odds)= natural log of the Odds of Death

### Regression Model Equation:
Log(Odds)= B_0 + B_1(#Packs1)

### Slope (B_1): Estimate of the Effect of Smoking
B_1= (delta in Log(Odds))/(Smoking 1 additional pack)= log( Odds Ratio )

## Implications
 * Regression coefficients = slopes
 * Measures of Association
 * Regression coefficient from logistic regression model is a log(Odds Ratio)


