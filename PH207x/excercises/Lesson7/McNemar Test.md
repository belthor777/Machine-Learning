# McNemar Test #
> Paired Dichotomies  
> MI= Myocardial infarction  
> e.g. Pairs matched on age & sex:

Diabetes | M.I. Yes | M.I. No | Total
-------- | -------- | ------- | ------
Yes      | 46       | 25      | 71
No       | 98       | 119     | 217
Total    | 144      | 144     | 288

> So we have 144 pairs and we want to use McNemar's Test:

                   | No M.I. - Diabetes | No M.I. - No Diabetes | Total
------------------ | ------------------ | --------------------- | ------
M.I. - Diabetes    | 9                  | 37                    | 46
M.I. - No Diabetes | 16                 | 82                    | 98
Total              | 25                 | 119                   | 144

## Chi-squared ##
> Discordant entries: 37 & 16  
> x²= SUM of all cells [ ( |obs-exp|**-1** )² / exp ]  
> **-1**: Stata ignores the correction factor, 1
>  
> x²= ( |37-16|-1 )² / (37+16)  
>   = 7.55  
>  
> x²_(1,0.010)=6.63  
> x²_(1,0.001)=10.83  
> => **0.001<p<0.010**  
>  
> p < 0.05
