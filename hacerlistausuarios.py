import pandas as pd
archivo_excel = pd.read_excel('usuarios.xlsx')
values = archivo_excel.values
print values[:,0]
