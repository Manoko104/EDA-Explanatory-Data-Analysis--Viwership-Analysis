import pandas as pd
# is a powerful Python library used for data manipulation, analysis, and handling structured data (like Excel files, CSVs, SQL tables, etc.).
#it provides data structure like dataframe and pd is an alias name

import numpy as np
# NumPy is a Python library mainly used for:
#Working with arrays (like supercharged lists, beacuse the can do powerful operation and complicated

#EDA (Explanatory Data Analyst)
#Meta Data

!pip install openpyxl -q
# this tells pyhton to install openpyxl packages anf in a quiet mode
# this will alow us to read from and write to excel files


import pandas as pd
#Pandas is a Python package used for data analysis and manipulation (especially tables, spreadsheets, CSV files, databases, etc.) and data cleaning and preparation. PD is a shortcut for pandas to make it easy for one code.
import numpy as np
#NumPy (Numerical Python) is a Python library mainly used for:
#Working with arrays (like supercharged lists, beacuse the can do powerful operation and complicated calculations).
#Doing mathematical operations (e.g., averages, sums, square roots, linear algebra).
#Handling large datasets quickly and efficiently

#Location of the data file
data_path="/Workspace/Users/regina.kabe@gmail.com/Viewership Analysis .xlsx"
# importing data from different sources (files, databases, APIs, streaming,excel or csv etc.).
# The process is called data ingestion/ load
# Question can import a PDF into pandas?Directly, No but with the right tools yes you can..
# If the PDF contains the tables  by usuing extra libraries (1)import tabula # Extract tables from PDF into a list of DataFrames
# (2) import camelot # Extract tables
# (3) If it’s text-based PDF (not tables) → you’d need to use libraries like PyPDF2 or pdfplumber to extract text, then parse/clean it into a pandas DataFrame

survey_analysis = pd.read_excel(data_path)
#for reading an excel file 

# display data
# astype converts all values in that column to the string data type (text).
# df["VideoTitle"] = ... → saves those converted values back into the same column.
# This ensures the entire VideoTitle column is treated as text.
survey_analysis["VideoTitle"] = survey_analysis["VideoTitle"].astype(str)
display(survey_analysis)

survey_analysis.shape
#It is a quick way of showing the number of rows and columns in a dataset.(e.g)To know how big your data is .

survey_analysis.dtypes
# this show the data type of each column, it is a useful way of understanding your data and avoid errors when you start analysing it.

survey_analysis.columns
# This shows the column names of the dataset
#Helpful for structuring your data and useful for checking column names before accessing or renaming them

survey_analysis.info()
# this gives summary of the data, including the number of rows, columns, data types, and memory usage.
# to understand the size of your data and missing data, as well as the data types of each column, before doing the calculations
survey_analysis.describe()
#EDA (Explanatory Data Analyst)

survey_analysis['Platform'].unique()
# function is used to find all the unique (distinct) values in a Series or column.

survey_analysis[['Platform','DateID','TotalTimeWatched','PlayEventType','VideoTitle']].apply(pd.Series.unique)
# this returns all the unique values in each column of the DataFrame.
# This is useful for understanding the distribution of values in each column and identifying any potential issues with data quality or consistency.

survey_analysis['Platform'].value_counts()
# checks how many times each unique value appears in the 'Platform' column.
# This is useful for understanding the distribution of values in the column and identifying any potential issues with data quality or consistency.
survey_analysis['Platform'].value_counts().plot.bar()


survey_analysis['Platform'].value_counts()
# checks how many times each unique value appears in the 'Platform' column.
# This is useful for understanding the distribution of values in the column and identifying any potential issues with data quality or consistency.
survey_analysis['Platform'].value_counts().plot.bar()

survey_analysis['TotalTimeWatched'].max()
# used to find the largest value

survey_analysis['TotalTimeWatched'].min()
# used to find the smallest value


survey_analysis['TotalTimeWatched'].mean()
# used to calculate the average value of number in a colums or across rows

survey_analysis.duplicated().sum()
# used to calculate total sum of values in a column(or rows)

survey_analysis.drop_duplicates(inplace=True)
# used to remove duplicate values in a column or rows

# inplace=True → means it changes the DataFrame directly instead of creating a new one.


survey_analysis.duplicated().sum()
# used to calculate total sum of values in a column(or rows)
survey_analysis['TotalTimeWatched'].sum()
# used to calculate

survey_analysis.describe()
# It generates the summary statistic of the dataset and gives a quick overview of the data.

survey_analysis.isnull().sum()
# this gives the total number of null values in each column

survey_analysis['CustomerID'].nunique()
# this gives the unique values in the column

survey_analysis['CustomerID'].unique()
# the actual list of distinct values in the column


survey_analysis.value_counts()
# this checks how ofeten does each value occurs

pd.value_counts(survey_analysis['Platform']).plot.bar()
# this shows the number of times each value occurs and plots it

survey_analysis.groupby('PlayEventType').mean()
# this is when you want to see the avarage of a column based on a specific  column
# here i wanted to see the average time watched based on the play event type


survey_analysis.groupby('Platform').mean()
# here was check the average time watched based on the platform


survey_analysis.groupby('VideoTitle').mean()
# here was check the average time watched based on the video title

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

# Count the number of shows watched per platform
platform_counts = (
    survey_analysis.groupby('Platform')
    .size()
    .sort_values(ascending=False)
)

# Plot the pie chart
platform_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(6, 6),
    startangle=90,
    title="Distribution of shows watched by platform"
)

plt.ylabel("")
plt.show()


survey_analysis[survey_analysis['TotalTimeWatched']<300].groupby(['Platform','VideoTitle']).mean()
# the average of whic vidoes are watched in less than 300 total watched time based on the platform

survey_analysis[survey_analysis['TotalTimeWatched']>300].groupby(['Platform','VideoTitle']).mean()
# the average of whic vidoes are watched in more than 300 total watched time based on the platform

