## Use the concept of class and object to show my favorite albums at the moment

class Album:
    def __init__(self,nome_album,nome_cantor,musica_fav,nota):
        self.nome_album = nome_album
        self.nome_cantor = nome_cantor
        self.musica_fav = musica_fav
        self.nota = nota

cantor1 = Album("DeBÍ TiRAR MáS FOToS", "Bad Bunny", "DtMF",98)
cantor2 = Album("Harry's House", "Harry Styles", "Keep Driving",83 )
cantor3 = Album("Circles", "Mac Miller", "Complicated",83)
cantor4 = Album("Alligator Bites Never Heal", "Doechii", "CATFISH",79 )

print(vars(cantor1))
print(vars(cantor2))
print(vars(cantor3))
print(vars(cantor4))