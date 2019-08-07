
# coding: utf-8

# In[17]:

import pandas as pd
import numpy as np


# In[2]:

df = pd.read_csv('/Users/ryanmichels/Downloads/budget_data.csv')


# In[3]:

df.head()


# In[24]:

df.shape


# In[6]:

total_number_months = df['Date'].count()


# In[35]:

net_profit = df['Profit/Losses'].sum()


# In[261]:

diff =0
for i in range(len(df['Profit/Losses'])-1):
    diff += df['Profit/Losses'].iloc[i+1] - df['Profit/Losses'].iloc[i]    
average_changes = diff/85    


# In[262]:

a = []
for i in range(len(df['Profit/Losses'])-1):
    a +=[df['Profit/Losses'].iloc[i+1] - df['Profit/Losses'].iloc[i]]
max(a),min(a)


# In[133]:

a


# In[256]:

def get_greatest_increase(df, answer =0):
    profit_change = df['Profit/Losses'].iloc[1] - df['Profit/Losses'].iloc[0]
    for i in range(len(df)-1):
        if df['Profit/Losses'].iloc[i+1] - df['Profit/Losses'].iloc[i] > profit_change:
            profit_change = df['Profit/Losses'].iloc[i+1] - df['Profit/Losses'].iloc[i]
            answer = i+1
    return answer
            


# In[257]:

get_greatest_increase(df)


# In[251]:

greatest_increase_profits = df['Profit/Losses'].iloc[25] - df['Profit/Losses'].iloc[24]


# In[254]:

def get_greatest_decrease(df, answer =0):
    loss_change = df['Profit/Losses'].iloc[1] - df['Profit/Losses'].iloc[0]
    for i in range(len(df)-1):
        if (df['Profit/Losses'].iloc[i+1]) - (df['Profit/Losses'].iloc[i]) < loss_change:
            loss_change = df['Profit/Losses'].iloc[i+1] - df['Profit/Losses'].iloc[i]
            answer = i+1
    return answer


# In[255]:

get_greatest_decrease(df)


# In[249]:

greatest_decrease_losses = df['Profit/Losses'].iloc[44] - df['Profit/Losses'].iloc[43]


# In[260]:

print("\tFinancial Analysis\n_____________________________________")
print("Total Months: \t ", total_number_months)
print("Total Profits: \t$", net_profit)
print("Average Change: $", round(average_changes,2))
print("Greatest Increase in Profits:", df['Date'].iloc[25],  "($"  ,greatest_increase_profits,")")
print("Greatest Derease in Profits:", df['Date'].iloc[44],  "($"  ,greatest_decrease_losses,")")


# In[ ]:



