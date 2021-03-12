#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'months since the last donation':2, 'total number of donation':24, 'total blood donated in c.c.':6000, 'months since the first donation':7})

print(r.json())

