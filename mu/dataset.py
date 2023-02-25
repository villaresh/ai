import os, csv

f=open("C:/Users/USER/Downloads/ai/dataset.csv",'r+')
w=csv.writer(f)
for path, dirs, files in os.walk("C:/Users/USER/Downloads/ai"):
    for filename in files:
        w.writerow([filename])

import pandas as pd
df = pd.read_csv("C:/Users/USER/Downloads/ai/dataset.csv")
df.to_csv("C:/Users/USER/Downloads/ai/dataset2.csv", index=False)
