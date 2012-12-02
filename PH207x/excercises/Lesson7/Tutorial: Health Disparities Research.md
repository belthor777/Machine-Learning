# Tutorial: Health Disparities Research #
The pathways between race/ethnicity, socioeconomic status, and health disparities are complex in the United States, e.g. [1, 2]. Using observational public databases like CHIS, we can investigate issues in health disparities. (However, it is important to always remember that association is not causation, and consequently we can only talk about observed associations in the dataset.)  
  
As a simple example, we investigate the relationship between poverty-level and visiting the doctor in the past year. As in last week’s tutorial, we use a random sample of 500 respondents from the 2009 CHIS survey. (If you wish to do a more detailed analysis, you can download the entire CHIS dataset from their website.)


### 1. Does modeling the number of people who went to the doctor using the binomial distribution seem appropriate? ###
> => **Yes**  
> No 

2. This week, we stratify by poverty level. Within each of these groups, does modeling the number of people who went to the doctor using a binomial distribution seem appropriate?
> => **Yes**  
> No 


##  Solution ##
The binomial model is appropriate in both instances. For any population, there is a true proportion who goes to the doctor, and if we randomly sample from that population, we have a fixed p, fixed n, independent observations, and a binary outcome. Again, when we stratify, there is a fixed proportion of the population who goes to the doctor. So, even though we are now considering different populations, the binomial model still works, but the "probability of success" changes when you stratify.
