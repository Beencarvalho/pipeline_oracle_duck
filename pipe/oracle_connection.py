import cx_Oracle
import pandas as pd

def connect_oracle(user, password, host, port, service_name):
    dsn_tns = cx_Oracle.makedsn(host, port, service_name=service_name)
    connection = cx_Oracle.connect(user=user, password=password, dsn=dsn_tns)
    return connection

def fetch_data_from_oracle(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [i[0] for i in cursor.description]
    cursor.close()
    return pd.DataFrame(rows, columns=columns)

