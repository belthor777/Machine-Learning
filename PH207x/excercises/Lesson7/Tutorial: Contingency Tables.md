# Tutorial: Contingency Tables #
> *cs* - Cohort Study, estimate an Odds Ratio (OR), Pearson Chi-square  
> *tabulate* - Conduct a Pearson Chi-square test, R x C  

	use "chis_healthdisparities.dta", replace
	tabulate poverty doctor, row
	tabulate poverty doctor, row expected

	cs doctor poverty, or woolf

	gen nopoverty = 1-poverty
	cs doctor nopoverty, or woolf

