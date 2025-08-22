import pandas  as pd 


Datos = pd.DataFrame({ 'Venta':[23,45,34,34,23,23],'Devoluciones':[2,3,0,6,7,8]   })
Datos['PiezasOK']= Datos['Venta'] - Datos['Devoluciones'] 
Datos.plot()

print(Datos)

print ('Promedio de Ventas')
print(Datos['Venta'].median())


print ('Ventas Maximas')
print(Datos['Venta'].max())


print ('Promedio de devoluciones')
print(Datos['Devoluciones'].median())