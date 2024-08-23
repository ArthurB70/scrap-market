import pyodbc
import traceback
import sys
import time

class ConexaoBanco():
    def __init__(self, config):
        self.connection_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"Server={config.banco.server};"
            f"Database={config.banco.database};"
            f"UID={config.banco.user};"
            f"PWD={config.banco.password};"
        )

        self.timeout = config.timeout = float(config.banco.timeout)
        self.conexao = None
    
    def AbrirConexao(self):
        try:
            self.conexao = pyodbc.connect(self.connection_string)
        except:
            traceback.print_exception(*sys.exc_info())

    def FecharConexao(self):
        try:
            self.conexao.close()
        except:
            traceback.print_exception(*sys.exc_info())

    def ExecutarComando(self, sql, commit = False):
        try:
            retorno = None
            start = time.time()
            end = time.time()
            while (not self.conexao or self.conexao.closed or end-start >= self.timeout):
                self.AbrirConexao()
                end = time.time()

            if(self.conexao and not self.conexao.closed):
                cursor = self.conexao.cursor()
                cursor.execute(sql)
                if(commit):
                    self.conexao.commit()
                else:    
                    retorno = cursor.fetchall()
                cursor.close()
                self.FecharConexao()
            else:
                Exception('Não foi possível abrir conexão com o banco de dados.')
            return retorno
        except:
            traceback.print_exception(*sys.exc_info())