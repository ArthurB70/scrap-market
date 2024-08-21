class Setor:
    def __init__(self, nome, id=0) -> None:
        self.id = id
        self.nome = nome
    
    def __repr__(self) -> str:
        return f'Id: {self.id}\tNome: {self.nome}'