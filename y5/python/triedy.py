class Cas:
    def __init__(self, hodina, minuta):
        self.hodina = hodina
        self.minuta = minuta
    def vypis(self):
        print(f'je {self.hodina} hodin a {self.minuta}')
teraz = Cas(9, 15)
teraz.vypis()