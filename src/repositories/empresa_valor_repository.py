from banco import ConexaoBanco
from models.empresa_valor import EmpresaValor

class EmpresaValorRepository:
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
    
    def SelecionarPorId(self, id) -> EmpresaValor:
        try:
            for valor in self.valores:
                if(valor.id == id):
                    return valor
            return None
        except:
            return None
        
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
                           CONVERT(datetime,'{empresa_valor.data.year}-{empresa_valor.data.month}-{empresa_valor.data.day} {empresa_valor.data.hour}:{empresa_valor.data.minute}:{empresa_valor.data.second}', 121), 
                           {'NULL' if empresa_valor.preco == None else empresa_valor.preco}, 
                           {'NULL' if empresa_valor.variacao == None else empresa_valor.variacao}, 
                           {'NULL' if empresa_valor.volume == None else empresa_valor.volume},
                           {'NULL' if empresa_valor.volume_real == None else empresa_valor.volume_real}, 
                           {'NULL' if empresa_valor.valor_mercado == None else empresa_valor.valor_mercado}, 
                           {'NULL' if empresa_valor.pl == None else empresa_valor.pl}, 
                           {'NULL' if empresa_valor.eps == None else empresa_valor.eps}, 
                           {'NULL' if empresa_valor.variacao_eps == None else empresa_valor.variacao_eps}, 
                           {'NULL' if empresa_valor.div_yield == None else empresa_valor.div_yield})'''
            
            self.banco.ExecutarComando(sql, commit=True)
            self.CarregarCache()

            return True
        except Exception:
            print(Exception())
            return False
    
    def Atualizar(self, empresa_valor) -> bool:
        try:
            if not empresa_valor:
                return False
            
            sql = f'''UPDATE EMPRESA_VALOR 
                        SET ID_EMPRESA = {empresa_valor.id_empresa}, 
                            DATA_VALOR = CONVERT(datetime, {empresa_valor.data.year}-{empresa_valor.data.month}-{empresa_valor.data.day} {empresa_valor.data.hour}:{empresa_valor.data.minute}:{empresa_valor.data.second}, 121), 
                            PRECO = {empresa_valor.preco == None: 'NULL' else: empresa_valor.preco}, 
                            VARIACAO = {empresa_valor.variacao == None: 'NULL' else: empresa_valor.variacao}, 
                            VOLUME = {empresa_valor.volume == None: 'NULL' else: empresa_valor.volume}, 
                            VOLUME_REAL = {empresa_valor.volume_real == None: 'NULL' else: empresa_valor.volume_real}, 
                            VALOR_MERCADO = {empresa_valor.valor_mercado == None: 'NULL' else: empresa_valor.valor_mercado}, 
                            PL = {empresa_valor.pl == None: 'NULL' else: empresa_valor.pl}, 
                            EPS = {empresa_valor.eps == None: 'NULL' else: empresa_valor.eps}, 
                            VARIACAO_EPS = {empresa_valor.variacao_eps == None: 'NULL' else: empresa_valor.variacao_eps}, 
                            DIV_YIELD = {empresa_valor.div_yield == None: 'NULL' else: empresa_valor.div_yield}
                      WHERE ID = {empresa_valor.id}'''
            
            print(sql)
            
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

        