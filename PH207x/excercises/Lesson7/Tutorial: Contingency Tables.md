# Tutorial: Contingency Tables #
> *cs* - Cohort Study, estimate an Odds Ratio (OR), Pearson Chi-square  
> *tabulate* - Conduct a Pearson Chi-square test, R x C  

	use "chis_healthdisparities.dta", replace
	tabulate poverty doctor, row
	tabulate poverty doctor, row expected

	cs doctor poverty, or woolf

	gen nopoverty = 1-poverty
	cs doctor nopoverty, or woolf


##Pearson Chi-square test##
> **Step1:**

	tabulate poverty doctor, row expected

> Look if all expected cell counts (expected frequency command) are higher than 5

	cs doctor poverty, or woolf
	tabulate poverty doctor, row expected chi2

## Presenting Results ##
> *Cohort Study*: Use the **Risk difference**  
> Never use the p-value to present the results.

# Install R by C table addon for stata#

	ssc install tabplot

> Example:

	tabplot racecat poverty
	tabplot poverty racecat
	tabulate racecat pov, row


