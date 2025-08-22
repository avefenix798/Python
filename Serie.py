import pandas as pd
import matplotlib.pyplot as plt
def main():
    # Example: Creating sample time series data
    dates = pd.to_datetime(pd.date_range(start='2023-01-01', periods=100, freq='D'))
    values = [i + (i**0.5) * 5 for i in range(100)] # Sample values with a trend
    df = pd.DataFrame({'Value': values}, index=dates)

    plt.figure(figsize=(10, 6)) # Set figure size for better readability
    plt.plot(df.index, df['Value'])
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Ejemplo Serie de tiempo Grafico')
    plt.grid(True) # Add a grid for easier reading
    plt.show()

if __name__ =='__main__':
    main()