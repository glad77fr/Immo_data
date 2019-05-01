import pandas as pd
import matplotlib.pyplot as plt
import xlsxwriter

source = pd.read_csv(r'C:\Users\Sabri\Desktop\Valeur foncière\valeursfoncieres-2018.txt',sep='|',encoding ='utf-8',low_memory=False)

source = source[source.columns[7:]] # Suppression des premières colonnes
asnieres =  source['Code postal']==92600
asnieres = source[asnieres]

Franklin = asnieres['Voie']=="FRANKLIN"
Franklin = asnieres[Franklin]

print(list(Franklin['Valeur fonciere']))
plt.plot(list(Franklin['Surface Carrez du 1er lot']),list(Franklin['Valeur fonciere']),'ro')

plt.show()

writer = pd.ExcelWriter(r'C:\Users\Sabri\Desktop\Valeur foncière\export.xlsx', engine='xlsxwriter')
asnieres.to_excel(writer, sheet_name='Feuil1')
writer.save()
