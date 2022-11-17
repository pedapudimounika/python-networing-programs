import pandas as pd

data = {'country': ['Belgium', 'india', 'brizal'],
'Capital': ['Brussel', 'newdelhi', 'beng'],
'population': [2323534, 4535647,364574]}

df = pd.DataFrame(data,columns=['country','Capital', 'population'])
print(df)