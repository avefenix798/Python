# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:11:42 2024

@author: Usuario
"""

from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient

import itertools
import pandas as pd


credentials = service_account.Credentials.from_service_account_file( r'C:\Users\Usuario\Downloads\active-guild-346221-85e5ccf45631.json')


client = BetaAnalyticsDataClient(credentials=credentials)

def query_data(api_response):
    dimension_headers = [header.name for header in api_response.dimension_headers]
    metric_headers = [header.name for header in api_response.metric_headers]
    dimensions = []
    metrics = []
    for i in range(len(dimension_headers)):
        dimensions.append([row.dimension_values[i].value for row in api_response.rows])
    dimensions
    for i in range(len(metric_headers)):
        metrics.append([row.metric_values[i].value for row in api_response.rows])
    headers = dimension_headers, metric_headers
    headers = list(itertools.chain.from_iterable(headers))   
    data = dimensions, metrics
    data = list(itertools.chain.from_iterable(data))
    df = pd.DataFrame(data)
    df = df.transpose()
    df.columns = headers
    return df
# Set up GA4 request
request = {
  "property": "properties/460121467", #input your property ID from Google Analytics 4 admin settings
  "date_ranges": [
    {
      "start_date": "2024-01-01", #adjust to your start date
      "end_date": "2024-09-24" #adjust to your end date
    }
  ],
  "dimensions": [   #input the dimensions you need
    {
      "name": "country"
    },
    {
      "name": "city"
    }
  ],
  "metrics": [ #input the metrics you need
    {
      "name": "sessions"
    },
    {
      "name": "transactions"
    }
  ]
}

# Execute GA4 request
response = client.run_report(request)

datos = query_data(response)

print (datos)
