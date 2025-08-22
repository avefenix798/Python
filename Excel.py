import pandas as pd
import matplotlib.pyplot as ptl
import os
def main():
    datos = pd.DataFrame({'Ventas':[23,45,34],'Sucursal':['Norte','Sur','Oeste']})
    datos = datos.sort_values(by='Ventas',  ascending=False)
    print(datos)
    datos.plot.barh()
    excel_file_path ='Ventas.csv'
    datos.to_csv(excel_file_path, index=False) 
    os.startfile(excel_file_path)
    print('Total de ventas')
    print(datos['Ventas'].sum())
    print('Mejores Ventas')
    print(datos[:1])


    ptl.show()
if __name__ =='__main__':
    main()
