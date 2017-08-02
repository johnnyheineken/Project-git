import pandas as pd

f = pd.read_csv('p13.csv', header=None)
s = 0
for i in range(100):
	s += int(f.iloc[i,0])

print(s)
