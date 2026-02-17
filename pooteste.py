class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def latir(self):
        return (f"{self.nome} disse au au")
    
cao1 = Cachorro("Ozzy", 2)
cao2 = Cachorro("Spike", 5)

print(cao1.latir())
print(cao2.latir())
