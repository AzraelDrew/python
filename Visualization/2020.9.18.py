'''
 $ @Author       : yznaisy
 $ @Date         : 2020-09-18 09:34:49
 $ @LastEditors  : yznaisy
 $ @LastEditTime : 2020-09-18 11:45:25
'''
import pandas as pd
import numpy as np
# s = pd.Series([1, 3, 5, np.nan, 7, 8])
# print(s)


dates = pd.date_range("20130101", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

# df2 = pd.DataFrame({'A': 1.,
#                     'B': pd.Timestamp('20130102'),
#                     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
#                     'D': np.array([3] * 4, dtype='int32'),
#                     'E': pd.Categorical(["test", "train", "test", "train"]),
#                     'F': 'foo'})
# print(df2)
# print(df2.dtypes)
# print(df2.A)


print(df.head(2))
print(df.tail(2))
print(df.index)
print(df.columns)
print(df.to_numpy())
