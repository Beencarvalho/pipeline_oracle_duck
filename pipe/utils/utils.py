def load_query_from_file(file_path, query_name):
    """
    Carrega uma consulta SQL de um arquivo com base no nome definido.
    
    :param file_path: Caminho para o arquivo .sql
    :param query_name: Nome da consulta dentro do arquivo (marcado por -- nome: query_name)
    :return: A consulta SQL correspondente como string
    """
    with open(file_path, 'r') as f:
        content = f.read()

    # Encontrar o nome da query e retornar o SQL associado
    queries = content.split('-- nome:')
    for query in queries:
        if query_name in query:
            return query.split(';')[0].strip() + ';'  # Retorna a consulta até o ';'
    
    raise ValueError(f"Consulta '{query_name}' não encontrada no arquivo {file_path}.")
