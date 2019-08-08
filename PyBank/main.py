
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np


# In[3]:

df = pd.read_csv('/Users/ryanmichels/Downloads/budget_data.csv')


# In[4]:

df.head()


# In[5]:

df.shape


# In[6]:

total_number_months = df['Date'].count()


# In[7]:

net_profit = df['Profit/Losses'].sum()


# In[8]:

diff =0
for i in range(len(df['Profit/Losses'])-1):
    diff += df['Profit/Losses'].iloc[i+1] - df['Profit/Losses'].iloc[i]    
average_changes = diff/85    


# In[9]:

a = []
for i in range(len(df['Profit/Losses'])-1):
    a +=[df['Profit/Losses'].iloc[i+1] - df['Profit/Losses'].iloc[i]]
max(a),min(a)


# In[10]:

a


# In[11]:

def get_greatest_increase(df, answer =0):
    profit_change = df['Profit/Losses'].iloc[1] - df['Profit/Losses'].iloc[0]
    for i in range(len(df)-1):
        if df['Profit/Losses'].iloc[i+1] - df['Profit/Losses'].iloc[i] > profit_change:
            profit_change = df['Profit/Losses'].iloc[i+1] - df['Profit/Losses'].iloc[i]
            answer = i+1
    return answer
            


# In[12]:

get_greatest_increase(df)


# In[13]:

greatest_increase_profits = df['Profit/Losses'].iloc[25] - df['Profit/Losses'].iloc[24]


# In[14]:

def get_greatest_decrease(df, answer =0):
    loss_change = df['Profit/Losses'].iloc[1] - df['Profit/Losses'].iloc[0]
    for i in range(len(df)-1):
        if (df['Profit/Losses'].iloc[i+1]) - (df['Profit/Losses'].iloc[i]) < loss_change:
            loss_change = df['Profit/Losses'].iloc[i+1] - df['Profit/Losses'].iloc[i]
            answer = i+1
    return answer


# In[15]:

get_greatest_decrease(df)


# In[16]:

greatest_decrease_losses = df['Profit/Losses'].iloc[44] - df['Profit/Losses'].iloc[43]


# In[44]:

print("\tFinancial Analysis\n_____________________________________")
print("Total Months: \t ", total_number_months)
print("Total Profits: \t$", net_profit)
print("Average Change: $", round(average_changes,2))
print("Greatest Increase in Profits:", df['Date'].iloc[25],  "($"  ,greatest_increase_profits,")")
print("Greatest Derease in Profits:", df['Date'].iloc[44],  "($"  ,greatest_decrease_losses,")")


# In[45]:

file = open("test.txt", "w") 
file.write("Financial Analysis" + "\n") 
file.write("_____________________________________\n") 
file.write("Total Months: {}\n".format(total_number_months)) 
file.write("Total Profits:  ${}\n".format(net_profit)) 
file.write("Average Change:  ${}\n".format(round(average_changes,2))) 
file.write("Greatest Increase in Profits:  {} (${})\n".format(df['Date'].iloc[25],greatest_increase_profits)) 
file.write("Greatest Decrease in Profits:  {} (${})".format(df['Date'].iloc[44],greatest_decrease_losses)) 
 
file.close() 


# In[ ]:



