import pandas as pd
import numpy as np
s = pd.Series([1,3,6,np.nan,44,1])

dates = pd.date_range('20181101',periods=6)
df = pd.DataFrame(np.random.randn(6,5),index=dates,columns=['a','b','c','d','e'])
#index为行，columns为列
print(df)
pf1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(pf1)
df2 = pd.DataFrame({
    'A':1.,'B':pd.Timestamp('20181101'),
    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
    'D':np.array([3]*4,dtype='int32'),
    'E':pd.Categorical(["test","train","test1","train"]),
    'F':'foo'})

print(df2,'\n')
print(df2.dtypes,'\n')
print(df2.index,'\n')
print(df2.values,'\n')
print(df2.describe,'\n')
print(df2.T,'\n')#转置
print(df2.sort_index(axis=1,ascending=False),'\n')
#排序，axis=0对列排序，0行排序；False倒序
print(df2.sort_values(by='E'))
