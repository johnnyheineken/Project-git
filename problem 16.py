
# coding: utf-8

# #problem 16

# In[19]:

import numpy as np
a=str((2**1000))
x=0



for i in np.arange(1,len(a)+1, step=1):
        x=x+int(a[i-1])

print('the number we are looking for is ', x)

