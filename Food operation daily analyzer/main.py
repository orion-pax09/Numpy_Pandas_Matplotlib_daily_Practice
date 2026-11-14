import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("delivery.csv")
copy_df = df.copy()
#Task 01 Explore the datasets
print("Display the first five records")
print(copy_df.head(5))
print("Number of rows and columns")
print(copy_df.shape)
print("Inspect data types")
print(copy_df.dtypes)
print("Count missing values ine ach columns")
print(copy_df.isna().sum())
#Task 02 Remve duplicates
print("Identify duplicates record")
print(copy_df.duplicated())
print("Drop duplicates...")
drop_dp = copy_df.drop_duplicates()
print(drop_dp.duplicated())
#Task 03 Handle missing values
print("Find missing values in numcerical records")
print(drop_dp.isna())
print("Replacing missing values with median")
drop_dp["delivery_time_min"] = drop_dp['delivery_time_min'].fillna(drop_dp["delivery_time_min"].median())
drop_dp["rating"] = drop_dp["rating"].fillna(drop_dp["rating"].median())
print(drop_dp.duplicated())
#Task 04 Numpy statistical analysis
print("Numpy array")
to_numpy = drop_dp.to_numpy()
print("Calculate the mean of delivery time:")
delivery_Array = drop_dp["delivery_time_min"].to_numpy()
mean_del = np.mean(delivery_Array).round(2)
print(mean_del)
print("Calculate median delivery time")
median_Del = np.median(delivery_Array)
print(median_Del)
print("Standard deviation of delivery time")
std_del = np.std(delivery_Array).round(2)
print(std_del)
Max_del = np.max(delivery_Array)
min_dl = np.min(delivery_Array)
print("Maximum delivery time: ",Max_del)
print("Minimum delivery time: ", min_dl)
#Task 05 Traffic analysis
print("Average delivery time for low traffic:")
flt_low = drop_dp[drop_dp["traffic"]=="Low"]
avg_low= round(flt_low["delivery_time_min"].mean(),2)
print(avg_low)
print("Average delivery time for medium traffic: ")
flt_medium = drop_dp[drop_dp["traffic"]=="Medium"]
mediium_avg = round(flt_medium["delivery_time_min"].mean(),2)
print(mediium_avg)
print("Average delivery time for high traffic: ")
flt_hgh = drop_dp[drop_dp["traffic"]=="High"]
High_avg = round(flt_hgh["delivery_time_min"].mean() , 2)
print(High_avg)
print("Longest average delivery time")
max_deli_avg = np.max([avg_low , mediium_avg , High_avg])
print(max_deli_avg)
#task 05 Detect outliers
Q3 = drop_dp["delivery_time_min"].quantile(0.75)
Q1 = drop_dp["delivery_time_min"].quantile(0.25)
IQR = Q3 - Q1

plt.boxplot(drop_dp["delivery_time_min"])
plt.ylabel("Delivery time")
plt.show()
