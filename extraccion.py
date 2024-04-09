import pandas as pd
import openpyxl

print('Aplicacion de extraccion de datos')
df = pd.read_excel('detalle_precios_productos_fabricados_2022.xlsx')

#Filtro por objeto 
filtro1=df[df["NOMBRE_VENDEDOR"] == "LETICIA RAMIREZ HERNANDEZ"]
print(filtro1)

#Filtro por filas
filtro2 = df.iloc[2:8,: ]   
print(filtro2)

#Filtro por columnas
filtro3 = df.iloc[2:5, [1,3,4,10]]
print(filtro3)

df1 = pd.read_excel('detalle_precios_productos_fabricados_2022.xlsx', index_col=1)

filtro4=df1.loc[["2022-11-22","'2022-12-23"], ["SUBTOTAL_PARTIDA"]]
print(filtro4)

filtro5=df.head(8)
print(filtro5)

filtro6=df[df["SUBTOTAL_PARTIDA"] > 77000]
print(filtro6)

#Filtro Y Tiene que cumplir las dos condiciones
filtro7=df[(df["SUBTOTAL_PARTIDA"] > 77000) & (df["FECHA_DOC"] == "2022-05-24")]
print(filtro7)
     
#Filtro o
filtro8=df[(df["SUBTOTAL_PARTIDA"] > 77000)| (df["FECHA_DOC"] == "2022-05-24")]
print(filtro8)

#Filtro not
filtro9=df[~(df["SUBTOTAL_PARTIDA"] > 77000) & ~(df["FECHA_DOC"] == "2022-05-24")]
print(filtro9)
     
#Convertir archivo filtrado a CSV
filtro1.to_csv("Entregable1.csv")
filtro2.to_csv("Entregable2.csv")
filtro3.to_csv("Entregable3.csv")
filtro4.to_csv("Entregable4.csv")
filtro5.to_csv("Entregable5.csv")
filtro6.to_csv("Entregable6.csv")
filtro7.to_csv("Entregable7.csv")
filtro8.to_csv("Entregable8.csv")
filtro9.to_csv("Entregable9.csv")

