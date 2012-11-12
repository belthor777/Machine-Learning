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
| Male   | 843  | 1101     | 1944   | 843/1944       | 843/1101= 0.765667574932
| Females| 707  | 1783     | 2490   | 707/2490       | 707/1783= 0.396522714526

Q1.) What is the 24 year Risk Ratio for dying comparing Males (exposed group) to Females (non-exposed group)?
Risk Ratio: RR= (843/194) / (707/2490)= 
di ( 843/194) / (707/2490) )
=> 

Q2.) What is the 24-year Risk Difference for dying, comparing Males (exposed group) to Females (non-exposed group)?
Risk Difference = 843/1944 - 707/2490=
di ( (843/1944) - (707/249) )
=>

Q3.) What is the 24-year Odds Ratio for dying, comparing Males (exposed group) to Females (non-exposed group)?
Odds Ratio= (843/1101) / (707/1783)
di ( (843/1101) / (707/1783) )
=>
