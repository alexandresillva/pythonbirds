class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprientar(self):
        return f'Olá {self.nome}'


if __name__ == '__main__':
    p = Pessoa("Alexandre Ribeiro")
    print(p.nome)
    print(p.idade)
    print(p.cumprientar())

