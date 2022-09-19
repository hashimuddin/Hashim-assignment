#!/usr/bin/env python
# coding: utf-8

# In[227]:


import numpy as np
import pandas as pd


# In[219]:


# Answer-1 
data = pd.read_csv(r"C:\Users\Hashim Uddin\Downloads\Plantix_Case_Study 17-9-22\sales_orders.csv")
data['Data_N'] = pd.to_datetime(data['creation_time'])
data['Data_N'].dt.year
data1 = pd.read_csv(r"C:\Users\Hashim Uddin\Downloads\Plantix_Case_Study 17-9-22\sales_orders_items.csv")
data1.rename(columns={'fk_order_id':'order_id'},inplace=True)
data2 = data.merge(data1,on=['order_id'])
data2["Year"] = data2.Data_N.dt.year
print(data2)
# There are various KPIs measure the performance of our app.
# 1. order_id - How are your people contributing to the expansion of your business in their given territory.
# 2. sales_order_status - Its clearly show the order is Rejected or shipped so its very important to bussiness.
# 3. order_quantity_accepted - Its clearly shows the accepted quantiy as quantity and shows 0 for rejected item of every order.
# 4. rate - rate plays the most important role of any bussiness. all growth and criaterias depands on the rate of products.


# In[220]:


# Answer -2(a) - 
data = pd.read_csv(r"C:\Users\Hashim Uddin\Downloads\Plantix_Case_Study 17-9-22\sales_orders.csv")
data['Data_N'] = pd.to_datetime(data['creation_time'])
data['Data_N'].dt.year
data1 = pd.read_csv(r"C:\Users\Hashim Uddin\Downloads\Plantix_Case_Study 17-9-22\sales_orders_items.csv")
data1.rename(columns={'fk_order_id':'order_id'},inplace=True)
data2 = data.merge(data1,on=['order_id'])
data2["Year"] = data2.Data_N.dt.year
data3 = data2.groupby(["fk_product_id","Year"])['order_quantity_accepted'].sum().to_frame()
data6 = data3.groupby(['Year'])['order_quantity_accepted'].sum()
print("Customers accepted orders quantity in each year")
print(data6)


# Above mentioned "data4" Output clearly shows the 'order_qunatity_accepted' in Year 2022 by customers is increase as compared to Year 2021
# So our bussiness is grow till july 2022.


# In[221]:


#Answer - 2(b)-
data = pd.read_csv(r"C:\Users\Hashim Uddin\Downloads\Plantix_Case_Study 17-9-22\sales_orders.csv")
data['Data_N'] = pd.to_datetime(data['creation_time'])
data['Data_N'].dt.year
data1 = pd.read_csv(r"C:\Users\Hashim Uddin\Downloads\Plantix_Case_Study 17-9-22\sales_orders_items.csv")
data1.rename(columns={'fk_order_id':'order_id'},inplace=True)
data2 = data.merge(data1,on=['order_id'])
data2["Year"] = data2.Data_N.dt.year
data3 = data2.groupby(["fk_product_id","Year"])['order_quantity_accepted'].sum().to_frame()
data6 = data3.groupby(['Year'])['order_quantity_accepted'].sum()
print("Customers accepted orders quantity in each year",data6)

data8 = data2.groupby(['Year'])['order_id'].count().to_frame()
print("Total number of Oreders in each years ",data8)
#Point-1   - Above mentioned "data6" Output clearly shows the 'order_qunatity_accepted' in Year 2022 by customers is increase as compared to Year 2021
# So our "app is perform really well" till July 2022.

#Point-2   - Above mention "data8" Output clearly shows the number of "order_id/number of orders" is increase in Year 2022 as compared to Year 2021 
# So our "app is perform really well" till July 2022.


# In[222]:


# Answer 2(c)
data = pd.read_csv(r"C:\Users\Hashim Uddin\Downloads\Plantix_Case_Study 17-9-22\sales_orders.csv")
data['Data_N'] = pd.to_datetime(data['creation_time'])
data['Data_N'].dt.year
data1 = pd.read_csv(r"C:\Users\Hashim Uddin\Downloads\Plantix_Case_Study 17-9-22\sales_orders_items.csv")
data1.rename(columns={'fk_order_id':'order_id'},inplace=True)
data2 = data.merge(data1,on=['order_id'])
data2["Year"] = data2.Data_N.dt.year

data8 = data2.groupby(['Year'])['order_id'].count().to_frame()
print("Total number of orders in each years ")
print(data8)
# Above mention answer clearly shows the number of "order_id/number of orders" is increase in Year 2022 
# as compared to Year 2021 so Our "User base" is growing till July 2022.


# In[223]:


# Answer - 3
data = pd.read_csv(r"C:\Users\Hashim Uddin\Downloads\Plantix_Case_Study 17-9-22\sales_orders.csv")
data['Data_N'] = pd.to_datetime(data['creation_time'])
data['Data_N'].dt.year
data1 = pd.read_csv(r"C:\Users\Hashim Uddin\Downloads\Plantix_Case_Study 17-9-22\sales_orders_items.csv")
data1.rename(columns={'fk_order_id':'order_id'},inplace=True)
data2 = data.merge(data1,on=['order_id'])
data2["Year"] = data2.Data_N.dt.year
data3 = (data2.groupby(['fk_product_id','Year'])['order_quantity_accepted'].sum().to_frame())
data4 = data3.loc[data3.groupby(['Year'])['order_quantity_accepted'].idxmax()] 
data5 = data3.loc[data3.groupby(['Year'])['order_quantity_accepted'].idxmax()] # Answer -3

print("Top selling products in each Years")
print(data5)

# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


# Creating dataset
z = [2021,2022]
x = [10235,12547]
y = [1045,1572]

# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")

# Creating plot
ax.scatter3D(x, y, z, color = "green")
plt.title("simple 3D scatter plot")

# show plot
plt.show()

# Answer 3=> Above mention "data5" output clearly shows the "product/fk_product_id" no. 10235 is a maximum selling product in Year 2021 
# And "product/fk_product_id" no. 12547 is a maximum selling product in Year 2022.
# Also drow the 3D graph between order_quantity_accepted,fk_product_id, Year .


# In[225]:


# Answer - 4
data2
data10 = data2[data2.Year.isin([2021])]
data11 = data10.groupby(["order_id"])['ordered_quantity','order_quantity_accepted'].sum()
Difference_Percentage = (((data11.order_quantity_accepted) / (data11.ordered_quantity))*100)
print("Order_Id's have 0 delivery rates ")
print(Difference_Percentage[Difference_Percentage.isin([0])])
# Our biggest concerned for Year 2021. So we should look over these order_id as these have 0 delivery rates.


# In[226]:


# Answer - 5
login = pd.read_csv(r"C:\Users\Hashim Uddin\Downloads\Plantix_Case_Study 17-9-22\login_logs.csv")
login['Data_N'] = pd.to_datetime(login['login_time'])
login
login.dtypes
login.rename(columns={'user_id':'fk_buyer_id'},inplace=True)
login1 = data2.merge(login,on=['fk_buyer_id'])
login2 = (login1.login_time)<(login1.creation_time)
login2.head(2)
login2.size
login1.size
login3 = login1.size - login2.size
login4 = ((login2.size)/(login1.size))*100

print("Orders is affected by the login frequency",login4)
# So 6.66666% orders is affected by the login frequency.


# In[ ]:





# In[ ]:





# In[9]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[79]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[69]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




