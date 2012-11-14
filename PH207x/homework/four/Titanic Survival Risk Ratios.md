# Titanic Survival Risk Ratios 
The following table describes the survival status of passengers on the Titanic, stratified by Passenger Class (First, Second, or Third), Sex/Age (Child, Women, or Man), and Survival Status. The Frequency column indicates the number of passengers in each stratum. (For example there were 4 1st class women passengers who did not survive and 140 1st class women passengers who did survive). These data were obtained from the website anesi.com and refers to British Parliamentary Papers, Shipping. Casualties (Loss of the Steamship “Titanic”), 1912. cmd 6352 “Report of a Formal Investigation into the circumstances attending the foundering on the 15th April 1912 of the British Steamship “Titanic” of Liverpool after striking ice in or near Latitude 41 46 N., Longitude 50 14 W., North Atlantic Ocean, whereby loss of life ensued (London; His Majesty’s Stationary Office, 1912) page 42. 

Passenger Class | Age/Sex | Survival Status | Frequency
--------------- | ------- | --------------- | -----------
First | Child | Survived | 6
First | Child | Did not survive | 0
First | Woman | Survived | 140
First | Woman | Did not survive | 4
First | Man | Survived | 57
First | Man | Did not survive | 118
Second | Child | Survived | 24
Second | Child | Did not survive | 0
Second | Woman | Survived | 80
Second | Woman | Did not survive | 13
Second | Man | Survived | 14
Second | Man | Did not survive | 154
Third | Child | Survived | 27
Third | Child | Did not survive | 52
Third | Woman | Survived | 76
Third | Woman | Did not survive | 89
Third | Man | Survived | 75
Third | Man | Did not survive | 387

##### Q1. Use these data to calculate the Risk Ratio for surviving comparing “women or children” as the exposed group and “all other passengers” as the non-exposed group. #####
=> Surviving Risk Ratio= ?

>                    | Died | Surviving | Total | Estimated Risk
> ------------------ | ---- | --------- | ----- | ------------------
>  Women or children | 158  | 353       | 511   | 353/511= 0.69080235
>  All other         | 659  | 146       | 805   | 146/805= 0.18136646

Risk Ratio: RR= 0.69080235 / 0.18136646= **3.808876**



##### Q2. Use these data to calculate the Risk Ratio for surviving comparing “women or children” as the exposed group and “all other passengers” as the non-exposed group for each passenger class. #####

###### a) First Class ######
Surviving Risk Ratio= **2,9883040936**

###### b) Second Class ######
Surviving Risk Ratio= **10,6666666667**

###### c) Third Class ######
Surviving Risk Ratio= **2,6003278689**


