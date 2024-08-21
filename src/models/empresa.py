class Empresa:
    def __init__(self
                 , nome
                 , sigla
                 , url
                 , id_setor
                 , id=0) -> None:
        self.id = id
        self.nome = nome
        self.sigla = sigla
        self.url = url
        self.id_setor = id_setor
    
    def __repr__(self) -> str:
        return ('Empresa\n'
                f'Nome: {self.nome}\n'
                f'Sigla: {self.sigla}\n'
                f'Url: {self.url}\n'
                f'Id Setor: {self.id_setor}'  
            )

    def set_id(self, id) -> None:
        self.id = id