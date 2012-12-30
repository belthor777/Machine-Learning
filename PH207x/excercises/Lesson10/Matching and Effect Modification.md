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
	* Old age itself influences the risk of having disease, so older people are going to be **more likely** to be your cases.
	*But remember, old age might also be related to whether you smoke or you don't smoke. And smoking brings with it higher risk of getting heart disease.

