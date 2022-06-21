#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 what will be the output of the following python code?
i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i+=1


# In[1]:


#2 what will be the output of the following python code snippet
x=1
x<<2


# In[2]:


#3write the output of the following python code?
l=[1, 0, 2, 0, 'hello', '',[]]
list(filter(bool, l))


# In[3]:


#4 what will be the output of the following python code?
x='abcd'
for i  in x:
    print(i.upper())


# In[4]:


#5 what will be the output of the following python program?
i = 0
while i<5:
    print(i)
    i+=1
    if i == 3:
        break
else:
    print(0)
    


# In[1]:


#1.write a BMI python streamlit program 
import streamlit as st
st.header ("'bmi streamlit'")
st.write('bmi status check')
bmi=st.number_input('BMI in')
if bmi<18.5:
    st.write('low bmi and this puts you in danger zone')
if 25>bmi>18.4:
    st.write('normal bmi')
if 25<bmi:
    st.write('This is considered overweight and a BMI of 30 and higher is considered obesity')
    


# In[ ]:




