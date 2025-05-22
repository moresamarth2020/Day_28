#!/usr/bin/env python
# coding: utf-8

# # For Loop with else in Python
# ### Python - else in Loop
# As you have learned before, the else clause is used along with the if statement. Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.

# In[1]:


for i in range(5):
    print(i)
else:
    print("Sorry no i")


# In[2]:


for i in []:
    print(i)
else:
    print("Sorry no i")


# In[3]:


for i in range (6):
    print(i)
    if i==4:
        break
else:
    print("Sorry no i")


# In[6]:


i=0
while i<7:
    print(i)
    i=i+1
    if i==4:
        break
else:
    print("Sorry no i")


# In[7]:


for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")


# In[ ]:




