# Pokédex é um dispositivo que rastreia as informações de Pokémon que são vistos ou capturados.

class Pokemon:
    def __init__(self,id_pokemon,nome,tipo, descricao, habilidade,e_capturado):
        self.id_pokemon = id_pokemon
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.habilidade = habilidade
        self.e_capturado = e_capturado

    def speak(self):
        print(f"{self.nome} {self.nome}")  

    def display_detalhes(self):
        print(f"Número: {self.id_pokemon}")
        print(f"Nome: {self.nome}")
        print(f"Tipo: {self.tipo}")
        print(f"Descrição: {self.descricao}")
        print(f"Habilidade: {self.habilidade} ")
        if self.e_capturado == True:
            print(f"{self.nome} foi capturado")
        else:
            print(f"{self.nome} não foi capturado")

pikachu = Pokemon(25, "Pikachu","Elétrico", "rato amarelo, bochechas vermelhas, cauda em formato de raio", "Estatico", True)
charizard = Pokemon(6,"Charizard","Fogo", "dragão alaranjado, asas azuis, chama na cauda", "Chama", False)
skiddo = Pokemon(672, "Skiddo", "Grama", "cabra verde, folhas nas costas, chifres curvos.", "Sorvedor de seiva", False)

pikachu.speak()
pikachu.display_detalhes()
print("--------------------------------")
charizard.speak()
charizard.display_detalhes()
print("--------------------------------")
skiddo.speak()
skiddo.display_detalhes()

