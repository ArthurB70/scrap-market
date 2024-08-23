from banco import ConexaoBanco
from models.empresa import Empresa

class EmpresaRepository:
    def __init__(self, config) -> None:
        self.banco = ConexaoBanco(config) 
        self.CarregarCache()
    
    def CarregarCache(self) -> bool:
        try:
            self.empresas = []
            sql = 'SELECT ID, NOME, SIGLA, URL, ID_SETOR FROM EMPRESA'
            dt = self.banco.ExecutarComando(sql)
            
            if(dt):
                for linha in dt:
                    self.empresas.append(Empresa(id = linha[0], nome = linha[1], sigla = linha[2], url = linha[3], id_setor = linha[4]))
            
            return True
        except:
            return False
    
    def SelecionarPorId(self, id) -> Empresa:
        try:
            for empresa in self.empresas:
                if(empresa.id == id):
                    return empresa
            return None
        except:
            return None
    
    def SelecionarPorNome(self, nome) -> Empresa:
        try:
            for empresa in self.empresas:
                if(empresa.nome == nome):
                    return empresa
            return None
        except:
            return None
        
    def SelecionarPorSigla(self, sigla) -> Empresa:
        try:
            for empresa in self.empresas:
                if(empresa.sigla == sigla):
                    return empresa
            return None
        except:
            return None
    
    def Inserir(self, empresa) -> Empresa:
        try:
            if not empresa:
                return None
            
            sql = f"INSERT INTO EMPRESA (NOME, SIGLA, URL, ID_SETOR) VALUES ('{empresa.nome}', '{empresa.sigla}', '{empresa.url}',{empresa.id_setor})"
            self.banco.ExecutarComando(sql, commit=True)
            self.CarregarCache()

            return self.SelecionarPorSigla(empresa.sigla)
        except:
            return None
    
    def Atualizar(self, empresa) -> bool:
        try:
            if not empresa:
                return False
            
            sql = f"UPDATE EMPRESA SET NOME = '{empresa.nome}', SIGLA = {empresa.sigla}, URL = {empresa.url}, ID_SETOR = {empresa.id_setor} WHERE ID = {empresa.id}"
            self.banco.ExecutarComando(sql, commit=True)
            self.CarregarCache()

            return True
        except:
            return False

    def Excluir(self, empresa) -> bool:
        try:
            if not empresa:
                return False
            
            sql = f"DELETE EMPRESA WHERE ID = {empresa.id}"
            self.banco.ExecutarComando(sql, commit=True)
            self.CarregarCache()

            return True
        except:
            return False

        