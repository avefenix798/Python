import pandas as pd
from pandasql import sqldf

# Create a sample DataFrame
data = {'date_column': pd.to_datetime(['2020-01-15', '2020-03-20', '2021-02-10', '2021-07-25', '2022-04-01']),
        'value': [10, 15, 20, 25, 30]}
df = pd.DataFrame(data)

# Define the SQL query to group by year and sum the 'value'
query = """
SELECT
    strftime('%Y', date_column) AS year,
    SUM(value) AS total_value
FROM
    df

GROUP BY year
HAVING SUM(value) > 30
ORDER BY year;
"""

# Execute the query using pandasql
result = sqldf(query, globals())

# Print the result
print(result)