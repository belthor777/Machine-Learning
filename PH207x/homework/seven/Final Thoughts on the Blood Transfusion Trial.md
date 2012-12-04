# Final Thoughts on the Blood Transfusion Trial #
> Continue using the Fergusson et al. (2012) clinical trial example from the previous two problems to complete the following questions.

#### 1. In the previous questions, we looked at three different tests of association: the Pearson Chi-square test, a 95% confidence interval for the odds ratio, and a risk difference test. ####

##### Are the results of these three tests consistent? #####
> Yes  
> No

##### Would you expect the results of the three tests to be consistent? #####
> Yes  
> No 

#### 2. Is there evidence of an association between blood group assignment and the composite outcome? #####
> Yes  
> No

#### 3. Think back to the Bonferroni correction from last week. If you were tasked with conducting hypothesis tests comparing the two blood groups for each of the 5 different outcomes, would you need to correct for multiple comparisons? #####
> Yes  
> No


#### 4. In this study, the authors state that they powered the study to detect an absolute difference of 15% in the two groups with 80% power, using a 2-sided test with alpha=0.05. After a few more adjustments, their final sample size calculation was 450. #####
> Now suppose you want to replicate the study using a different population. Given that the authors did not find an association in their data, you decide to increase the power and decrease the difference detected between standard and fresh groups. Using an equal number of infants in both groups, what is the total sample size needed in order to achieve 90% power, assuming that the proportion of infants experiencing the composite outcome in the standard group was 55% and 45% in the fresh blood group (again, with  alpha=0.05).
> **Hint1:** You can simply use stata dropdown menus as follows ... Statistics >> Power and Sample size >> Tests of means and proportions >> 2 sample comparison proportions >> input your proportions in 0.** way >> go to options and adjust the significance level and the power >> hit submit ... finally use your calculator ....... Good luck 

	sampsi .45 .55, alpha(0.05) power(0.90)

> total sample size= **1088**


#### 5. Consider a covariate, the clinical risk index for babies (CRIB), which was measured in the infants enrolled in the clinical trial. CRIB is usually associated with the composite outcome. From the baseline characteristics table in the Fergusson et al paper, we find that the median and IQR for CRIB is similar between the standard and fresh blood groups. This suggests that the distribution of CRIB is similar in both groups. #####
> True or False: Because the distribution of CRIB is similar betwen groups, the study investigators would not have gained any power to detect an effect by matching on CRIB score.  
>  
> => **Yes**  
> No

