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
2. **Confounder -> Outcome**: Target of Matching in Case Control Studies
3. **Exposure -> Outcome**:
