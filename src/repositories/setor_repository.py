from banco import ConexaoBanco
from models.setor import Setor

class SetorRepository:
    def __init__(self, config) -> None:
        self.banco = ConexaoBanco(config) 
        self.CarregarCache()
    
    def CarregarCache(self) -> bool:
        try:
            self.setores = []
            sql = 'SELECT ID, NOME FROM SETOR'
            dt = self.banco.ExecutarComando(sql)
            
            if(dt):
                for linha in dt:
                    self.setores.append(Setor(id = linha[0], nome = linha[1]))
            
            return True
        except:
            return False
    
    def SelecionarPorId(self, id) -> Setor:
        try:
            for setor in self.setores:
                if(setor.id == id):
                    return setor
            return None
        except:
            return None
    
    def SelecionarPorNome(self, nome) -> Setor:
        try:
            for setor in self.setores:
                if(setor.nome == nome):
                    return setor
            return None
        except:
            return None
            
    def Inserir(self, setor) -> Setor:
        try:
            if not setor:
                return None
            
            sql = f"INSERT INTO SETOR (NOME) VALUES ('{setor.nome}')"
            self.banco.ExecutarComando(sql, commit=True)
            self.CarregarCache()

            return self.SelecionarPorNome(setor.nome)
        except:
            return None
    
    def Atualizar(self, setor) -> bool:
        try:
            if not setor:
                return False
            
            sql = f"UPDATE SETOR SET NOME = '{setor.nome}' WHERE ID = {setor.id}"
            self.banco.ExecutarComando(sql, commit=True)
            self.CarregarCache()

            return True
        except:
            return False

    def Excluir(self, setor) -> bool:
        try:
            if not setor:
                return False
            
            sql = f"DELETE SETOR WHERE ID = {setor.id}"
            self.banco.ExecutarComando(sql, commit=True)
            self.CarregarCache()

            return True
        except:
            return False

        