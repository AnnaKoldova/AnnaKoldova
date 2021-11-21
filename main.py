import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#upload CSV file
sales = pd.read_csv(r"C:\Users\ak240\Desktop\Data Analytics Course\Salesstore.csv")
print(sales.shape)
print(sales.head(10))

print(sales['Ship_Mode'] == 'Express Air')
filt = (sales['Ship_Mode'] == 'Express Air')
print(sales[filt])

print(sales['Ship_Mode'] == 'Regular Air')
filt2 = (sales['Ship_Mode'] == 'Regular Air')
print(sales[filt2])

