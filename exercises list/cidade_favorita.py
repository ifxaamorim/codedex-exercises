## Crie um app com duas cidades favoritas e utilize o __init__

class Cidades:
    def __init__(self,nome,pais,populacao,ponto_ref ):
        self.nome = nome
        self.pais = pais
        self.populacao = populacao
        self.ponto_ref = ponto_ref

minas = Cidades("Minas Gerais", "Brasil", 230456789, ["Praça da liberdade", "Pirulito", "Ouro Preto"])

print(vars(minas))

australia = Cidades("Sidney", "Australia", 230456789, ["Great Barrier Reef", "Ilha dos Cangurus", "Melbourne"])

print(vars(australia))