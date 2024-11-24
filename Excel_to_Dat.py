import csv
from collections import defaultdict

Countries = dict()

#read the unemployment rate file for rate and take the correct year and region for each country

with open("Unemployment rate.csv", "r", encoding='utf-8') as unemployment:
    unemployment_reader = csv.reader(unemployment)
    for country in unemployment_reader:
        if country[2] == '2023':
            Countries[country[0].strip().lower()] = [country[1], country[4], None, None, None]
        else:
            Countries[country[0].strip().lower()] = [None, country[4], None, None, None]

with open("Inflation_Rate_2023.csv", "r", encoding='utf-8') as inflation_rate:
    inflation_reader = csv.reader(inflation_rate)
    for country in inflation_reader:
        if country[0].lower().strip() not in Countries:
            print(country[0].lower(), "not seen")
        else:
            Countries[country[0].lower().strip()][2] = country[1]
        
with open("Interest_Rates_clean.csv" , "r", encoding='utf-8') as interest_rates:
    interest_rates = csv.reader(interest_rates)
    for country in interest_rates:
        if country[0].lower().strip() in Countries:
            Countries[country[0].lower().strip()][3] = country[1]
        else:
            print(country[0])

print("gdp")
with open("Real_GDP_growth_2023.csv", "r", encoding='utf-8') as gdp_growth:
    gdp_growth = csv.reader(gdp_growth)
    for country in gdp_growth:
        if country[0].lower().strip() in Countries:
            Countries[country[0].lower().strip()][4] = country[1]
        else:
            print(country[0])

        


with open("econ.dat", "w", newline='', encoding='utf-8') as write_file:
    writer = csv.writer(write_file)
    writer.writerow(["Name", "Unemployment", "region", "inflation_rate", "interest_rates", "gdp_growth"])
    for country in Countries:
        if Countries[country][0] is not None and Countries[country][2] is not None:
            writer.writerow([country, Countries[country][0], Countries[country][1],
                              Countries[country][2], 
                              Countries[country][3], 
                              Countries[country][4]])
