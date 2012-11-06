use "/home/thomas/Dokumente/PH207x/datasets/fhs.2d92301d751b.dta"
describe
codebook
codebook bmi1 bmi2 bmi3
describe  bmi1 bmi2 bmi3
summarize sysbp1
summarize sysbp1, detail
di 295-83.5
by sex1, sort : summarize sysbp1
by sex1, sort : summarize sysbp1 if sex1 == 1
tabulate sex1 prevhyp1
list 1
list sysbp1 1
list sysbp1
use "/home/thomas/Dokumente/PH207x/datasets/framingham_dataset.dta"
tabulate glucose1
summarize glucose1
summarize
di 4434-4037
by sex1, sort : summarize glucose1, detail
summary diabetes1
summarize diabetes1
by sex1, sort : summarize diabetes1, detail
by sex1, sort : summarize diabetes1, detail
tabulate diabetes1 if sex1==2
by sex1, sort : summarize glucose1, detail
by sex1,=2 sort : summarize glucose1, detail
by sex1, sort : summarize glucose1, detail, if sex1==2
by sex1, sort : summarize glucose1, detail, if sex1==2
summarize glucose1
#
max(summarized)
max(summarize)
describe
describe obs
describe glucose1
summarize glucose1
generate agesq1 = age1*age1
generate agecap1 = .
replace agecat1 = 1 if age1 < 40
generate agecat1 = .
replace agecat1 = 1 if age1 < 40
replace agecat1 = 2 if age1 >= 40 & age1 < 50
replace agecat1 = 3 if age1 >= 50 & age1 < 60
replace agecat1 = 4 if age1 >= 60 & age1 <= 70
tabulate agecat1
generate agecat1 = .# Generate Missing Values
generate agecat1 = .; Generate Missing Values
generate agesq1 = age1*age1
summarize agesq1
drop agesq1
label variable agecat1 "Age categorical at exam1"
agecat1
label define agecatlabel 1 "30-39" 2 "40-49" 3 "50-59" 4 "60-70"
label values agecat1 agecatlabel
tabulate agecat1
generate bmihigh1 = .# Generate Missing Values
replace bmihigh1 = 0 if bmi1 <= 25
replace bmihigh1 = 1 if age1 > 25
tabulate bmihigh1
generate bmihigh1 = .
replace bmihigh1 = 0 if bmi1 <= 25
replace bmihigh1 = 1 if age1 > 25
tabulate bmihigh1
drop bmihigh1
generate bmihigh1 = .
replace bmihigh1 = 0 if bmi1 <= 25
replace bmihigh1 = 1 if bmi1 > 25
tabulate bmihigh1
drop bmihigh1
generate bmihigh1 = .
replace bmihigh1 = 0 if bmi1 <= 25
replace bmihigh1 = 1 if bmi1 > 25
replace bmihigh1 = 1 if bmi1 > 25 & bmi1 <.
tabulate bmihigh1
drop bmihigh1
codebook bmi1 
codebook bmi1
generate bmihigh1 = .
replace bmihigh1 = 0 if bmi1 <= 25
replace bmihigh1 = 1 if bmi1 > 25
replace bmihigh1=1 if bmi1 >25 & bmi1 <= 60
tabulate bmihigh1
drop bmihigh1
codebook bmi1
generate bmihigh1 = .
replace bmihigh1 = 0 if bmi1 <= 25
replace bmihigh1=1 if bmi1 >25 & bmi1 <= 60
tabulate bmihigh1
drop bmihigh1
summarize bm1
summarize bmi1
generate bmihigh1 = .
replace bmihigh1 = 0 if bmi1 <= 25
replace bmihigh1 = 1 if bmi1 >25 & bmi1 <= 60
replace bmihigh1 = missing if bmi1 > 60
tabulate bmihigh1
drop bmihigh1
generate bmihigh1 = .
replace bmihigh1 = 0 if bmi1 <= 25
replace bmihigh1 = 1 if bmi1 >25 & bmi1 <= 60
replace bmihigh1 = 2 if bmi1 > 60
tabulate bmihigh1
drop bmihigh1
generate bmihigh1 = .
replace bmihigh1 = 0 if bmi1 <= 25
replace bmihigh1 = 1 if bmi1 >25 & bmi1 <= 60
replace bmihigh1 = 2 if bmi1 > 60
label define bmihigh1_label 1 "0" 2 "1" 3 "missing"
label values bmihigh1 bmihigh1_label
tabulate bmihigh1
drop bmihigh1
generate bmihigh1 = .
replace bmihigh1 = 0 if bmi1 <= 25
replace bmihigh1 = 1 if bmi1 >25 & bmi1 <= 60
replace bmihigh1 = 2 if bmi1 > 60
label define bmihigh1_label 0 "0" 1 "1" 2 "missing"
label values bmihigh1 bmihigh1_label
tabulate bmihigh1
drop bmihigh1
generate bmihigh1 = .
replace bmihigh1 = 0 if bmi1 <= 25
replace bmihigh1 = 1 if bmi1 >25 & bmi1 <= 60
replace bmihigh1 = 2 if bmi1 > 60
label define bmihigh1_label 0 "0" 1 "1" 2 "missing"
label values bmihigh1 bmihigh1_label
tabulate bmihigh1
drop bmihigh1
drop bmihigh1_label
drop bmihigh1_label
drop bmihigh1_label 
mean
mean bmi1  bmi2 bmi3
generate meanbmi = mean bmi1  bmi2 bmi3
 mean bmi1  bmi2 bmi3
generate meanbmi = bmi1 bmi2 bmi3
generate meanbmi = bmi1 bmi2 bmi3 mean bmi1  bmi2 bmi3
 mean bmi1  bmi2 bmi3
generate meanbmi = 0
meanbmi = mean bmi1 bmi2
gen meanbmi= .
replace meanbmi= (bmi1+bmi2+bmi3)/3 if bmi1*bmi2*bmi3 >0
tabulate meanbmi
drop meanbmi
display meanbmi
gen meanbmi= .
replace meanbmi= (bmi1+bmi2+bmi3)/3 if bmi1*bmi2*bmi3 >0
tabulate meanbmi
describe meanbmi
summarize meanbmi
egen meanbmi2 = rowmean(bmi1 bmi2 bmi3)
by sex1, sort : summarize meanbmi2, detail
by sex1, sort : summarize meanbmi2, detail
summarize meanbmi2, detail
graph box sysbp1
graph box sysbp1
histogram sysbp1
histogram sysbp1, discrete
histogram sysbp1
histogram sysbp1, bin(10)
histogram sysbp1, bin(265)
histogram sysbp1, bin(50)
histogram sysbp1, bin(50) by(sex1)
graph box sysbp1, by(sex1)
twoway (scatter sysbp1 sysbp1)
twoway (scatter sysbp1 sysbp2)
histogram glucose1, by(sex1)
histogram glucose1
summary glucose1
summarize glucose1
summarize glucose1, detail
graph box heartrte1
twoway (scatter age1 glucose1)
twoway (scatter age1 glucose1)
codebook bmi1
generate bmihigh1 = .
replace bmihigh1 = 0 if bmi1 <= 25
replace bmihigh1 = 1 if bmi1 >25 & bmi1 <= 60
replace bmihigh1 = 2 if bmi1 > 60
label define bmihigh1_label 0 "0" 1 "1" 2 "missing"
label values bmihigh1 bmihigh1_label
tabulate bmihigh1
drop bmihigh1
drop bmihigh1_label
codebook bmi1
generate bmihigh1 = .
replace bmihigh1 = 0 if bmi1 <= 25
replace bmihigh1 = 1 if bmi1 >25 & bmi1 <= 60
label define bmihigh1_label 0 "0" 1 "1" 2 "missing"
label values bmihigh1 bmihigh1_label
tabulate bmihigh1
drop bmihigh1
drop bmihigh1_label
sumarize bmi1
summarize bmi1
describe
twoway (scatter bmi1 bmi2)
twoway (scatter bmi1 bmi2)
summarize bmi1
summarize bmi1, detail
summarize bmi1, detailif sex1=1
by sex1, sort : summarize bmi1, detail
graph box bmi1 if sex1
describe sex1
tabulate bmi1 sex1 
tabulate bmi1
tabulate sex1 
by sex1, tabulate bmi1
by sex1, tabulate bmi1 sex1
 tabulate bmi1
bysort sex1: summarize bmi1, detail
graph box bmi1, by(sex1)
generate meanbmi = .
replace meanbmi= bmi2-bmi1
summarize meanbmi
drop meanbmi
generate meanbmi = .
replace meanbmi= bmi2-bmi1
summarize meanbmi
drop meanbmi
display 10.43-(-10.5)
generate bmidelta = .
replace bmidelta = bmi2-bmi1
codebook bmidelta
bmidelta    
codebook bmidelta
graph bar (mean) bmidelta
graph box bmidelta if sex1
graph box bmidelta
graph pie, over(bmidelta)
graph pie, over(bmidelta)
graph matrix bmidelta
graph matrix bmidelta
twoway (scatter bmidelta bmidelta)
histogram bmidelta
generate bmidelta = .
replace bmidelta = bmi2-bmi1
display bmidelta+2
codebook bmidelta
generate bmidelta = .
replace bmidelta = bmi2-bmi1
display 0.067831+2*1.80152
display 0.067831-2*1.80152
 tabulate sex 1 prev hype 1
 tabulate sex 1 prevhype 1
 tabulate sex1 prevhype1
 tabulate sex1 prevhyp1
codebook death
codebook prevhyp1
summarize prevhyp1
 tabulate sex1 prevhype1
 tabulate sex1 prevhyp1
di 799*100/1430
di (100*799)/1430
.tabulate prevhyp1 sex1 . by sex1, sort : summarize prevhyp1
tabulate prevhyp1 sex1 . by sex1, sort : summarize prevhyp1
.tabulate prevhyp1 sex1
 tabulate sex1 prevhyp1
by sex1, sort : summarize prevhyp1
tab prevhyp1 sex1, cell
di (100*799)/1430+
di (100*799)/1430
