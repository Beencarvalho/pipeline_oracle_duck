import duckdb
import pandas as pd

def process_data_with_duckdb(df, query):
    con = duckdb.connect(database=':memory:')
    
    # Criar a tabela no DuckDB com o DataFrame
    con.execute("CREATE TABLE my_table AS SELECT * FROM df")
    
    # Executar a consulta genérica passada como argumento
    result = con.execute(query).df()
    
    return result
