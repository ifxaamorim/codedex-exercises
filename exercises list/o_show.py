class Fan:
    def __init__(self,nome,artista_favorito, reacao):
        self.nome = nome
        self.artista_favorito = artista_favorito
        self.reacao = reacao

    def ver_show(self):
        print(f"{self.nome} está reagindo: {self.reacao} ao ver {self.artista_favorito} no palco")


fan1 = Fan("Lucas", "Olivia Rodrigo", "Grita")
fan2 = Fan("Camilla", "Taylor Swift", "Grita de alegria")

fan1.ver_show()
fan2.ver_show()
