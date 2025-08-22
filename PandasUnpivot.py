import pandas as pd

# Create a sample wide DataFrame
data = {'City': ['New York', 'London'],
        'Jan_Sales': [100, 150],
        'Feb_Sales': [120, 160],
        'Mar_Sales': [110, 140]}
df_wide = pd.DataFrame(data)

print("Wide DataFrame:")
print(df_wide)

# Unpivot the DataFrame using melt
df_long = pd.melt(df_wide, id_vars=['City'], 
                  value_vars=['Jan_Sales', 'Feb_Sales', 'Mar_Sales'],
                  var_name='Month', value_name='Sales')

print("\nLong DataFrame (unpivoted):")
print(df_long)