import json

def load_oracle_credentials(file_path):
    """
    Carrega as credenciais do Oracle a partir de um arquivo JSON.
    
    :param file_path: Caminho para o arquivo JSON contendo as credenciais
    :return: Um dicionário com as credenciais (user, password, host, port, service_name)
    """
    with open(file_path, 'r') as file:
        credentials = json.load(file)
    
    return credentials
