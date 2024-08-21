from banco import ConexaoBanco
from models.empresa_valor import EmpresaValor

class SetorRepository:
    def __init__(self, config) -> None:
        self.banco = ConexaoBanco(config) 
        self.CarregarCache()
    
    def CarregarCache(self) -> bool:
        try:
            self.valores = []
            sql = '''SELECT ID
	                    , ID_EMPRESA
                        , DATA_VALOR
                        , PRECO
                        , VARIACAO
                        , VOLUME
                        , VOLUME_REAL
                        , VALOR_MERCADO
                        , PL
                        , EPS
                        , VARIACAO_EPS
                        , DIV_YIELD 
                    FROM EMPRESA_VALOR'''
            
            dt = self.banco.ExecutarComando(sql)
            
            if(dt):
                for linha in dt:
                    self.setores.append(EmpresaValor(id = linha[0],
                                                     id_empresa = linha[1],
                                                     data = linha[2],
                                                     preco = linha[3],
                                                     variacao = linha[4],
                                                     volume = linha[5],
                                                     volume_real = linha[6],
                                                     valor_mercado = linha[7],
                                                     pl = linha[8],
                                                     eps = linha[9],
                                                     variacao_eps = linha[10],
                                                     div_yield = linha[11]))
            
            return True
        except:
            return False
    
    def Inserir(self, empresa_valor) -> bool:
        try:
            if not empresa_valor:
                return False
            
            sql = f'''INSERT INTO EMPRESA_VALOR (ID_EMPRESA,
                                                 DATA_VALOR, 
                                                 PRECO, 
                                                 VARIACAO, 
                                                 VOLUME, 
                                                 VOLUME_REAL, 
                                                 VALOR_MERCADO, 
                                                 PL, 
                                                 EPS, 
                                                 VARIACAO_EPS, 
                                                 DIV_YIELD) 
                    VALUES ({empresa_valor.id_empresa}, 
                           '{empresa_valor.data}', 
                           {empresa_valor.preco}, 
                           {empresa_valor.variacao}, 
                           {empresa_valor.volume},
                           {empresa_valor.volume_real}, 
                           {empresa_valor.valor_mercado}, 
                           {empresa_valor.pl}, 
                           {empresa_valor.eps}, 
                           {empresa_valor.variacao_eps}, 
                           {empresa_valor.div_yield})'''
            
            self.banco.ExecutarComando(sql, commit=True)
            self.CarregarCache()

            return True
        except:
            return False
    
    def Atualizar(self, empresa_valor) -> bool:
        try:
            if not empresa_valor:
                return False
            
            sql = f'''UPDATE EMPRESA_VALOR 
                        SET ID_EMPRESA = {empresa_valor.id_empresa}, 
                            DATA_VALOR = {empresa_valor.data}, 
                            PRECO = {empresa_valor.preco}, 
                            VARIACAO = {empresa_valor.variacao}, 
                            VOLUME = {empresa_valor.volume}, 
                            VOLUME_REAL = {empresa_valor.volume_real}, 
                            VALOR_MERCADO = {empresa_valor.valor_mercado}, 
                            PL = {empresa_valor.pl}, 
                            EPS = {empresa_valor.eps}, 
                            VARIACAO_EPS = {empresa_valor.variacao_eps}, 
                            DIV_YIELD = {empresa_valor.div_yield}
                      WHERE ID = {empresa_valor.id}'''
            
            self.banco.ExecutarComando(sql, commit=True)
            self.CarregarCache()

            return True
        except:
            return False

    def Excluir(self, empresa_valor) -> bool:
        try:
            if not empresa_valor:
                return False
            
            sql = f"DELETE EMPRESA_VALOR WHERE ID = {empresa_valor.id}"
            self.banco.ExecutarComando(sql, commit=True)
            self.CarregarCache()

            return True
        except:
            return False

        