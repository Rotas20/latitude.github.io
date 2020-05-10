import pandas as pd

#read in the datafile (as csv)

df = pd.read_csv('/Users/star/GitHub/HW/WebVisualizations/Web-Design-Challenge/Resources/cities.csv')


df.to_html('Data.html',index=False)

