
import pandas as pd
import plotly.express as px

data = pd.read_csv("D:\data\country_vaccinations.csv")
#print(data)
print(data.head())
print(data.describe())
print(pd.to_datetime(data.date))
print(data.country.value_counts())
data = data[data.country.apply(lambda x: x not in ["England", "Scotland", "Wales", "Northern Ireland"])]
print(data.country.value_counts())
print(data.vaccines.value_counts())

df = data[["vaccines", "country"]]
print(df.head())

vaccine_map = px.choropleth(data, locations = 'iso_code', color = 'vaccines')
vaccine_map.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
vaccine_map.show()

