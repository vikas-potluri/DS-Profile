#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
Title:  Data Science Profile
Author: Sai vikas potluri
Description:  This code generates your Data Science profile plot as described in 
"Doing Data Science" by Cathy O'Neil and Rachel Schutt.
Feel free to contact me with any questions, suggestions, or corrections!
Email: vikaschowdhury.p@gmail.com
"""

import time
import pandas as pd
import os
import matplotlib.pyplot as plt

# Today's date
date = (time.strftime("%Y-%m-%d"))

# Your info goes here.
name = 'Sai Vikas Potluri' # Put your name here.
bar_data_labels = ['Mathematics', 'Statistics', 'Computer Science', 'Machine Learning', 'Communication', 'Visualization', 'Domain Expertise'] # These are the Data Science areas suggested in Doing Data Science.
bar_data = [60, 70, 30, 70, 60, 50, 50] # Rate each skill from 0 to 100. 
bar_data = pd.DataFrame(bar_data) # Put your data into a dataframe

# Create directory for Data Science profile
if not os.path.exists("%s_Data_Science_Profile" % name):
    os.makedirs("%s_Data_Science_Profile" % name)

# Create the plot
bar_data.plot(kind='bar', ylim=[0,100], legend=False, figsize=[20,10]).set_xticklabels(labels=bar_data_labels, rotation=0, fontsize=14)
plt.title("%s's Data Science Profile on %s" % (name, date), fontsize=20)
plt.xlabel('Skill', fontsize=18)
plt.ylabel("Rating (0 to 100)", fontsize=18)
plt.savefig('%s_Data_Science_Profile/%s_Data_Science_Profile_%s.png' % (name, name, date))  # Save the plot within a folder in your working directory


# In[ ]:




