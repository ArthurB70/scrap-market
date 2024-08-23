
class EmpresaValor:
    def __init__(self
                 , id_empresa
                 , data
                 , preco
                 , variacao
                 , volume
                 , volume_real
                 , valor_mercado
                 , pl
                 , eps
                 , variacao_eps
                 , div_yield
                 , id=0) -> None:
        
        self.id = id
        self.id_empresa = id_empresa
        self.data = data
        self.preco =  self.FormatarDecimal(preco)
        self.variacao = self.FormatarDecimal(variacao)
        self.volume = self.FormatarDecimal(volume)
        self.volume_real = self.FormatarDecimal(volume_real)
        self.valor_mercado = self.FormatarDecimal(valor_mercado)
        self.pl = self.FormatarDecimal(pl)
        self.eps = self.FormatarDecimal(eps)
        self.variacao_eps = self.FormatarDecimal(variacao_eps)
        self.div_yield = self.FormatarDecimal(div_yield)
    
    def __repr__(self) -> str:
        return (f'Id Empresa: {self.id_empresa} \n'
                f'Data: {self.data}\n'
                f'Preço: {self.preco}\n'
                f'Variação: {self.variacao}\n'
                f'Volume: {self.volume}\n'
                f'Volume Real: {self.volume_real}\n'
                f'Valor de Mercado: {self.valor_mercado}\n'
                f'PL: {self.pl}\n'
                f'EPS: {self.eps}\n'
                f'Variação EPS: {self.variacao_eps}\n'
                f'Div. Yield: {self.div_yield}'
            )

    @staticmethod
    def FormatarDecimal(valor):
        if valor == '—':
            return None
        
        valor = valor.replace('BRL','').replace('%','').replace('.','').replace(',','.').replace(' ', '').replace(' ','')
        multiplicador = 1

        if 'K' in valor:
            multiplicador = 1000
        elif 'M' in valor:
            multiplicador = 1000000
        elif 'B' in valor:
            multiplicador = 1000000000
    
        valor = valor.replace('K','').replace('M','').replace('B','').replace('\U00002013', '-').replace('\U00002212','-')
        return float(valor) * multiplicador