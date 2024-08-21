import json
import encrypt as enc

CONFIG_FILE_PATH = '..\config.json' 

class Path:
    def __init__(self,
                 download_default,
                 log):
        
        self.download_default = download_default
        self.log = log
    
    def __repr__(self):
        return f'Download_default{self.download_default}\nArquivo_log: {self.log}\n'

class BancoDados:
    def __init__(self
                 , server
                 , database
                 , user
                 , password
                 , timeout) -> None:
        self.server = server
        self.database = database
        self.user = user
        self.password = password
        self.timeout = timeout
    
    def __repr__(self):
        return f'Servidor: {self.server}\nBanco: {self.database}\nUser{self.user}'


class Config:
    def __init__(self):
        atributos_encriptados = ['password', 'token']

        config_path = self.ImportarConfig('paths', atributos_encriptados)
        config_db = self.ImportarConfig('credenciais_db', atributos_encriptados)
        
        self.path = Path(
            download_default = config_path['download_default'],
            log = config_path['log']
        )

        self.banco = BancoDados(
            server= config_db['server'],
            database= config_db['database'],
            user= config_db['user'],
            password= config_db['password'],
            timeout = config_db['timeout']
        )
    
    def ImportarConfig(self, configuracao, atributos_encriptados):
        config_json = None
        with open(CONFIG_FILE_PATH, 'r', encoding='utf-8') as f:
            config_json = json.load(f)
            
        config = config_json[configuracao]
        config_keys = list(config.keys())

        if('encrypt' in config_keys):
            encrypt_keys = []
            for atributo in config_keys:
                if (atributo in atributos_encriptados): 
                    encrypt_keys.append(atributo)

            if(config['encrypt'] == 'S'):
                config['encrypt'] = 'N'
                for conf in encrypt_keys:
                    config[conf] = enc.Encrypt(config[conf])
                    
                config_json[configuracao] = config

                with open(CONFIG_FILE_PATH, 'w', encoding='utf-8') as f:
                    json.dump(config_json, f, indent = 4)
            
            for conf in encrypt_keys:
                config[conf] = enc.Decrypt(config[conf])

        return config
