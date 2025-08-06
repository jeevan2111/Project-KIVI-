#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install matplotlib seaborn --quiet')


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Customer Churn.csv')
df.head()


# In[3]:


df.info()


# In[4]:


df["TotalCharges"] = df["TotalCharges"].replace(" ","0")
df["TotalCharges"] = df["TotalCharges"].astype("float")


# In[5]:


df.info()


# In[6]:


df.isnull().sum().sum()


# In[7]:


df.describe()


# In[8]:


df["customerID"].duplicated().sum()


# In[9]:


# converted 0 and 1 values of senior citizen to yes/no to make it easier to understand
def conv(value):
    if value == 1:
        return "yes"
    else:
        return "no"

df['SeniorCitizen'] = df["SeniorCitizen"].apply(conv)


# In[10]:


# Pie chart showing exact number of customers who churned vs. stayed
ax = sns.countplot(x = 'Churn', data = df)
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Churn")
plt.show()


# In[11]:


#from the given pie chart we can conclude that 26.54% of our customers have churned out.
plt.figure(figsize = (3,4))
gb = df.groupby("Churn").agg({'Churn':"count"})
plt.pie(gb['Churn'], labels = gb.index, autopct = "%1.2f%%")
plt.title("Percentage of Churned Customeres", fontsize = 10)
plt.show()


# In[12]:


# Around 28% of females and 26% of males churned — not a big difference, so gender likely doesn't affect churn much
plt.figure(figsize = (6,5))
ax = sns.countplot(x = "gender", data = df, hue = "Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Churn by Gender (with Count)")
plt.show()


# In[13]:


plt.figure(figsize = (4,4))
ax = sns.countplot(x = "SeniorCitizen", data = df)
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Senior Citizen")
plt.show()


# In[14]:


total_counts = df.groupby('SeniorCitizen')['Churn'].value_counts(normalize=True).unstack() * 100

# Plot
fig, ax = plt.subplots(figsize=(10, 4))  # Adjust figsize for better visualization

# Plot the bars
total_counts.plot(kind='bar', stacked=True, ax=ax, color=['#1f77b4', '#ff7f0e'])  # Customize colors if desired

# Add percentage labels on the bars
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    ax.text(x + width / 2, y + height / 2, f'{height:.1f}%', ha='center', va='center')

plt.title('Churn by Senior Citizen (Stacked Bar Chart)')
plt.xlabel('SeniorCitizen')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=0)
plt.legend(title='Churn', bbox_to_anchor = (0.9,0.9))  # Customize legend location

plt.show()


# #### comparative a greater pecentage of people in senior citizen category have churned
# 

# In[15]:


plt.figure(figsize = (9,4))
sns.histplot(x = "tenure", data = df, bins = 72, hue = "Churn")
plt.show()


# #### people who have used our services for a long time have stayed and people who have used our sevices 1 or 2 months have churned
# 

# In[16]:


plt.figure(figsize = (7,4))
ax = sns.countplot(x = "Contract", data = df, hue = "Churn")
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Contract")
plt.show()


# #### people who have month to month contract are likely to churn then from those who have 1 or 2 years or contract. 
# 

# In[17]:


df.columns.values


# In[18]:


columns = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 
           'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

# Number of columns for the subplot grid (you can change this)
n_cols = 3
n_rows = (len(columns) + n_cols - 1) // n_cols  # Calculate number of rows needed

# Create subplots
fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, n_rows * 4))  # Adjust figsize as needed

# Flatten the axes array for easy iteration (handles both 1D and 2D arrays)
axes = axes.flatten()

# Iterate over columns and plot count plots
for i, col in enumerate(columns):
    sns.countplot(x=col, data=df, ax=axes[i], hue = df["Churn"])
    axes[i].set_title(f'Count Plot of {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Count')

# Remove empty subplots (if any)
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()


# ### PhoneService
# - Most customers have phone service.
# - Customers with phone service show higher churn than those without.
# 
# ### MultipleLines
# - Customers with multiple lines tend to churn more.
# - Those with no phone service churn the least.
# 
# ### InternetService
# - Fiber optic users have the highest churn rate.
# - DSL users churn less.
# - No internet service = very low churn.
# 
# ### OnlineSecurity
# - Customers without online security churn much more.
# - Online security helps reduce churn.
# 
# ### OnlineBackup
# - No online backup → higher churn.
# - Backup users are more loyal.
# 
# ### DeviceProtection
# - Device protection lowers churn.
# - Lack of it increases the risk of churn.
# 
# ### TechSupport
# - Lack of tech support = high churn.
# - Tech support users rarely churn.
# 
# ### StreamingTV
# - Slightly higher churn in customers without streaming TV.
# - Not a strong churn factor.
# 
# ### StreamingMovies
# - Similar to StreamingTV — no service = slightly higher churn.
# 
# The majority of customers who do not churn tend to have services like PhoneService, InternetService (particularly DSL), and OnlineSecurity enabled. For services like OnlineBackup, TechSupport, and StreamingTV, churn rates are noticeably higher when these services are not used or are unavailable.
# 

# In[19]:


plt.figure(figsize = (6,4))
ax = sns.countplot(x = "PaymentMethod", data = df, hue = "Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Churned Customers by Payment Method")
plt.xticks(rotation = 45)
plt.show()


# ## customer is likely to churn when he is using electronic check as a payment method.
# 

# In[20]:


pip install nbconvert


# In[ ]:





# In[ ]:




