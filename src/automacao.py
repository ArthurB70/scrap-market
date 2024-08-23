from selenium.webdriver.common.by import By
from configuracoes import Config
from browser import Browser
from banco import ConexaoBanco
from models.empresa import Empresa
from models.empresa_valor import EmpresaValor
from models.setor import Setor
from repositories.setor_repository import SetorRepository
from repositories.empresa_repository import EmpresaRepository
from repositories.empresa_valor_repository import EmpresaValorRepository
from datetime import datetime

config = Config()

setor_repository = SetorRepository(config)
empresa_repository = EmpresaRepository(config)
empresa_valor_repository = EmpresaValorRepository(config)

browser = Browser(config)

browser.BrowseUrl(r'https://br.tradingview.com/markets/stocks-brazil/market-movers-all-stocks/')

xpath_mostrar_mais = '/html/body/div[3]/div[4]/div/div[2]/div/div[4]/div[3]/button'

while(browser.WaitFindElement(xpath_mostrar_mais, 'Carregar mais')[0]):
    browser.WaitAndClickElement(xpath_mostrar_mais, 'Clicar carregar mais')

xpath_empresas = '/html/body/div[3]/div[4]/div/div[2]/div/div[4]/div[2]/div[2]/div/div/table/tbody/tr'
elements =  browser.FindElements(xpath_empresas, '')
#_ , element = browser.WaitFindElement(xpath_empresas, '')
i = 1
for element in elements:
    print(i,len(elements))
    i += 1
    setor_texto = element.find_element(By.XPATH,'.//td[11]/a').text
    setor = setor_repository.SelecionarPorNome(setor_texto)
    
    if(not setor):
        setor = setor_repository.Inserir(Setor(nome = setor_texto))

    sigla_texto = element.find_element(By.XPATH,'.//td[1]/span/a').text
    url_texto = element.find_element(By.XPATH,'.//td[1]/span/a').get_attribute('href')
    nome_texto = element.find_element(By.XPATH,'.//td[1]/span/sup').text
    
    empresa = empresa_repository.SelecionarPorSigla(sigla_texto)

    if(not empresa):
        empresa = empresa_repository.Inserir(Empresa(nome = nome_texto, sigla = sigla_texto, url = url_texto, id_setor = setor.id))

    preco_texto = element.find_element(By.XPATH,'.//td[2]').text
    variacao_texto = element.find_element(By.XPATH,'.//td[3]').text
    volume_texto = element.find_element(By.XPATH,'.//td[4]').text
    volume_real_texto = element.find_element(By.XPATH,'.//td[5]').text
    valor_mercado_texto = element.find_element(By.XPATH,'.//td[6]').text
    pl_texto = element.find_element(By.XPATH,'.//td[7]').text
    eps_texto = element.find_element(By.XPATH,'.//td[8]').text
    variacao_eps_texto = element.find_element(By.XPATH,'.//td[9]').text
    diYield_texto = element.find_element(By.XPATH,'.//td[10]').text

    empresa_valor_repository.Inserir(EmpresaValor(id_empresa = empresa.id, 
                                                  data = datetime.now(), 
                                                  preco = preco_texto,
                                                  variacao = variacao_texto,
                                                  volume = volume_texto,
                                                  volume_real= volume_real_texto,
                                                  valor_mercado= valor_mercado_texto,
                                                  pl=pl_texto,
                                                  eps=eps_texto,
                                                  variacao_eps=variacao_eps_texto,
                                                  div_yield=diYield_texto
                                                  ))
    

browser.CloseBrowser()
