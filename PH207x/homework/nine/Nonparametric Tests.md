## Nonparametric Tests ##

#### 1. Suppose we wish to test a new treatment for dry, itchy eyes. We gather a group of eye patients, and, for each patient, we randomly treat one eye with the experimental treatment and one eye with the standard treatment. The outcome, eye relief, is a continuous measure, and the distribution of the differences in eye relief between eyes is normally distributed. Suppose we want to test whether the treatment is effective at improving eye relief. Which of the following tests is valid: ####
> **Hint1:** Continues, normally distributed and we have dependent variables
* sign test 
* signed-rank test 
* paired t-test 
* all of the above 


#### 2. Suppose you are conducting a two-sided sign test. You have data from 8 paired samples, and you observe 1 positive sign and 7 negative signs. What is the p-value corresponding to the null hypothesis that there is no difference in median between the two groups? ####

```stata
	use "CVOS_me"
	signtest t6=t0
```

        sign | observed | expected
------------ | -------- | ---------
    positive | 1        | 4
    negative | 7        | 4
        zero | 0        | 0
   **TOTAL** | **8**    | **8**

```stata
One-sided tests:
  Ho: median of t6 - t0 = 0 vs.
  Ha: median of t6 - t0 > 0
      Pr(#positive >= 1) =
         Binomial(n = 8, x >= 1, p = 0.5) =  0.9961

  Ho: median of t6 - t0 = 0 vs.
  Ha: median of t6 - t0 < 0
      Pr(#negative >= 7) =
         Binomial(n = 8, x >= 7, p = 0.5) =  0.0352

Two-sided test:
  Ho: median of t6 - t0 = 0 vs.
  Ha: median of t6 - t0 != 0
      Pr(#positive >= 7 or #negative >= 7) =
         min(1, 2*Binomial(n = 8, x >= 7, p = 0.5)) =  0.0703
```

#### 3. Walker et al. (1987) examined the characteristics of children dying from sudden infant death syndrome. The sids.dta contains the age at death (in days) for a sample of 12 girls and 17 boys. Using an appropriate non-parametric test with a 0.05 level of significance, test whether the median age at death is the same for boys and girls. Be sure to verify the assumptions of your test. ####

##### What is the absolute value of your test statistic? #####
> **Hint1:** ABSOLUTE = NO NEGATIVE SIGN !!!!  
> **Hint2:** I did not put the test statistic in as 0.xxxx, just as .xxxx. Don't know if that will make a difference for you or not.  
> **Hint3:** You need to view/read the tutorial segment Nonparametrics for Independent Samples.  
> => **|Z|=|-0.044|=0.044**

```stata
	use "sids.dta"
	pwcorr Age Sex, sig
	spearman Age Sex
	ranksum Age, by(Sex)
```

##### What is your p-value? #####
> => **0.9647**


###### Based on this test, can you conclude that we do not have enough evidence to suggest that the median age at death is different between boys and girls? ######
* => **Yes**
* No

###### Would it be appropriate to use a two-sample t-test in this case?. ######
* Yes
* => **No**


