# Problem Statement:
# The task is to scrape the list of largest companies in US by revenue form wikipedia using
#  Beautiful Soup in Python. The data required to be extracted includes the rank, name of company,
#  Industry, Revenue, Revenue growth, Headquaters.

# Question:
# What is the process to extract data from the wikipedia website using Beautiful Soup in Python? 
# Specifically, how can we extract the rank, name of the company, Industry, Revenue, Revenue growth,
#  Headquarters for the top US companies by Revenue?

#########################################################################################
import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue")
#print(response)
soup= BeautifulSoup(response.content,'html.parser')
table=soup.find("table",class_="wikitable sortable")

data = []
headers = [th.text.strip() for th in table.find_all("th")]

#print(headers)

for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    Rank=cols[0].text.strip()
    Name=cols[1].text.strip()
    Industry=cols[2].text.strip()
    Revenue=cols[3].text.strip()
    RevenueGrowth=cols[4].text.strip()
    #Employees=cols[5].text.strip()
    Headquarters=cols[6].text.strip()
    
    data.append([Rank,Name,Industry,Revenue,RevenueGrowth,Headquarters])
#print(data)
   
df=   pd.DataFrame(data,columns=["Rank","Name","Industry","Revenue","RevenueGrowth","Headquarters"])

print(df.head())

######################## End of the program #########################################