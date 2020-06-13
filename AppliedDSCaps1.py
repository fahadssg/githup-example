#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Assign the web page url to a variable
html_doc="https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"


# In[3]:


# import the source text of the web page
import requests 
website_url = requests.get(html_doc).text
from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url,'lxml')
print(soup.prettify())


# In[ ]:


# extract the table syntax from the source code of the web page
My_table = soup.find('table',{'class':'wikitable sortable'})
My_table


# In[ ]:


# assign the headers of the table to a vriable
t_headers = My_table.find_all('th')
t_headers


# In[ ]:


# delete the tags from the list values of the header
forbiddenList = ["a", "i"]
tempList = t_headers
sentenceList = [s for s in [''.join(j for j in i if j not in forbiddenList) for i in tempList] if s]
print(sentenceList)


# In[ ]:


# read the table data rows and columns values and assign it to a list woth the headers values
from bs4 import BeautifulSoup
import csv
soup = BeautifulSoup(website_url,'lxml')
table = soup.find("table")
t_headers = sentenceList
output_rows = [t_headers]
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text.strip())
    output_rows.append(output_row)


# In[ ]:


# write the output to csv file
with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


# In[ ]:


# read csv file and assign the data into a dataframe
import pandas as pd
df = pd.read_csv('output.csv')
df.dtypes


# In[ ]:


# rename the headers
df = df.rename(columns={"Postal Code\n": "Postal Code", "Borough\n": "Borough", "Neighborhood\n":"Neighborhood"})
df.dtypes


# In[ ]:


df.head()


# In[ ]:


df.shape


# In[ ]:


# Get names of indexes for which column Age has value 30
indexNames = df[ df['Borough'] == 'Not assigned' ].index
indexNames


# In[ ]:


# Delete these row indexes from dataFrame
df.drop(indexNames , inplace=True)


# In[ ]:


df

