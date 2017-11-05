
# coding: utf-8

# In[1]:

import numpy as np
import time



# In[2]:



days=np.array([])
print(days)

year_stand=np.array(["A","C","A","B","A","B","A","A","B","A","B","A"])
year_leap=np.array(["A","D","A","B","A","B","A","A","B","A","B","A"])


i=1901                  
while i < 2001:
    if (i % 4 == 0 and (i % 100 !=0 or i % 400 == 0)):
        days=np.append(days,year_leap)
    else:
        days=np.append(days,year_stand)
    
    i=i+1
    
print(days)
print(len(days))
sum(days=='D')


# In[3]:

days_no=np.array([])
print(len(days))
for i in np.arange(1,len(days)+1,step=1):
    if days[i-1]=='A':
        days_no=np.append(days_no,np.arange(1,32,step=1))
    else:
        if days[i-1]=='B':
            days_no=np.append(days_no,np.arange(1,31,step=1))
        else:
            if days[i-1]=='C':
                days_no=np.append(days_no,np.arange(1,29,step=1))
            else:
                if days[i-1]=='D':
                    days_no=np.append(days_no,np.arange(1,30,step=1))
                else: print('shoot yourself')
                
print(len(days_no))
print(days_no)



# In[4]:

weeks=(np.array([2,3,4,5,6,7,1]))

print(len(days_no))
for i in np.arange(1,len(days_no)/7,step=1):
 weeks = np.append(weeks,(np.array([2,3,4,5,6,7,1])))

weeks=weeks[0:len(days_no)]


# In[6]:

true_weeks=(weeks==7)
true_days=(days_no==1)

print(true_days & true_weeks)
suma=sum(true_days & true_weeks)
print('The number we are looking for is ',suma,'.',sep='')


