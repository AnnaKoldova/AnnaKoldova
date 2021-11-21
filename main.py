import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#upload CSV file
sales = pd.read_csv(r"C:\Users\ak240\Desktop\Data Analytics Course\Salesstore.csv")
print(sales.shape)
print(sales.head(10))

#filtering
print(sales['Ship_Mode'] == 'Express Air')
filt = (sales['Ship_Mode'] == 'Express Air')
print(sales[filt])

print(sales['Ship_Mode'] == 'Regular Air')
filt2 = (sales['Ship_Mode'] == 'Regular Air')
print(sales[filt2])

print(sales.loc[sales['Customer_Segment'] == 'Corporate'])
print(sales.loc[(sales['Customer_Segment'] == 'Corporate')
                & (sales['Ship_Mode'] == 'Express Air')
                & (sales['Order_Quantity'] >= 0)])
#groupes most common

from itertools import combinations
from collections import Counter

count = Counter()
for row in sales['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 2)))

for key, value in count.most_common():
    print(key, value)
#group by
print(sales.groupby(['Region']).count())

#duplicates

print(sales[sales['Order_ID'].duplicated(keep=False)])
sales['Grouped'] = sales.groupby('Order_ID')['Product_Category'].transform(lambda x: ','.join(x))
sales = sales[['Order_ID', 'Grouped']].drop_duplicates()
print(sales)

plot_11=sns.regplot(data=sales,x='Sales',y='Profit')
plt.show()

#visualisation

plot_1 = sns.histplot(data=sales, x='Ship_Mode')
plt.show()

plot_2 = sns.histplot(data=sales, x='Customer_Segment')
plt.show()

plot_3 = sns.histplot(data=sales, x='Product_Category')
plt.show()

plot_4 = sns.histplot(data=sales, x='Product_Container')
plt.show()

plot_5 = sns.barplot(data=sales, x='Region', y='Profit', hue='Ship_Mode')
plt.xticks(rotation=45)
plt.show()

plot_6 = sns.barplot(data=sales, x='Region', y='Sales', hue='Ship_Mode')
plt.xticks(rotation=45)
plt.show()

plot_7 = sns.barplot(data=sales, x='Region', y='Profit', hue='Customer_Segment')
plt.xticks(rotation=45)
plt.show()

plot_8 = sns.barplot(data=sales, x='Region', y='Profit', hue='Product_Category')
plt.xticks(rotation=45)
plt.show()








