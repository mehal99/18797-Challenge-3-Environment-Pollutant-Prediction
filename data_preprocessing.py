import pandas as pd
# Read the data from the CSV file
df = pd.read_csv("/content/data.csv")
# Display the DataFrame to verify the data
print(df.head)

# Filter the data for PM2.5 and OZONE pollutants
filtered_df = df[df['Pollutant'].isin(['PM2.5', 'OZONE'])]

#separate PM2.5 and OZONE values into different columns
pivot_df = filtered_df.pivot(index=["Timestamp"], columns="Pollutant", values=["Concentration", "Unit", "AQI", "AQI Category"])
pivot_df.reset_index(inplace=True)

# Flatten the multi-level column names
pivot_df.columns = ['_'.join(col).strip() for col in pivot_df.columns.values]
pivot_df.rename(columns={"Timestamp_": "Timestamp", "Concentration_PM2.5": "Concentration_PM2.5", "Concentration_OZONE": "Concentration_Ozone", "Unit_PM2.5": "Unit_PM2.5", "Unit_OZONE": "Unit_Ozone", "AQI_PM2.5": "AQI_PM2.5", "AQI_OZONE": "AQI_Ozone", "AQI Category_PM2.5": "AQI Category_PM2.5", "AQI Category_OZONE": "AQI Category_Ozone"}, inplace=True)

print(pivot_df)
pivot_df.to_csv("/content/filtered_data.csv")