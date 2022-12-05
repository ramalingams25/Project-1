import  pandas as pd
df = pd.read_csv("melb_data_processed_v1.csv")
df.head(2)
#Creating a subset of the main data to do the data cleaning autmatically
housing = df[['Price','Bedroom2','Bathroom','Landsize','YearBuilt','Distance','Regionname']].copy()
#To see the missing data records and its percentage
print(housing.isnull().sum())
print((housing.isnull().sum()/len(housing))*100)
#To remove 'BuildingArea' column from the subset dataset
housing.drop('BuildingArea',inplace=True,axis=1)
print(housing.head(2))
#To find the mean and update the missing values in Bedroom_mean
Bedroom_mean = housing['Bedroom2'].mean()
Bedroom_mean = round(Bedroom_mean,0)
print(Bedroom_mean)
housing['Bedroom2'].fillna(Bedroom_mean,inplace=True)
#To find the mean and update the missing values in Bathroom Column
Bathroom_mean = housing['Bathroom'].mean()
Bathroom_mean = round(Bathroom_mean,1)
print(Bathroom_mean)
housing['Bathroom'].fillna(Bathroom_mean,inplace=True)
#To see the missing data records and its percentage
print(housing.isnull().sum())
print((housing.isnull().sum()/len(housing))*100)