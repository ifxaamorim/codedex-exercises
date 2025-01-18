## Crie um app com duas cidades favoritas e utilize o __init__

class Cidades:
    def __init__(self,nome,pais,populacao,ponto_ref ):
        self.nome = nome
        self.pais = pais
        self.populacao = populacao
        self.ponto_ref = ponto_ref

minas = Cidades("Minas Gerais", "Brasil", 21322691, ["Praça da liberdade", "Praça 7", "Ouro Preto"])

print(vars(minas))

australia = Cidades("Sidney", "Australia", 26997958, ["Great Barrier Reef", "Ilha dos Cangurus", "Melbourne"])

print(vars(australia))