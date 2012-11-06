

********** Lab Exercise 1 ***********

use "C:\Documents and Settings\LHUND\My Documents\Lauren\POSTDOC\TA\EdX\Data\fhsclean.dta", clear
log using "C:\Documents and Settings\LHUND\My Documents\Lauren\POSTDOC\TA\EdX\Lab exercises\lab1.smcl"

************ Exploring data **************

describe
codebook
summarize sysbp1
summarize sysbp1, detail
summarize sysbp1 if sex1==1
bysort sex1: summarize sysbp1
tabulate sex1
tabulate sex1, missing
tabulate sex1 prevhyp1

*Now suspend your log file by clicking the Log button.
log off

*List the first 50 observations for sbp1 and sex1.
list sysbp1 sex1 in 1/50

********* Creating New Variables **********

*Create a new variable called agesq1 that is the square of age at exam 1. 
generate agesq1=age1*age1
drop agesq1
generate agesq1=age1^2

generate agecat1=. 
replace agecat1=1 if age1 < 40
replace agecat1=2 if age1 >= 40 & age1 < 50
replace agecat1=3 if age1 >= 50 & age1 < 60
replace agecat1=4 if age1 > 60 & age1 < .

*Double check our work after creating new variables!
summarize age1 agesq1
tabulate agecat1, missing

*Add labels to the new variables we created, agesq1 and agecat1.
label variable agesq1 "Age squared, exam 1”
label variable agecat1 “Categorical age, exam 1”

tabulate sex1 

*Add labels to the values of agecat1.  
abulate agecat1
label define agecatlabel 1 "30-39" 2 "40-49" 3 "50-59" 4 "60-70"
label values agecat1 agecatlabel
tabulate agecat1

describe

******** GRAPHING ***********

*Create a box plot for sysbp1. 
graph box sysbp1

*Create a histogram for sysbp1. 
histogram sysbp1

*What happens to the graph when you change the number of bins?
histogram sysbp1, bin(20)
histogram sysbp1, bin(50)

*Create separate histograms of sysbp1 for males and females. 
histogram sysbp1, by(sex1)

*Create a scatterplot of sysbp1 and sysbp2.
 scatter sysbp1 sysbp2

