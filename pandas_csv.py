import pandas as pd
data = pd.read_csv(r'C:\Users\user410\Desktop\pythonfiles\gaints.csv')
df = pd.DataFrame(data, columns=['CEO', 'Established'])
print(df)