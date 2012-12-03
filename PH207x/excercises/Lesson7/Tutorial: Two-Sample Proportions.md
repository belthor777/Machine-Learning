# Tutorial: Two-Sample Proportions #
> X_1 ~ Bin(n_1, p_1)  H_0: p_0=p_1  
> X_0 ~ Bin(n_0, p_0)  H_A: p_0 != p_1  
>  
> X_1 ~ N( μ_1, σ²)  H_0: μ_1=μ_2  
> X_0 ~ N( μ_0, σ²)  H_A: μ_1 != μ_2  
  
> **T-Distribution**  
> t= ( ̅x_1 -  ̅x_2) / s*p*sqrt(1/n_1 + 1/n_2)  
>  
> ^p_1= x_1/n_1  
> ^p_0= x_0/n_0  
>  
> Z= ^p_1 - ^p_0 / sqrt( p(1-p) * ( 1/n_1 + 1/n_2 ) )
> p= x_1 + x_2 / n_1 + n_2


### Test in Stata ###
> H_0: p_1=p_0  
> H_A: p_1 != p_0  
> alpha=0.05  
> 95%  

	tabulate poverty doctor

>                    | Visited doctor in the|  
>  Below the federal |    past 12 months    |  
>      poverty level | Didn't go  Went to d |     Total  
> -------------------+----------------------+----------  
> Above poverty line |        79        358 |       437  
> Below poverty line |        19         44 |        63  
> -------------------+----------------------+----------  
>              Total |        98        402 |       500  
  
> p = (358 + 44) / (437 + 63)= 0.804  
  
> **Compare Poverty line**
> 63*0.084= 50.7  
> 63*(1-0.084)= 12.3  



