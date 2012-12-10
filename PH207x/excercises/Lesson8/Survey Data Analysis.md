## Sampling Methods ##
Several Sampling methods:

* Simple Random Sampling (SRS) 
* Stratified Sampling 
* Cluster Sampling 
* Stratified Cluster Sampling

### Design Effect ###
Design Effect (DEFF) is the ratio of the variance under the design used, to the variance with simple random sampling. e.g. DEFF=2 means you need twice as big a sample to get the same variance as you would get with a simple random sample.

## Tutorial: Survey Designs  ##
> Real-world, publicly available survey data is often very complex. Consequently, we will use "hypothetical" data for all of the tutorials in this week's tutorial sequence, estimating p, the prevalence of a disease, say malaria, in a hypothetical country, called Inventia.

Province | Population size | Number of districts
-------- | --------------- | --------------------
 1       | 225000          | 50
 2       | 150000          | 42
 3       | 100000          | 32
 4       |  25000          | 23
 Total   | 500000          | 146

> We know that p differs between different provinces, due to the different hypothetical climates in each area. p may also vary somewhat between districts, given different access to malaria prevention. For instance, urban populations may have more resources to prevent malaria, and thus a lower prevalence. The true prevalence of malaria in Inventia is 13.1%.  
>  
> In the following tutorial, we examine how to analyze data from several different survey designs: 

* Simple random sampling (SRS) - We randomly sample 1,000 people.
* Stratified Sampling - We randomly sample 250 people from each of the 4 provinces of Inventia.
* Cluster Sampling - We randomly sample 25 districts from Inventia and randomly sample 40 people within each district.
* Stratified Cluster sampling - Within each of the 4 provinces, we sample 5 districts and sample 50 people within each selected district.

> **Discuss the advantages and disadvantages of these survey designs, considering ease of implementation, c ost, feasibility, and precision of your estimate. Which design would you do in practice?**  
>  
> This is an open-ended question, without a definitive correct answer. Please discuss your answers below on the discussion boards.

#### Answer (Some thoughts (this is not a comprehensive list/answer!) ####
> Stratified sampling protects against obtaining a bad simple random sample (e.g. by chance, sample all males); and facilitates subgroup estimation (e.g. sample equal numbers from each province by design, so that you can compare estimates between provinces). Further, if your survey is well designed and you use auxillary information, stratified sampling is the most effcient survey design, beating out simple random sampling. However, to implement stratified sampling, we need auxilliary information to increase precision (variance within strata); and need to know the population-size within each stratum.  
>  
> Cluster sampling is typically more convenient (usually way easier to implement when doing large-scale surveys than SRS or stratified sampling). However, this convenience results in a loss of efficiency (need to sample more people to obtain same precision as an SRS). We also need auxillary information about population size within each cluster.

## Tutorial: Survey Data Analysis in Stata: Simple Random Sampling ##
> We aim to estimate p, the prevelance of malaria, in a hypothetical country, called "Inventia", with four provinces and multiple districts within provinces.

> **Surveys:**

* Simple Random Sampling (SRS) 
* Stratified Sampling 
* Cluster Sampling 
* Stratified Cluster Sampling

	 use "srs_sampling.dta"

> Before analyzing, *svyset* your data!

1. What is the design of my survey?
2. Am I using a finite population correction? At which stage of the design?
3. What are the survey weights used in the design?

> N=pop_size=500000  
> n=1000  
> p=?

> q= 1000/500000  
> w= 50000/1000

	gen weight_srs=pop_size/n
