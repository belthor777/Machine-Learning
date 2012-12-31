# Matching and Effect Modification #

## Matching - Intro ##

### Restriction ###
* **Matching** restricts selection of some subjects to obtain a specified distribution of the matching factor
* **Observational studies** (e.g. cohort studies): Typically restricts selection of the comparison group
	* **Cohort Study**: Non-exposed subjects selected to have similar distribution of as exposed subjects
	* **Case Control Study**: Controls selected to have similar distribution of as cases

### Motivation for Matching: Avoid Confounding ###
* **Matching alone avoids confounding in cohort studies (probided there is a fixed matching ratio)**
* Matching alone does not necessarily avoid confounding in case-control studies
	* Still requires adjustment for the matching factor in the analysis

### DAG with Confounding - Causal Diagram ###
1. **Confounder -> Exposure**: Target of Matching in Cohort Studies  
-> So what matching does in a cohort study, it addresses the relationship
between the potential confounder.
2. **Confounder -> Outcome**: Target of Matching in Case Control Studies
	* And I said in a cohort study, matching blocks that relationship.
	* And it also has been independent risk factor for the outcome.
3. **Exposure -> Outcome**:

#### Why I want to have old people in my study? ####
The problem is there are two reasons, as I look at my cases and select their match controls matching by age, there are **two reasons I might see a lot of old people among my cases**. The two reasons are, 
* that if age is my potential confounder, and CHD-- coronary heart disease-- is my outcome, there are two potential mechanisms by which old people could end up being cases in your study.
	1. Old age itself influences the risk of having disease, so older people are going to be **more likely** to be your cases.
	2. But remember, old age might also be related to whether you smoke or you don't smoke. And smoking brings with it higher risk of getting heart disease.

### Summary: Case Control Studies ###
* Matching on a confounder in a case control study:
	- Builds **similar distributions** of confounder among the cases and controls
	- Builds similar distributions of any correlate of the confounder (e.g. exposure) among the cases and controls
* Implication: Biases crude **odds ratio** towards its null value (1.0)

## How to Perform Matching: Question##
When performing matching in a case-control study:
* => **Controls are selected to have a similar distribution of the matching factors as the cases.**
* Non-exposed subjects are selected to have similar distribution of the matching factors as exposed subjects. 
* Cases are selected to represent the exposure distribution in the general population.
* Controls are selected to have a similar distribution of the exposure as the cases. 

## Example of Matching ##

### Example of confounding by sex in a large population ###
* **A. Sex distribution among exposed and among non-exposed subjects in the source population**  
  
         | Exposed     | Non-Exposed
-------- | ----------- | ------------
 Males   | 8,000 (80%) | 8,000 (80%)
 Females | 2,000 (20%) | 2,000 (20%)
 Total   | 10,000      | 10,000

* **B. Exposure and sex-specific risks of outcome**  
  
         | Exposed | Non-Exposed
-------- | ------- | ------------
 Males   | 0.06    | 0.02
 Females | 0.03    | 0.01

* **C. Expected number of outcomes**  
  
         | Exposed | Non-Exposed  | Total
-------- | ------- | ------------ | ------ 
 Males   | 480     | 40           | 
 Females | 60      | 80           | 
 Total   | 540     | 120          | 660 Controls 

Now, remember a confounder has to have two relationships:
1. It has to be in balance in the two groups you're comparing.
2. But it also has to be an independent risk factor or at least a marker or a determinant of developing the disease.
  
> So right now from these two characteristics, characteristic **A** and characteristic **B** on this slide, we can say that this particular factor of sex **should be a confounder**. It's satisfying the two criteria that confounder has to have.
  
> **The risk changes from 2% to 6%**. So what's the right answer for the effect of the exposure? The risk ratio here is **3.0**. Regardless whether you're male or female, the exposure triples your risk.
  
##### DAG with Sex - Causal Diagram #####

1. **Sex -> Exposure**: ***80%***
2. **Sex -> Disease**: ***Risk Ratio= 2%***
3. **Exposure -> Disease**:


* **D. Expected sex-specific data**  
  
             | Males Outcome |       | *Total*   | Females Outcome |       | *Total* 
------------ | ------------- | ----- | --------- | --------------- | ----- | --------- 
             | **+**         | **-** |           | **+**           | **-** | 
 Exposed     | 480           | 7520  | 8000      | 60              | 1940  | 2000      
 Non-Exposed | 40            | 1960  | 2000      | 80              | 7920  | 8000      
 Risk Ratio  |               |       | 3.0       |                 |       | 3.0       

#### Conclusion ####
* Sex appears to be a confounder
	- Associated with the exposure in the source population
	- Independent determinant of the outcome
* RR_Crude=4.5 != RR_Adjusted=3.0


### Example Matched (by sex) cohort study ###
**Matched (by sex) cohort study** based on 1000 exposed subjects selected at random from the source population
* **A. Sex distribution among exposed and among matched non-exposed subjects**  
  
         | Exposed   | Non-Exposed
-------- | --------- | ------------
 Males   | 800 (80%) | 800 (80%)
 Females | 200 (20%) | 200 (20%)
 Total   | 1000      | 1000

* **B. Exposure and sex-specific risks of outcome**  
  
         | Exposed | Non-Exposed
-------- | ------- | ------------
 Males   | 0.06    | 0.02
 Females | 0.03    | 0.01

* **C. Expected number of outcomes**  
  
         | Exposed | Non-Exposed  | Total
-------- | ------- | ------------ | ------ 
 Males   | 48      | 16           | 
 Females | 6       | 2            | 
 Total   | 54      | 18           | 72 

* **D. Expected sex-specific data**  
  
             | Males Outcome |       | *Total*   | Females Outcome |       | *Total* 
------------ | ------------- | ----- | --------- | --------------- | ----- | --------- 
             | **+**         | **-** |           | **+**           | **-** | 
 Exposed     | 48            | 752   | 800       | 6               | 194   | 200      
 Non-Exposed | 16            | 784   | 800       | 2               | 198   | 200      
 Risk Ratio  |               |       | 3.0       |                 |       | 3.0      

* **E. Expected crude data**  
  
             | Outcome       |       | *Total*  
------------ | ------------- | ----- | --------- 
             | **+**         | **-** |           
 Exposed     | 54            | 946   | 1000 
 Non-Exposed | 18            | 982   | 1000 
 Risk Ratio  |               |       | 3.0 


#### Conclusion for cohort study ####
* I no longer have a relationship in my data set between sex and exposure (between sex and smoking). Therefore, **sex should not be a confounder**.
* RR_Crude=RR_Adjusted=3.0
* Matching on Sex avoids confounding


### Example Matched (by sex) case control study ###
**Matched (by sex) cohort study** based on all 660 outcome cases that developed from the source population
* **A. Sex distribution among exposed and among matched controls**  
  
         | Cases     | Control
-------- | --------- | ------------
 Males   | 520 (79%) | 520 (79%)
 Females | 140 (21%) | 140 (21%)
 Total   | 660       | 660

* **B. Exposure and sex-specific risks of outcome**  
	- **Cases (Panel C for source population):**  
  
         | Exposed   | Non-Exposed  | Total
-------- | --------- | ------------ | ------
 Males   | 480 (92%) | 40 (8%)      | 520 
 Females | 60 (43%)  | 80 (57%)     | 140 
 Total   | 540 (82%) | 120 (18%)    | 660 

	- **Control (Panel A for source population):**  
  
         | Exposed   | Non-Exposed  | Total
-------- | --------- | ------------ | ------
 Males   | 416 (80%) | 104 (20%)    | 520 
 Females | 28 (20%)  | 112 (80%)    | 140 
 Total   | 444 (67%) | 216 (33%)    | 660 

* **C. Expected sex-specific data**  
  
             | Males Exposure |       | *Total*   | Females Exposure |       | *Total* 
------------ | -------------- | ----- | --------- | ---------------- | ----- | --------- 
             | **+**          | **-** |           | **+**            | **-** | 
 Exposed     | 480            | 40    | 520       | 60               | 80    | 140 
 Non-Exposed | 416            | 104   | 520       | 28               | 112   | 140 
 Odd Ratio   |                |       | 3.0       |                  |       | 3.0 

* **D. Expected crude data**  
  
             | Outcome       |       | *Total*  
------------ | ------------- | ----- | --------- 
             | **+**         | **-** |           
 Exposed     | 540           | 120   | 660 
 Non-Exposed | 444           | 216   | 660 
 Odd Ratio   |               |       | 2.2 

Odd Ratio is less than 3.0. It's under estimating the true effect. That's the implications of matching in this case by sex which is a strong correlate of your exposure.

#### Conclusion ####
* Matching by sex alone did not avoid confounding
* **Adjusted analysis is still required**
* Problem: two reasons for high prevalence of male sex among cases
	- Sex is a risk factor
	- Exposure a risk factor and sex associated with exposure


## Matching - Efficiency ##
In the last lecture I try to make a distinction of the implications of **matching in a cohort study versus matching a case control study**. I said the good news is, matching in a cohort study with equal numbers of non-exposed being matched to each exposed person **avoids confounding**.

#####Q: Why would people want to do a match design when you're doing a case control study?#####
* Because either way you have to control for the factor. If it's a true confounder and you didn't match on it, you're going to have to control for it the analysis.
* You get a more efficient analysis. You have more power for when you do your tests of significance, or your confidence intervals will be now narrower when you report your confidence intervals around your odds ratios.

### Matching and Efficiency in Case Control Study ###
* Not machting on a confounder -> **varying case/control ratios across strata**
* Matching on a confounder -> **constant case/control ratios across strata**
* **Matched analysis tends to be more efficient than *stratified analysis* of unmatched data**

And I'm going to measure **odds ratios** in each of these tables, and use **Mantel-Haenszel's formula** to get the adjusted value, because I'm assuming **age is a confounder**.

## Results of Matching - Question ##
Matching in a case-control study:
* => **A. Results in narrower confidence intervals than would have been obtained if one did not conduct a matched study.**
* B. Provides an unbiased estimate of the association even without accounting for the matching in the analysis. 
* C. Limits the potential for recall bias. 
* D. Choices A and B

## Matching - Analysis ##
Video: https://s3.amazonaws.com/edx-course-videos/harvard-ph270x/H-PH207X-FA12-L10-11_001.mp4  
  
Basic prinziple: Perform analysis within each matched group and then pool to obtain a summary average  
  
Typical format for results from a case control study involving
* 1-1 matching on a single factor.  
  
                | Exposure  + | Status of Control - 
--------------- | ----------- | -------------------- 
 Exposure       | + A         | **B** 
 Status of Case | **- C**     | D 

The information about whether exposure is related to being a case, being a control, is really limited to the matched groups where the case and the control are called **discordant with** respect to exposure. (-C AND B)  
-> So for example, capital **B** were the number of matched groups where the case was a smoker and the control was not, and capital **C** were the number of matched groups where the control was a smoker and the case was not. The relative sizes of B and D are going to tell you whether smokers are more likely to be cases than to be controls.

### Odds Ratio Estimation ###
And in biostatistics, you learn that the way you estimate an odds ratio linking ***exposure to disease*** from case control studies that are matched of the form we were just looking at is you divide the number of matched groups where the ***case is a smoker and the control is not***, capital B. You ***divide*** that ***by capital C***, the number of matched groups where the ***control was a smoker and the case was not***. That ratio estimates the odds ratio for developing -- for being a case of disease comparing smokers to nonsmokers.

```math
	OR=B/C
```
> Identical to the Mantel-Haenszel estimate for the odds ratio with each matched pair as a separate stratum

#### Example: Predictors of Low Birth Weight Babies ####
* Case Control Study
* **56 cases** (infants born with low birth weight)
* **56 controls** matched by **age of the mother**
* **Exposure: Maternal smoking during pregnancy**

##### Matched Analysis #####
  
                | Exposure  + | Status of Control - 
--------------- | ----------- | -------------------- 
 Exposure       | + 8         | **22** 
 Status of Case | **- 8**     | 18 

```math
	OR=22/8=2.75
```

##### Stratified Analysis #####
We need **8** ***two by two tables***  
  
###### Now, remember what Mantel-Haenszel's formula does: ######
**It says, for an odds ratio, take the value, A, and multiply it by the value, D, and divide it by the grand number, T. That goes into the formula in the numerator of the Mantel-Haenszel estimate.**  
  
                | Exposure  + | Status of Control - 
--------------- | ----------- | -------------------- 
 Exposure       | + A         | **B** 
 Status of Case | **- C**     | D 

**Well, in the first case of the following table:**
* A is 1, 
* D is 0
* T is 2
* ***So it's going to be A*D/T=1*(0)/2***
  
           | Strata D+ | Strata D- | Frequency | AD/T    | BC/T    | SUM AD/T   | SUM BC/T 
---------- | --------- | --------- | --------- | ------- | ------- | ---------- | -------- 
 E+        | 1         | 1         | 8         | 0       | 0       | 8*0        | 8*0 
 E-        | 0         | 0         |           |         |         |            |    
           |           |           |           |         |         |            |    
 E+        | 1         | 0         | 22        | 1/2     | 0       | 22*1/2     | 22*0 
 E-        | 0         | 1         |           |         |         |            |    
           |           |           |           |         |         |            |    
 E+        | 0         | 1         | 8         | 0       | 1/2     | 8*0        | 8*1/2 
 E-        | 1         | 0         |           |         |         |            |    
           |           |           |           |         |         |            |    
 E+        | 0         | 0         | 18        | 0       | 0       | 18*0       | 18*0 
 E-        | 1         | 1         |           |         |         |            |    
           |           |           |           |         |         |            |    
 **Total** |           |           |           | **1/2** | **1/2** | **22*1/2** |**8*1/2** 

```math
	OR=(SUM AD/T) / (SUM BC/T)= 22(1/2)/8(1/2)=2.75
```

### Conclusion ###
So the important piece to keep in mind is that if you have **matching in a case control study**, once you come to the analysis stage, **you still have to control for the matching factor as if it's still a confounder**. In this case, if you control using stratified analysis, you'll get the same answer you're learning using the formulas in biostatistics for doing matched analysis.

## Effect Modification Example  ##
Video 1: https://s3.amazonaws.com/edx-course-videos/harvard-ph270x/H-PH207X-FA12-L10-12_100.mp4  
Video 2: https://s3.amazonaws.com/edx-course-videos/harvard-ph270x/H-PH207X-FA12-L10-13_100.mp4
  
**Confounding vs. Effect modification**: These are entirely different concepts of epidemiology. But they're often confused because they both **typically involve stratified analysis**. But they use **stratified analyses in different ways** to answer entirely different questions.

### Effect Modification ###
* Refers to an **exposure** having a **different** effect on the **outcome** in different groups of patients
	- Example: Personlized medicine
* Detected by comparing stratum-specific estimates of the measure of effect (**sub-group analyses**)

Effect modification means they are different: The effect of a drug, the effect of a treatment, the effect of an exposure is modified by the group of people you are looking at-- in that case, by the age of the people.  
  
This is what I mean by effect modification, the value that we're giving to describe the effect of an exposure-- in in this case, the effect of a treatment, beta blocking-- differs. It depends on what type of person you are. In this case, in terms of a person's risk of having a cardiac complication.

* **Effect Modifier**: Factor whose levels show different effect of the exposure on the outcome
* Conclusion about Effect Modification is dependent on the chosen measure of effect (**Effect Measure Modification**)


  




