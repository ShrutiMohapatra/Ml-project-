import boto3
import pandas as pd

s3 = boto3.client('s3')
s3.download_file('mybucket', 'data/data.csv', 'data.csv')

df = pd.read_csv("data.csv")
print(df.head())


