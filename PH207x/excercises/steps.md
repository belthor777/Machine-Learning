# Pre Test:
> Pretest: Prevalence is 16.1%. Which means out of 100 people, 16.1 people have disease. That means 100 - 16.1 do not have the disease.

# Post Test
1. When the test is carried out, ideally all 16.1 should test positive, But the sensitivity being 0.721, out of 16.1, only (16.1 * 0.721) test positive. Remaining test -ve inspite of having disease. So 16.1 - (16.1 * 0.721) is the number of cases who have disease and yet have tested negative (False Negative).

2. So the proportion who test FN is = Number tested False Negative in Step 2 / Total No of patients with disease (16.1). This will give you your FN rate.

3. Now from Step 1 we know how many people do not have disease. This is the number which should ideally test -ve if the specificity was 100% i.e. 1. But since specificity is only 0.932, only (100 - 16.1) * 0.932 test -ve.

4. This means ((100 - 16.1) - (100 - 16.1) * 0.932) test positive inspite of not having a disease. These are your False Positive Cases.

5. So now calculate the FP rate similar to how we calculated FN rate.

6. Now you have your FN and FP rates. Be happy.

7. Now your PPV is TRUE POSITIVE / TOTAL POSITIVE. Here true positive is the value you got in Step 2 (16.1* sensitivity)). And Total Positives is this value plus FP you got in step 5.

8. Similarly your NPV is True Negative / Total Negative values.

9. Use the formula 1-PPV and 1-NPV.

10. If you get all correct, you must wear a big smile!
