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
|        | Headache | No Headache | Total | Disease Odds | Disease Odds
------------------------------------------------------------
| Male   | 10       | 40          | 50    | 10/40= 0.25  | 40/10=4
| Females| 5        | 45          | 50    | 5/45= 0.11   | 45/5= 9

Odds Ratio= (10/40) / (5/45) = 2.25


