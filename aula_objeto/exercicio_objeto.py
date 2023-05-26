class Pessoa:
    def __init__ (self,nome,peso,idade,comendo=False,falando=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def apresentar(self):
        memoria = print(f'{self.nome}')
        return memoria

    def comer(self,comida):
        if self.comendo == False and self.falando == False:
            self.comendo = True
            memoria = print(f'Agora {self.nome} está comendo uma {comida}, nham nham.')
            return memoria
        elif self.falando == True:
            print(f'Não podes comer enquanto fala!')
        else:
            memoria = print(f'{self.nome} já está comendo, nham nham.')
            return memoria
    def parar_de_comer(self):
        if self.comendo == True:
            self.comendo = False
            memoria = print(f'Agora {self.nome} não está mais comendo, :(')
            return memoria
        else:
            memoria = print(f'{self.nome} não está comendo!!!')
            return memoria
    def falar(self):
        if self.comendo == False and self.falando == False:
            print(f'HABLANDO AOHA')
            self.falando = True
        elif self.comendo == True:
            print(f'NO PUEDES HABLAR PAPANDO!')
        elif self.falando == True:
            print(f'JA ESTÁS HABLANDO HOMBRE!')
    def parar_de_falar(self):
        if self.falando == True:
            print(f'Paraste de Hablar')
            self.falando = False
        else:
            print(f'NO ESTÁS HABLANDO HOMBRE!')

a = Pessoa("Hugo",110,28)

print(f'{a.apresentar()}')
print(vars(a))

a.comer("Manga")
a.comer("Uva")
a.falar()
a.parar_de_comer()
a.parar_de_comer()
a.falar()
a.falar()
a.comer("Uva")
a.parar_de_falar()
a.parar_de_falar()