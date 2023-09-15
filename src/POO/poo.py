class Cachorros:
    def __init__(self,nome,cor_de_pele, idade, tamanho):
        self.nome = nome
        self.cor_de_pelo = cor_de_pele
        self.idade = idade
        self.tamanho = tamanho
    
    def latir(self):
        print('Au au!')
    def correr(self):
        print(f'{self.nome} está correndo...')

cachorro1 = Cachorros('Toma','marrom', 5, 'medio')
cachorro1.latir()
cachorro1.correr()