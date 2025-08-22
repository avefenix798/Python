import pandas as pd, pyodbc    

def main():
    con_string = 'DRIVER={SQL Server};SERVER=DESKTOP-KLQGNV9\SQLEXPRESS;DATABASE=Datos'
    cnxn = pyodbc.connect(con_string)
    query = """
    select top 5 Categoria
    , sum(Venta) Venta
    from [dbo].[Venta]
    group by Categoria
    order by sum(Venta) Desc
    """
    Top = pd.read_sql(query, cnxn)
    Top.to_clipboard()
    print(Top)

if __name__ == '__main__':
    main()