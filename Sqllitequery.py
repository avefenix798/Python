import sqlite3
import pandas as pd
import matplotlib.pyplot as ptl
def main():
    rutabase = r'C:\Users\avefe\Desktop\Ejemplo.db'
    conn = sqlite3.connect(rutabase)

    df = pd.read_sql_query("select segment ,class , sum(value) Valor  from Inventory_v2 group by segment,class", conn)

    df.plot.bar('segment','Valor')
    ptl.title('Valor por segmento')
    ptl.show()


if __name__ == '__main__':
    main()
