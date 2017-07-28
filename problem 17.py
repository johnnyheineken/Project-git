
# coding: utf-8

# # problem 17

# #### description
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# 
# 
# ######
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

# In[109]:

#how to generate the words
#lets use dictionaries
#111-119
import numpy as np
import sys
import time
#dictionaries
units={0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
tens={0:'',1:'ten',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
teens={10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}

start=time.time()
words=np.array(['onethousand'])

#from one to hundred
for number in np.arange(1,100,step=1):
    if len(str(number))==1:
        words=np.append(words,units[number])
    else: 
        if int(str(number)[0])==1:
            words=np.append(words,teens[int(str(number)[0:2])])
        else:   
            words=np.append(words,tens[int(str(number)[0])])
            words=np.append(words,units[int(str(number)[1])])
     
 
        
#from one hundred to one thousand
for number in np.arange(100,1000,step=1):
        if int(str(number)[1])==1:
            words=np.append(words,units[int(str(number)[0])])
            words=np.append(words,'hundred')
            words=np.append(words,'and' + teens[int(str(number)[1:3])])
        else:
            if int(str(number)[1])==0 and int(str(number)[2])==0:
               words=np.append(words,units[int(str(number)[0])])
               words=np.append(words,'hundred') 
            else:
             words=np.append(words,units[int(str(number)[0])])
             words=np.append(words,'hundred')
             words=np.append(words,'and' + tens[int(str(number)[1])])
             words=np.append(words,units[int(str(number)[2])])

           
x=0          
for i in np.arange(1,len(words)+1,step=1) :
    x=x+len(words[i-1])
    
    
print('The number of letters is ', x,'.',sep='')
end=time.time()
print('Elapsed time: ',end-start,'.',sep='')

