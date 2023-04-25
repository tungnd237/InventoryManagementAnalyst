# Boilerplate preprocessing codes (for EDA)
# DROPPED: less important columns
# ENCODED: categorical columns
# STANDARDIZED: all columns by StandardScaler

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

import scipy.stats as stats

from sklearn.decomposition import PCA
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# IMPORT: Tableau Superstore dataset
df = pd.read_csv("../data/superstore_sample.csv")


# CHANGE: to natural format: non-numeric types
# Type Change: 2 columns -> str
df['Customer ID'] = df['Customer ID'].astype("string")
df['Product ID'] = df['Product ID'].astype("string")
# Type Change: 5 columns -> category 
df['Ship Mode'] = df['Ship Mode'].astype("category")
df['Segment'] = df['Segment'].astype("category")
df['Region'] = df['Region'].astype("category")
df['Category'] = df['Category'].astype("category")
df['Sub-Category'] = df['Sub-Category'].astype("category")
# Type Change: 2 columns -> datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])


# DEFINE: column types
id_columns = [
    "Customer ID", "Product ID",
]
# Potential target variables
numeric_columns = [
    "Sales", "Quantity", "Discount", "Profit"
]
category_columns = [
    "Ship Mode", #4
    "Segment", #3
    "Region", #4
    "Category", #3
    "Sub-Category" #17
]
void_columns = [
   "Row ID", "Order ID", "Country"
]

# Customer Name <-> Customer ID
# Product Name <-> Product ID
# [City, State, Postal Code] <-> Region
redundant_columns = [
    "Customer Name", "Product Name", 
    "City", "State", "Postal Code"
]


# ASSIGN: numeric id instead of string id
# Customer Id -> C_id
# Product Id -> P_id
for i in id_columns:
    df[i[0]+'_id'] = df.groupby(i).ngroup()


# DROP: 10 Columns = id + void + redundant
dropping_columns = id_columns + void_columns + redundant_columns
df_f = df.drop(columns=dropping_columns)

# PROFILE: exploratory analysis & save to HTML - uncomment when needed
# import ydata_profiling as yp
# report_super_f = df_f.profile_report()
# report_super_f.to_file(output_file="0409_super_f_report.html")

# ENCODE: One-Hot Encode 5 categorical variables
# "Ship Mode"#4 "Segment"#3 "Region"#4 "Category"#3 "Sub-Category"#17
for i in category_columns:
    ohe = OneHotEncoder()
    ohe_df = pd.DataFrame(
        ohe.fit_transform(df_f[[i]]).toarray())
    # add suffix to column names in ohe_df
    ohe_df.columns = ohe_df.columns.astype(str)
    ohe_df = ohe_df.add_suffix(i)
    # define new dataframe to distinguish before-and-after encoding
    df_f = df_f.join(ohe_df)

# DROP & Standardize: categorical variables
# will have to check how much data deviates from Gaussian
# for now, assume it fares ok 
# = leave it as window for improvement
scaler = StandardScaler()

# Save standardized dataframe in a new variable,
# for preliminary model training and testing
scaled_df_f = scaler.fit_transform(
    df_f.drop(category_columns, axis=1))