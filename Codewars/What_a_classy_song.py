class Song:
    def __init__(self, title, artist):
        self.tittle = title
        self.artist = artist
        self.old_peoples = []

    def how_many(self, lista):
        x = 0
        for nomes in (x.lower() for x in lista):
            if nomes not in self.old_peoples:
                self.old_peoples.append(nomes)
                x += 1
        return x


# Utilizando Set para resolver problema.
# class Song_2:
#     def __init__(self, tittle, artist):
#         self.tittle = tittle
#         self.artist = artist
#         self.old_peoples = set()

#     def how_many(self, lista):
#         lista = set(map(str.lower, lista))
#         resp = len(lista.difference(self.old_peoples))
#         self.old_peoples = self.old_peoples.union(lista)

#         return resp



class Song_3:

    def __init__(self, tittle, artist):
        self.tittle = tittle
        self.artist = artist
        self.lst = []


    def how_many(self, lista):
        s = sum(1 for name in (x.lower() for x in lista) if name not in self.lst)
        self.lst.extend([name.lower() for name in lista])

        return s 

mount_moose = Song_3('Pompeii', 'Bastille')

print(mount_moose.how_many(['John', 'Fred', 'Bob', 'Carl']))
print(mount_moose.how_many(['Thiago', 'Ricardo', 'BOB']))
print(mount_moose.how_many(['Thiago', 'Ricardo', 'BOB', 'Daminai']))


