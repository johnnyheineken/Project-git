
# coding: utf-8

# In[45]:

print('zdarec')
import numpy as np
import math
import time



# In[46]:

start = time.time()
hodne=150000
potential_primes=np.arange(5,hodne, step=2)
primes=np.array([2,3])


for i in potential_primes:
        if( 0 not in (i % primes[math.sqrt(i)>=primes])):
            primes=np.append(primes,i)          
        if len(primes)==10001:
            break
            
print('the number is ' + str(primes[len(primes)-1]))
end = time.time()
print(end - start)


# In[22]:



