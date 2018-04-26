import pandas as pd
import pandas_gbq as gbq

# Insert your BigQuery Project ID Here
projectid = [INSERT PROJECT ID]

# csv url
#url = [INSERT URL TO PULL DATA]

# Read file into a DataFrame: df
df = pd.read_csv(url)

# create new table in BQ, if table already exists, replace it.
gbq.to_gbq(df, [INSERT DATASET.TABLE], projectid,private_key=[INSERT_KEY],if_exists='replace')

#print the head() of the df
print(df.head())