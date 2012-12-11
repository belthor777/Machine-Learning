# Survey Design #
> You decide to conduct a survey to measure physical activity in Boston. You plan to collect information on the amount of physical activity per week, history of diabetes, weight, height, age, and gender.  
>  
> There are seventeen distinct neighborhoods in Boston, with substantial differences in race/ethnicity, socioeconomic status, and population density. You expect to observe variability in physical activity indicators by neighborhood. Unfortunately there is no specific information about within-neighborhood heterogeneity (variance); therefore, you design the survey based on the assumption that variances of indicators are equal across neighborhoods.  
>  
>The table below displays population data for Boston in 2010. Assume that these population numbers are still accurate today.

	Neighborhood            | Population - 2010
	----------------------- | ------------------
	 South End              | 34669
	 Central                | 30901
	 Fenway - Kenmore       | 40898
	 South Boston           | 33688
	 Charlestown            | 16439
	 Allston - Brighton     | 74997
	 West Roxbury           | 30445
	 Roxbury                | 59790
	 East Boston            | 40508
	 Jamaica Plain          | 39897
	 Back Bay - Beacon Hill | 27476
	 Hyde Park              | 31813
	 North Dorchester       | 28384
	 South Dorchester       | 59949
	 Roslindale             | 32589
	 Mattapan               | 34616
	 Harbor Islands         | 535
	 Boston                 | 617594

> *Source: Boston Redevelopment Authority Research Division (2011). Boston 2010 Census Population: Planning District Comparison: http://www.bostonredevelopmentauthority.org/PDF/ResearchPublications//PDPercentChange.pdf*

> Data which we need:
* seventeen distinct neighborhoods


#### 1. Consider the following questions ####
> Suppose you decided to randomly sample 1,700 people from the city of Boston (call this Design 1). For any given individual in South Dorchester, what is the probability of being selected in the survey? What is this probability for an individual in Harbor Islands?  
> **Hint1:** How could be the probability of Harbor Island be equal to the one of South Rochester ? (groups of selection were previously specified)  
> **Hint2:** It should work f=n/N for: q1 (sample size 1700)  
> **Hint3:** If you have a sample size(n), and a population size in Boston(N), and you now the formula that n/N, they have equal chances to be selected

> **Design 1:**

	gen weight_srs=617594/1700  
	gen fpc=1700/617594  
	di fpc

> => *fpc= 0.00275262*

* South Dorchester: **0.00275262**
* Harbor Islands: **0.00275262**


#### 2. What is likely the main challenge of conducting this survey? ####
> **Hint1:** This document helps: Advantages and disadvantages of simple random sampling: http://dissertation.laerd.com/simple-random-sampling.php#ad-dis

* SRS is difficult to implement in practice 
* SRS does not necessarily sample people from each neighborhood 

#### 3. Now, you randomly sample 100 people within each neighborhood (Design 2). What is the probability of a random individual in South Dorchester being sampled? What is the probability of a randomly selected individual in Harbor Islands being sampled? ####
> **Hint1:** It should work f=n/N for: q3 (sample size 100)

> **Design 2:**

	gen fpc_south_dorchester=100/59949  
	gen fpc_harbor_islands=100/535  

> => *fpc_south_dorchester= 0.00166808*  
> => *fpc_harbor_islands= 0.18691589*  

* South Dorchester: **0.00166808**   
* Harbor Islands: **0.18691589**

#### 4. What kind of survey design is Design 2? ####
* stratified sample 
* cluster sample 
* simple random sample 

#### 5. Consider an alternate design (Design 3). In each neighborhood the number of individuals sampled is proportional to the population size of the neighborhood. Assuming that the sample size is fixed at 1,700, would you expect Design 2 or Design 3 to provide more precise estimates of the physical activity indicators among Boston residents? ####
> **Hint1:** You just need to think about the two designs. One is a sample where you randomly select 100 people from every neighbourhood. The other is a sample where the number selected is proportional to the size of the neighbourhood. So areas with a small population with have less people selected than a region with a large population.

* Design 2
* Design 3

#### 6. For Design 3, consider the probability of a random individual in South Dorchester being sampled; and the probability of a random individual in Harbor Islands being sampled. These probabilities are approximately the same as the probabilities calculated using: ####

* Design 1
* Design 2

#### 7. Why might you want to use Design 2 compared to Design 3? ####

* to increase precision 
* if you wanted neighborhood-specific estimates 
* for both precision and neighborhood specific estimates 

#### 8. Next, you decide you do not want to visit all 17 neighborhoods, so you randomly sample 10 neighborhoods. Within each sampled neighborhood selected, you randomly sample 170 people. Call this Design 4. What is the probability of a random individual in South Dorchester being included in the survey? What is the probability of a random individual in Harbor Islands being included in the survey? ####
> **Hint1:** Watch 7th video of Survey Data Analysis: Tutorial Survey data Analysis in STATA(continued)- first 5 minutes  
> **Hint2:** My suggestion is: make a table in excel with the data and do calculations over there is pretty straightforward to answer q8, q9 and q10
> **Hint3:** It should work f=n/N for: q8 you randomly sample 10 neighborhoods out of 17 and multiply that by n/N (sample size 170)
> **Hint4:** If you were a person in district x. What is the probability of your district being chosen. Then go on from there. 

> **See my calc file for the solution of question 8**

* South Dorchester: **0.0016680845**
* Harbor Islands: **0.1869158879**

#### 9. A "self-weighting" design is a survey design for which every individual in the population has an equal probability of inclusion. Which survey designs are self-weighting (or approximately self-weighting)? ####

* Designs 1 and 2 
* => **Designs 1 and 3** - 1 ist constant as well as 2 and 4 are variable 
* Designs 2 and 3 
* Designs 1 and 4 
* Designs 2 and 4 

#### 10. Consider yet another design (Design 5), in which you again select 10 neighborhoods. Now, the probability of a neighborhood being included in the survey is proportional to its population size. Within each sampled neighborhood, you randomly sample 170 people. Would you expect Design 4 or Design 5 to provide more precise estimates of the physical activity indicators among Boston residents? ####
> **Hint1:** In Design 4, you randomly choose 10 districts out of 17, this means that all districts have the same probability of being chosen regardless of the size of their population. Design 5 is another story, the sampling of the districts is proportional to the size of their population, which means bigger districts are more likely to get chosen. 

* Design 4
* Design 5 


