import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
inventory = pd.read_csv("Inventory.csv")
weekly_loans = pd.read_csv("weekly_loans.csv")
#task 01
print("============================Inspect the first five rows of each dataframe============================")
print(inventory.head(5))
print(weekly_loans.head(5))
print("============================Checking shapes and data types============================")
print(inventory.shape)
print(inventory.dtypes)
print(weekly_loans.shape)
print(weekly_loans.dtypes)
#Task 02 Analyze borrowing demand
print("============================Group the loans by book_id and calculate sum , avg , max============================")
demand = weekly_loans.groupby(by="book_id").agg(
    total_loans = ("loans" , "sum"),
    avg_loans = ("loans" , "mean"),
    max_loans = ("loans" , "max")
)
print(demand)
#Task 03 Merge the datasets
merge = pd.merge(left=inventory , right=demand , on="book_id" , how="left")
merge[["total_loans" , "avg_loans" , "max_loans"]] = (merge[["total_loans" , "avg_loans" , "max_loans"]].fillna(0))
#task 04 Feature engineering
merge["weeks_of_cover"] = round(merge["current_stock"] / merge["avg_loans"] , 2)
#Task 05 NumPy classification
condition = [merge["current_stock"]==0 , merge["total_loans"]==0 , merge["weeks_of_cover"]<1 , merge["weeks_of_cover"] < 2]
choices = ["out of stock" , "No loan history" , "Reorder now" , "Monitor"]
reorder_status = np.select(condlist=condition , choicelist=choices , default="Healthy")
merge["reorder_status"] = reorder_status
#Task 06 – Data Sorting
print("============================Sort all books by total_loans in descending order============================")
merge_sort = merge.sort_values(by="total_loans" , ascending=False)
print(merge_sort)
print("============================Identify 5 most borrowed books============================")
print(merge_sort.head(5))
print("=========================Identify the 5 least borrowed books============================")
print(merge_sort.tail(5))
merge_sort_cover = merge_sort.sort_values(by="weeks_of_cover" , ascending=True)
print("============================Sort books by weeks_of_cover from lowest to highest============================")
print(merge_sort_cover)
# Task 07 – Risk Analysis
print("=========================Count books in each reorder_status category=========================")
count_book = merge_sort_cover["reorder_status"].value_counts() 
print(count_book)
print("=========================Calculate the percentage of books in each category=========================")
count_book_p = merge_sort_cover["reorder_status"].value_counts(normalize=True)*100
print(count_book_p)
print("=========================Identify all books marked Reorder now=========================")
title = merge_sort_cover.loc[merge_sort_cover["reorder_status"]=="Reorder now" , "title"]
print(title)
print("=========================Identify all books marked out of stock=========================")
out_of_stock = merge_sort_cover.loc[merge_sort_cover["reorder_status"] =="out of stock" , "title"]
print(out_of_stock)
print("=========================Find books with high demand but low stock=========================")
restock_books = merge_sort_cover.loc[(merge_sort_cover["total_loans"] > 10)&(merge["current_stock"] <=5) , "title"]
print(restock_books)
# Task 08 – Statistical Analysis
print("=========================Calculate average current stock=========================")
numpyArray = merge_sort_cover.to_numpy()
current_stock = merge_sort_cover["current_stock"].to_numpy()
avg = np.mean(current_stock)
print("Average: ",avg)
print("Find book with highest total loans")
total_loans = merge_sort_cover["total_loans"].to_numpy()
highest_index = np.argmax(total_loans)
lowest_index = np.argmin(total_loans)
print(merge_sort_cover.iloc[highest_index])
print("=========================Find book with lowest total loans=========================")
print(merge_sort_cover.iloc[lowest_index])
print("=========================Calculate the median borrowing demand=========================")
median_borrow = np.median(total_loans)
print("Median: " , median_borrow)
print("=========================Identify books whose borrowing demand is above average=========================")
above_Avg = merge_sort_cover.iloc[total_loans > avg]
print(above_Avg)
#Task 09 – Business Insights
print("=========================Identify the top 5 books that need restocking=========================")
restock = merge_sort_cover[merge_sort_cover["reorder_status"] == "Reorder now"]
sort_restock_top5 = restock.sort_values(by="weeks_of_cover" , ascending=False).head(5)
print(sort_restock_top5)
print("=========================Find books with zero borrowing history================================")
zero_loans = merge_sort_cover[merge_sort_cover["total_loans"]==0]
print(zero_loans)
print("=========================Identify books with excessive stock but low demand===========================")
low_demand = merge_sort_cover[(merge_sort_cover["total_loans"] < 10 )& (merge_sort_cover["total_loans"] >= 5 )]
print(low_demand)
print("==========================Calculate how many books are healthy=================================")
healthy_book = np.sum(merge_sort_cover["reorder_status"].to_numpy() == "Healthy")
print("Total Helthy books: ",healthy_book)
print("===========================Recommend which books the library should prioritize purchasing================================")
high_demand = restock["title"].to_numpy()
idx = 1
for i in high_demand:
    print(f"{idx}. {i}")
    idx+=1
print("==================================Bar chart showing books by risk category=============================")
plt.figure(figsize=(9,5))
risk_count = merge_sort_cover["reorder_status"].value_counts()
plt.bar(risk_count.index , risk_count.values)
plt.title("Books by risk category")
plt.xlabel("Risk category")
plt.ylabel("Number of books")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
print("============================Top 10 most borrowed books=========================")
top_10 = merge_sort_cover.sort_values(by="total_loans",ascending=False)
plt.figure(figsize=(20,5))
plt.bar(top_10["title"] , top_10["total_loans"] , color = "black")
plt.xlabel("Books title")
plt.ylabel("Total loans")
plt.xticks(rotation = 20)
plt.subplots_adjust(bottom=0.30)
plt.tight_layout()
plt.show()
print("================ INVENTORY RISK DISTRIBUTION ================")

risk_count = merge["reorder_status"].value_counts()

plt.figure(figsize=(8, 8))

plt.pie(
    risk_count.values,
    labels=risk_count.index,
    autopct="%1.1f%%",
)

plt.title("Library Inventory Risk Distribution")

plt.show()