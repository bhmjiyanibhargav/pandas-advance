#!/usr/bin/env python
# coding: utf-8

# # question 01
Sure, here are five functions of the pandas library with execution examples:

read_csv() - This function is used to read a CSV (Comma Separated Values) file and convert it into a pandas dataframe.
# In[1]:


import pandas as pd

# Reading a CSV file and creating a pandas dataframe
df = pd.read_csv('data.csv')
print(df.head())

describe() - This function is used to get a summary of the numerical data in a pandas dataframe.
# In[2]:


import pandas as pd

# Creating a pandas dataframe
data = {'Name': ['John', 'Sam', 'Sara', 'Tom'], 'Age': [25, 30, 20, 35], 'Salary': [50000, 60000, 45000, 70000]}
df = pd.DataFrame(data)

# Getting a summary of the numerical data in the dataframe
print(df.describe())

groupby() - This function is used to group a pandas dataframe by one or more columns and apply a function to each group.



# In[3]:


import pandas as pd

# Creating a pandas dataframe
data = {'Name': ['John', 'Sam', 'Sara', 'Tom', 'John'], 'Department': ['Sales', 'IT', 'Sales', 'IT', 'Sales'], 'Salary': [50000, 60000, 45000, 70000, 55000]}
df = pd.DataFrame(data)

# Grouping the dataframe by Department and getting the mean salary for each group
group_data = df.groupby('Department')['Salary'].mean()
print(group_data)

fillna() - This function is used to fill missing values in a pandas dataframe with a specified value or method.
# In[4]:


import pandas as pd
import numpy as np

# Creating a pandas dataframe with missing values
data = {'Name': ['John', 'Sam', 'Sara', 'Tom'], 'Age': [25, np.nan, 20, 35], 'Salary': [50000, 60000, np.nan, 70000]}
df = pd.DataFrame(data)

# Filling missing values in the Age and Salary columns with the mean value of the column
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print(df)

pivot_table() - This function is used to create a pivot table from a pandas dataframe.
# In[5]:


import pandas as pd

# Creating a pandas dataframe
data = {'Name': ['John', 'Sam', 'Sara', 'Tom', 'John'], 'Department': ['Sales', 'IT', 'Sales', 'IT', 'Sales'], 'Salary': [50000, 60000, 45000, 70000, 55000]}
df = pd.DataFrame(data)

# Creating a pivot table to show the mean salary for each Department and Name combination
pivot_data = pd.pivot_table(df, values='Salary', index=['Department'], columns=['Name'], aggfunc=np.mean)
print(pivot_data)


# # question 02
Sure, here's a Python function that takes a Pandas DataFrame df with columns 'A', 'B', and 'C' as input, and re-indexes the DataFrame with a new index that starts from 1 and increments by 2 for each row:
# In[6]:


import pandas as pd

def reindex_df(df):
    # Get the length of the DataFrame
    length = len(df)

    # Create a new index starting from 1 and incrementing by 2
    new_index = range(1, 2 * length, 2)

    # Set the new index on the DataFrame
    df.index = new_index

    # Return the DataFrame with the new index
    return df


# In[7]:


# Creating a sample dataframe
data = {'A': [10, 20, 30, 40], 'B': [100, 200, 300, 400], 'C': [1000, 2000, 3000, 4000]}
df = pd.DataFrame(data)

# Call the function to re-index the DataFrame
new_df = reindex_df(df)

# Print the new DataFrame with the re-indexed rows
print(new_df)


# # question 03

# In[9]:


def sum_first_three_values(df):
    sum = df['Values'].iloc[:3].sum()
    print("Sum of first three values:", sum)

You can pass your DataFrame df to this function, and it will slice the first three values in the 'Values' column using iloc[:3] and calculate their sum using the sum() method. The function then prints the sum to the console.

Note that this assumes that your 'Values' column is a numeric data type. If it's not, you may need to convert it to a numeric type first using the astype() method, like this:
# In[10]:


df['Values'] = df['Values'].astype(float)


# # questiom 04
# 
Q4. Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column
'Word_Count' that contains the number of words in each row of the 'Text' column.
# In[11]:


import pandas as pd

def add_word_count_column(df):
    df['Word_Count'] = df['Text'].apply(lambda x: len(x.split()))
    return df

You can pass your DataFrame df to this function, and it will create a new column called 'Word_Count' that contains the number of words in each row of the 'Text' column. The function uses the apply() method to apply a lambda function to each row of the 'Text' column. The lambda function uses the split() method to split the text into a list of words, and then calculates the length of that list using len(). Finally, the function returns the modified DataFrame.

Note that this function assumes that each row of the 'Text' column contains a string of text that can be split into words using whitespace as a delimiter. If your data is more complex, you may need to modify the function to handle edge cases.
# # question 05
DataFrame.size and DataFrame.shape are both methods of a Pandas DataFrame, but they return different information.

DataFrame.size returns the total number of elements in the DataFrame, which is the product of the number of rows and columns. It is equivalent to DataFrame.shape[0] * DataFrame.shape[1].

DataFrame.shape returns a tuple containing the number of rows and columns in the DataFrame. Specifically, it returns the dimensions of the DataFrame as (number of rows, number of columns).

Here's an example to illustrate the difference between the two methods:
# In[12]:


import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.size)    
print(df.shape)   


# # question 06
To read an Excel file in Pandas, you can use the read_excel() function. This function can read both .xls and .xlsx file formats.

Here's an example code snippet that demonstrates how to use read_excel() to read an Excel file:

python

import pandas as pd

df = pd.read_excel('my_excel_file.xlsx')
In this example, the read_excel() function reads the contents of the Excel file named my_excel_file.xlsx and stores them in a Pandas DataFrame called df. You can then use this DataFrame to manipulate and analyze the data in Python.

You can pass additional arguments to read_excel() to customize its behavior, such as specifying which worksheet to read, skipping rows or columns, or specifying the data types of the columns. For more information, you can consult the Pandas documentation on read_excel().
# # question 07

# In[13]:


import pandas as pd

def extract_username(df):
    df['Username'] = df['Email'].str.split('@').str[0]
    return df

You can pass your DataFrame df to this function, and it will create a new column called 'Username' that contains the username part of each email address. The function uses the str.split() method to split each email address into two parts, separated by the '@' symbol. It then uses the .str[0] indexing to extract the first part (i.e., the username) and store it in the new 'Username' column. Finally, the function returns the modified DataFrame.

Note that this function assumes that each row of the 'Email' column contains a string of text that can be split into two parts using the '@' symbol. If your data is more complex, you may need to modify the function to handle edge cases.
# # question 08

# In[14]:


import pandas as pd

def filter_df(df):
    return df[(df['A'] > 5) & (df['B'] < 10)]

Here, the function filter_df takes a DataFrame df as input and returns a new DataFrame that contains only the rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10.

The boolean indexing condition (df['A'] > 5) & (df['B'] < 10) filters the rows where both conditions are met. The & operator combines the conditions, so only the rows where both conditions are True are selected.
# In[15]:


df = pd.DataFrame({'A': [3, 8, 6, 2, 9],
                   'B': [5, 2, 9, 3, 1],
                   'C': [1, 7, 4, 5, 2]})
                   
filtered_df = filter_df(df)


# # question 09

# In[16]:


import pandas as pd

def calculate_stats(df):
    mean = df['Values'].mean()
    median = df['Values'].median()
    std_dev = df['Values'].std()
    return mean, median, std_dev
df = pd.DataFrame({'Values': [1, 2, 3, 4, 5]})
mean, median, std_dev = calculate_stats(df)
print('Mean:', mean)
print('Median:', median)
print('Standard Deviation:', std_dev)


# # question 10

# In[17]:


import pandas as pd

def add_moving_average(df):
    ma_column = df['Sales'].rolling(window=7, min_periods=1).mean()
    df['MovingAverage'] = ma_column
    return df
df = pd.DataFrame({'Sales': [10, 20, 15, 25, 30, 20, 25, 35, 40, 30],
                   'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05',
                            '2022-01-06', '2022-01-07', '2022-01-08', '2022-01-09', '2022-01-10']})
df['Date'] = pd.to_datetime(df['Date'])
df = add_moving_average(df)
print(df)


# # question 11

# In[18]:


import pandas as pd

def add_weekday(df):
    df['Weekday'] = df['Date'].dt.strftime('%A')
    return df
df = pd.DataFrame({'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']})
df['Date'] = pd.to_datetime(df['Date'])
df = add_weekday(df)
print(df)


# # question 12
# 

# In[19]:


import pandas as pd

def select_dates(df):
    start_date = pd.Timestamp('2023-01-01')
    end_date = pd.Timestamp('2023-01-31')
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    selected_df = df.loc[mask]
    return selected_df
df = pd.DataFrame({'Date': ['2023-01-01', '2023-01-15', '2023-02-01', '2023-02-15']})
df['Date'] = pd.to_datetime(df['Date'])
selected_df = select_dates(df)
print(selected_df)


# # question 13 
Q13. To use the basic functions of pandas, what is the first and foremost necessary library that needs to
be imported?The first and foremost necessary library that needs to be imported to use the basic functions of pandas is pandas itself.

To import pandas, you can use the following code:


import pandas as pd

The pd alias is a common convention used to make it easier to refer to the pandas library throughout your code. Once imported, you can use various functions and classes from the pandas library to create, manipulate, and analyze DataFrames and Series.
# In[ ]:




