# Criando uma classe
class Pessoa:

    # Método construtor (é executado quando criamos o objeto)
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método para mostrar os dados
    def apresentar(self):
        print("Olá, meu nome é", self.nome)
        print("Eu tenho", self.idade, "anos")


# Criando um objeto (uma pessoa)
p1 = Pessoa("Ana", 20)

# Chamando o método
p1.apresentar()