# 1. Print the file Fruits.csv

with open("fruits.csv", "r", encoding="utf-8") as file:
    print(file.read())

# 2. Print the same file with csv (delimiter default is ",")

import csv #(if not done before)
with open("fruits.csv", "r", newline = "", encoding="utf-8") as file:
    csv_rows = csv.reader(file, delimiter = "-")
    
    for row in csv_rows :
        print(row)

# 3. Print the same file with pandas

import pandas as pd #(if not done before)
text = pd.read_csv("fruits.csv", sep = ",", index_col = 0)
text


    
