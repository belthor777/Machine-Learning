## Trends in Unemployment ##
> We again use publicly available data from the World Bank’s website to examine national trends in unemployment percentages (percent unemployed in total labor force) in four countries: the United States, Great Britain, Japan, and Canada.  
>  
In this question, we examine unemployment trends over time using a correlation analysis, focusing primarily on the United States and Japan.  
>  
> Use the dataset UnemploymentbyCountry.dta to answer the following questions. 

```stata
	use "UnemploymentbyCountry.dta"
```

### Consider the following questions: ###

#### 1. Calculate the Pearson and Spearman correlations between total unemployment and year for the United States and for Japan. ####

##### United States: ######
* Pearson: **-0.3415**
* Spearman: **-0.4517**

```stata
	pwcorr unemployedtotal year if country == "United States", sig
```

```stata
	spearman unemployedtotal year if country == "United States"
```

##### Japan: ######
* Pearson: **0.8437**
* Spearman: **0.8162**

```stata
	pwcorr unemployedtotal year if country == "Japan", sig
```

```stata
	spearman unemployedtotal year if country == "Japan"
```

#### 2. Exclude all years after 2007 (recall that the financial collapse occurred in late 2008). Recalculate the correlations in question 1. (Hint: use an "if" command to restrict to certain years in Stata.) ####

##### United States: ######
* Pearson: **-0.7557**
* Spearman: **-0.7733**

```stata
	pwcorr unemployedtotal year if country == "United States" & year < 2008, sig
```

```stata
	spearman unemployedtotal year if country == "United States" & year < 2008
```

##### Japan: ######
* Pearson: **0.8276**
* Spearman: **0.7998**

```stata
	pwcorr unemployedtotal year if country == "Japan" & year < 2008, sig
```

```stata
	spearman unemployedtotal year if country == "Japan" & year < 2008
```


#### 3. Construct a scatter plot with year on the x-axis and with both unemployment in the United States and unemployment in Japan on the y-axis. ####
> **Hint1:** try plotting different symbols for the United States and Japan by creating two different plots within the Twoway graphs window; restrict to a specific country by using an "if" statement within each plot window).

##### Which pattern best describes the trend in unemployment in the United States between 1980 and 2010? ##### 
* linear 
* quadratic 
* => **cyclic**
* gradual non-linear increase 

```stata
	twoway (connected unemployedtotal year if country=="United States") if year > 1979 & year < 2011
```

##### Which pattern best describes the trend in unemployment in the Japan between 1980 and 2010? #####
* linear 
* quadratic 
* cyclic
* **gradual non-linear increase** 

```stata
	twoway (connected unemployedtotal year if country=="Japan") if year > 1979 & year < 2011
```


#### 4. True or False: correlation analyses have the potential to mask important non-linear trends in data. ####
> **Hint1:** Can correlation analysis hide non-linear relationships.
* => **True**
* False


Are there not other methods to analyze non linear relationship like spearman and rank test? 

Spearman and rank are used for not normal distributed data. In Q4 we are interested about "non-linear trends". And this is a big difference.

#### 5. Restricting to the United States, construct a scatterplot with year on the x-axis and with total unemployment; unemployment among women; and unemployment among men on the y-axis. Do there appear to be sex-specific differences in the unemployment trends? #### 
* True
* **False**

```stata
	twoway (scatter unemployedf year if country=="United States", sort) (scatter unemployedm year if country=="United States", sort)
```

