import requests
import numpy as np
import pandas as pd
import json

page = 1
responses = []
url = "https://api.openbrewerydb.org/v1/breweries"
payload = {'page':page, 'per_page':125}
headers = {}

##iterate over 50 pages pulling 125 records for each page
while page < 50:
    page = page + 1
    response = requests.request("GET", url, headers=headers, data=payload).json()
    responses.extend(response)
##convert the list of responses to a pandas dataframe
frames = []
for r in responses:
    frames.append(r)
breweries = pd.DataFrame(frames)
## save the dataframe to memory as a csv
breweries.to_csv('open_breweries_US.csv')

