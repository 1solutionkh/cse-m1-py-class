import pandas as pd

# Series = 1D labeled array (like a single column)
s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])

print(s)
# a    10
# b    20
# c    30
# d    40

print(s["b"])       # 20    — lookup by label
print(s.iloc[0])    # 10    — lookup by position
print(s.mean())     # 25.0
print(s * 2)        # a 20, b 40, c 60, d 80
