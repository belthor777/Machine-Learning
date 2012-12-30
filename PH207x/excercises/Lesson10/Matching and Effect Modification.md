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

### DAG with Confounding ###
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
* **Sex distribution among exposed and among non-exposed subjects in the source population**  
  
         | Exposed     | Non-Exposed
-------- | ----------- | ------------
 Males   | 8,000 (80%) | 8,000 (80%)
 Females | 2,000 (20%) | 2,000 (20%)
 Total   | 10,000      | 10,000

* **Exposure and sex-specific risks of outcome**  
  
         | Exposed | Non-Exposed
-------- | ------- | ------------
 Males   | 0.06    | 0.02
 Females | 0.03    | 0.01

Now, remember a confounder has to have two relationships:
1. It has to be in balance in the two groups you're comparing.
2. But it also has to be an independent risk factor or at least a marker or a determinant of developing the disease.

> So right now from these two characteristics, characteristic A and characteristic B on this slide, we can say that this particular factor of sex should be a confounder. It's satisfying the two criteria that confounder has to have.
