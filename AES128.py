test
convert hexstring to binary
figure out key iteration
arrange pt into 4x4 array of 8 bits per
numpy array
the more you see pt
#Import Packages
import pandas as pd

#Load CSV File
data = pd.read_csv("sp500.csv", parse_dates=['Date'])




#Q6 -----------------------------------------------------------------------------------------



#Filter data for the years 2017-2018 (Until Month 4)
filtered_data = data[(data['Date'] >= '2017-01-01') & (data['Date'] <= '2018-12-31')] #Data Ends M-4

#Group data by month
monthly_data = filtered_data.groupby(pd.Grouper(key='Date', freq='M'))

#Print months
for month, month_data in monthly_data:
    print(f"Month: {month.year} - {month.month:02d}")
    print(f"Average Open Price: {month_data['Open'].mean()}")
    print(f"Average Close Price: {month_data['Close'].mean()}")
    print(f"Average Transaction Volume: {month_data['Volume'].mean()}")
    print(f"Total Gain/Loss: {month_data['Close'].iloc[-1] - month_data['Open'].iloc[0]}")
    print("\n---------------------------------------------------------------------------------\n")

#Query months with a certain range of open prices
query_range = data[(data['Open'] >= 600) & (data['Open'] <= 850)]

#Display the query result
print("Months with open prices between 600 and 850:")
print(query_range)



#Q7 -----------------------------------------------------------------------------------------


#Filter data for the years 1950-2018 
filtered_data = data[(data['Date'].dt.year >= 1950) & (data['Date'].dt.year <= 2018)]

#Group data by year
yearly_data = filtered_data.groupby(filtered_data['Date'].dt.year)

#Initialize variables for most profitable year
most_profitable_year = None
max_gain = float('-inf')

#Print years + the most profitable year at the end
for year, year_data in yearly_data:
    avg_open_price = year_data['Open'].mean()
    avg_close_price = year_data['Close'].mean()
    avg_transaction_volume = year_data['Volume'].mean()
    gainLoss = year_data['Close'].iloc[-1] - year_data['Open'].iloc[0]

    #Check if gain loss is the new highest gainer
    if gainLoss > max_gain:
        most_profitable_year = year
        max_gain = gainLoss

    print(f"Year: {year}")
    print(f"Average Open Price: {avg_open_price}")
    print(f"Average Close Price: {avg_close_price}")
    print(f"Average Transaction Volume: {avg_transaction_volume}")
    print(f"Gain/Loss: {gainLoss}")
    print("\n---------------------------------------------------------------------------------\n")

#Print the most profitable year
print(f"The most profitable year is: {most_profitable_year}. Total Gain: {max_gain}")
