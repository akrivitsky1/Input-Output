cost = int(input("Enter cost of car:"))
miles_year = int(input("Enter miles driven per year:"))
gas = int(input("Enter cost of gas:"))
mpg = int(input("Efficency in miles per gallon:"))
resale = int(input("Estimated resale value after 5 years:"))

depreciation = cost - resale
cost_gas = ((gas/mpg)*miles_year) * 5
five_year = depreciation + cost_gas 

print("Five year cost:",float(five_year))
