
# coding: utf-8

# # Problem 1

# In[16]:

import os
os.getcwd()


# import numpy for data manipulation and pandas for reading the 'dataframe' into python. time for measuring computing time.

# In[17]:

import numpy as np
import pandas as pd
import time
array=pd.read_csv('p18_help.txt',delimiter=' ',header=None)
type(array)


# no idea why the df was loaded as it was, nevertheless I had to remove the last column

# In[18]:

grid=np.array(array)
grid=np.delete(grid,15,1)
grid.shape


# final for loop. not a rocket science, but the indexes are tricky

# In[24]:

start=time.time()
for i in np.arange(1,grid.shape[0]+1,step=1)[::-1]:
        for j in np.arange(1,grid.shape[0]+1,step=1):
          grid[i-2,j-2]=grid[i-2,j-2]+max(grid[i-1,j-2],grid[i-1,j-1])
      

print('The sum is ',grid[0,0],'.',sep='')
end=time.time()
print('Elapsed time: ',round(end-start,4),'s', sep='')

