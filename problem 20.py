
# coding: utf-8

# In[11]:

import math
import numpy as np
import time
start=time.time()
number=str(math.factorial(100))
x=0
for i in np.arange(1,len(number),step=1):
    x=x+int(number[i-1])
    
print('The number is ',x,sep='')
end=time.time()
print('Elapsed time: ',round(end-start,4),'s', sep='')

