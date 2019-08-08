
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np


# In[3]:

ed = pd.read_csv('/Users/ryanmichels/Downloads/election_data.csv')


# In[4]:

ed.head()


# In[5]:

total_number_votes = ed['Voter ID'].count()


# In[6]:

list_of_candidates = ed['Candidate'].value_counts()


# In[7]:

candidates =ed['Candidate'].unique()


# In[8]:

list_of_candidates


# In[9]:

khan_votes = ed[ed['Candidate']=='Khan'].count()


# In[10]:

khan_percentage = round((khan_votes/total_number_votes)*100,2)


# In[11]:

correy_votes = ed[ed['Candidate']=='Correy'].count()


# In[12]:

correy_percentage = round((correy_votes/total_number_votes)*100,2)


# In[13]:

li_votes = ed[ed['Candidate']=='Li'].count()


# In[14]:

li_percentage = round((li_votes/total_number_votes)*100,2)


# In[15]:

otooley_votes = ed[ed['Candidate']=='O\'Tooley'].count()


# In[16]:

otooley_percentage = round((otooley_votes/total_number_votes)*100,2)


# In[17]:

winner = 'Khan'


# In[18]:

print('Election Results')
print('_________________')
print('Total Votes: ', total_number_votes)
print('_________________')
print(candidates[0], ":",khan_percentage.values[0],"%", "(", khan_votes.values[0], ")")
print(candidates[1], ":",correy_percentage.values[0],"%", "(", correy_votes.values[0], ")")
print(candidates[2], ":",li_percentage.values[0],"%", "(", li_votes.values[0], ")")
print(candidates[3], ":",otooley_percentage.values[0],"%", "(", otooley_votes.values[0], ")")
print('_________________')
print("Winner:", winner)
print('_________________')


# In[33]:

file = open("Election Results.txt", "w") 

file.write("Election Results" + "\n")
file.write("_____________________________________\n")
file.write("Total Votes: {}\n".format(total_number_votes))
file.write("_____________________________________\n")
file.write("{}: {}% ({})\n".format(candidates[0], khan_percentage.values[0], khan_votes.values[0]))
file.write("{}: {}% ({})\n".format(candidates[1], correy_percentage.values[0], correy_votes.values[0]))
file.write("{}: {}% ({})\n".format(candidates[2], li_percentage.values[0], li_votes.values[0]))
file.write("{}: {}% ({})\n".format(candidates[3], otooley_percentage.values[0], otooley_votes.values[0]))
file.write("_____________________________________\n")
file.write("Winner:{}\n".format(winner))
file.write("_____________________________________\n")

file.close() 


# In[ ]:



