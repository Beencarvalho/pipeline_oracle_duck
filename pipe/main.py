from oracle_connection import connect_oracle, fetch_data_from_oracle
from duckdb_processing import process_data_with_duckdb
from utils.utils import load_query_from_file
from secret.oracle_secrets import load_oracle_credentials  # Carregar a função para ler as credenciais

# Caminho para os arquivos de queries e credenciais
queries_file = 'sql/queries.sql'
credentials_file = 'secret/oracle_connection_info.json'

# Carregar as queries a partir do arquivo SQL
query_oracle = load_query_from_file(queries_file, 'query_oracle')
query_duckdb = load_query_from_file(queries_file, 'query_duckdb')

def main_pipeline():
    # Carregar as credenciais do arquivo JSON
    oracle_credentials = load_oracle_credentials(credentials_file)
    
    # Conectar ao Oracle usando as credenciais carregadas
    oracle_conn = connect_oracle(user=oracle_credentials['user'], 
                                 password=oracle_credentials['password'], 
                                 host=oracle_credentials['host'], 
                                 port=oracle_credentials['port'], 
                                 service_name=oracle_credentials['service_name'])
    
    # Buscar os dados do Oracle usando a query carregada do arquivo SQL
    df_oracle = fetch_data_from_oracle(oracle_conn, query_oracle)
    
    # Processar com DuckDB usando a query carregada do arquivo SQL
    processed_data = process_data_with_duckdb(df_oracle, query_duckdb)
    
    # Fechar a conexão com o Oracle
    oracle_conn.close()
    
    # Retornar ou salvar o resultado processado
    return processed_data

if __name__ == '__main__':
    final_data = main_pipeline()
    print(final_data)
