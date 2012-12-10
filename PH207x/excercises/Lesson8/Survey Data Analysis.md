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


> **Before analyzing, *svyset* your data!**

1. What is the design of my survey?
2. Am I using a finite population correction? At which stage of the design?
3. What are the survey weights used in the design?

### Simple Random Sampling (SRS) ###

> N=pop_size=500000  
> n=sample_size=1000  
> p=?

> q= 1000/500000  
> w= 50000/1000  
> f=1-n/N -> But Stata don't use it -> Look at fpc  
> fpc=final_pop_correction=n/N

	gen sample_size=1000  
	gen weight_srs=pop_size/sample_size  
	gen fpc=sample_size/pop_size  
	svyset id [pweight = weight_srs], fpc(fpc)

> Result:

     Parameter |  Value
-------------- | ------------
      pweight: | weight_srs
          VCE: | linearized
  Single unit: | missing
     Strata 1: | \<one\>
         SU 1: | id
        FPC 1: | fpc


	svy: proportion malaria

> Without fpc, the confidence interval is changing and the proportion of svy is the same

	svyset id [pweight = weight_srs]  
	svy: proportion malaria  
	proportion malaria

> So, please use fpc and use extract the design effect:  
> deff= var(your current design) / var(SRS infinite large population)

	svyset id [pweight = weight_srs], fpc(fpc)  
	svy: proportion malaria  
	estat effects, deff

	svy, sub(if province == 1): proportion malaria
	svy, sub(if province == 2): proportion malaria
	svy, sub(if province == 3): proportion malaria
	svy, sub(if province == 4): proportion malaria


### Stratified Sampling  ###

Province | Sample People
-------- | --------------
 1       | 250
 2       | 250
 3       | 250
 4       | 250
Total    | 1000

> strata=provinces  
> survey weights=?

#### What's the probability of a random individual, in say,province two being selected. ####
> For province two, it's just going to be 250 divided by the population's size of province two.

> sample_size=250  
> weight=sample_size/pop_size_of_province_2  
> fpc=final_pop_correction=n/N

	use "stratified_sampling.dta  
	gen sample_size=250  
	gen weight_stratified=pop_size/sample_size  
	gen fpc_stratified=1/weight_stratified  
	svyset id [pweight = weight_stratified], strata(province) fpc(fpc_stratified)

> Result:

     Parameter |  Value
-------------- | ------------
      pweight: | weight_stratified
          VCE: | linearized
  Single unit: | missing
     Strata 1: | province
         SU 1: | id
        FPC 1: | fpc_stratified


	svy: proportion malaria  
	estat effects, deff

> Check Oversize:

	svy: proportion malaria, over(province)
	table prov_size


### Cluster Sampling ###
> 2 Stage Design of a Cluster survey

Province | District |Sample People
-------- | -------- | --------------
 1       | 1        | 20
 1       | 2        | 10
 1       | 3        | 2
 1       | ..       | ..
 2       | ..       | ..
 3       | ..       | ..
 4       | ..       | ..
Total    | 2346     | 1000

> We are doing:  
> 25 districts by randomly sampling  
> 40 people/district by randomly sampling  
> fpc_I=25/146  
> fpc_II=40/people_in_district  
>  
> P(district 4 is sampled)= ?= fpc_I  
> P(Joe | disctrict 4 is sampled)= ?= fpc_II

	use "cluster_sampling.dta"
	gen fpc_I=25/146
	gen fpc_II=40/districtsize

	gen weight_cluster=(fpc_I*fpc_II)^-1
	svyset district [pweight=weight_cluster], fpc(fpc_I) || id, fpc(fpc_II)

	svy: proportion malaria
	estat effects, deff


### Stratified Cluster  ###

Province | District |Sample People
-------- | -------- | --------------
 1       | 1        | 20
 1       | 2        | 10
 1       | 3        | 2
 1       | 4        | ..
 1       | 5        | ..
 1       | ..       | ..
 2       | 1        | ..
 2       | 2        | ..
 2       | 3        | ..
 2       | 4        | ..
 2       | 5        | ..
 2       | ..       | ..
 3       | 1        | ..
 3       | 2        | ..
 3       | 3        | ..
 3       | 4        | ..
 3       | 5        | ..
 3       | ..       | ..
 4       | 1        | ..
 4       | 2        | ..
 4       | 3        | ..
 4       | 4        | ..
 4       | 5        | ..
 4       | ..       | ..
Total    | 2346     | 1000


	use "stratifiedcluster_sampling.dta"


> Example: Bob lives in district 2 of province 2  
> 5/ #district in P2 -> 50/#people in district 2  
> is equal to 5/fpc_I -> 50/fpc_II  
>  
> weights= (fpc_I * fpc_II)^-1  
> ndistrict= total number of districts

	gen fpc_I=5/ndistrict
	gen fpc_II=5/districtsize

	gen weight_stratcluster=(fpc_I*fpc_II)^-1
	svyset district [pweight=weight_stratcluster], fpc(fpc_I) strata(province)|| id, fpc(fpc_II)

	svy: proportion malaria
	estat effects, deff

## Other Aspects of Survey Design ##
> A survey weight for a given individual is the inverse of the probability that this person is included in the survey. Survey weights are therefore a function of the sample size and the size of the population from which you sample. Think about the sampling designs we discussed in class and the definition of a survey weight to answer the questions below.   
>   
> Suppose you have a population that can be divided into different subpopulations (strata/clusters). What auxiliary information is always required to calculate survey weights for the following types of designs:

#### A simple random sample? ####

* => **total population size**
* population size within strata 
* population size within clusters 
* none of the above 


#### Stratified random sample? ####

* total population size 
* => **population size within strata**
* population size within clusters 
* none of the above 

#### Cluster sample? ####

* total population size 
* population size within strata 
* => **population size within clusters**
* none of the above 

## Answer ##
> A survey weight for individual is the inverse probability that the individual is included in the sample. To calculate survey weights for a simple random sample, you need to know the total population size, because the weights are defined as the total number in the sample, divided by the total population size (though everyone in the sample has the same weight, so the weights don't actually impact your analysis). For a stratified sample, the weights are defined as the sample size per strata, divided by the population size in a strata. Therefore, you need to know the population size within strata. And for a cluster sample, you need to know the population size within each cluster. 


# Examining the Results of Stata Data Analysis #
> The results of each of the surveys are below. 

 Survey Designs     | ^p    | se(^p) | 95% CI        | DEFF 
------------------- | ----- | ------ | ------------- | ---- 
 Truth              | 0.131 |        |               |      
 SRS                | 0.128 | 0.0106 | (0.107,0.149) | 1
 Stratified         | 0.131 | 0.0120 | (0.107,0.155) | 1.28
 Cluster            | 0.144 | 0.0142 | (0.115,0.173) | 1.63
 Stratified Cluster | 0.155 | 0.0145 | (0.125,0.186) | 1.61

> Summary of our estimate of p from each of the survey designs.

* Examining these results, compare and contrast the survey designs again.
* Stratified sampling can be more efficient than simple random sampling. Looking at the design effects, we see that this is not the case for our survey design. Why?
* Relatedly, how might we design a stratified survey that is more efficient than the simple random sample?

## Answer Some thoughts (this is not a comprehensive answer) ##
> Recall that we designed our survey such that we sample the same number of people in each province. More efficient designs would exploit: 

1. the total population size in each strata, and 
2. the amount of variability in responses in each strata. 

> When there is more variability within strata, you should sample more people. Ideally, we would select strata that minimize the within-strata variability to gain efficiency over SRS. The cluster or stratified-cluster surveys might be easier to implement in practice. Looking at the design effect estimates (as well as the standard error of our estimate of malaria prevalence), it is clear that we do sacrifice some efficiency by using cluster sampling. 


# Tutorial: The Perils of Non-response #
> Calculate p with people who came back to the test

1. High responses - pA
2. Moderate responses - pB
3. Low responses - pC

> 'proportion highchol highcholC highcholB highcholA' is using only the data which are not missing. That is the reason why Number of obs is only 58.

	use "FraminghamNonresponseExample.dta"
	proportion highchol highcholC highcholB highcholA


	gen wA=1/pA
	proportion highcholA [pweight=wA]

	gen wB=1/pB
	proportion highcholB [pweight=wB]

	gen wC=1/pC
	proportion highcholC [pweight=wC]



