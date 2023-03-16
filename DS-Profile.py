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

import plotly.graph_objects as go

categories = ['Mathematics','Statistics','Computer Science',
              'Machine Learning', 'Communication','Visualization','Domain Expertise']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[6, 7, 2, 7, 6,5,5],
      theta=categories,
      fill='toself',
      name='Product A'
))


fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 10]
    )),
  showlegend=False
)

fig.show()
# In[ ]:




