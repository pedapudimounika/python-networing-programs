import pandas as pd
data = pd.read_excel(r'C:\Users\user410\Desktop\pythonfiles\companies.xlsx')
df = pd.DataFrame(data, columns=['CEO'])
print(df)