import math

# Classe para representar um círculo
class Circulo:
    # Inicializa o objeto com o valor do raio
    def __init__(self, raio):
        self.raio = raio

    # Calcula e retorna a área do círculo
    def area(self):
        return math.pi * self.raio ** 2

    # Calcula e retorna o perímetro do círculo
    def perimetro(self):
        return 2 * math.pi * self.raio

# Classe para representar um retângulo
class Retangulo:
    # Inicializa o objeto com os valores da largura e altura
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    # Calcula e retorna a área do retângulo
    def area(self):
        return self.largura * self.altura

    # Calcula e retorna o perímetro do retângulo
    def perimetro(self):
        return 2 * (self.largura + self.altura)

# Função para imprimir informações (área e perímetro) de uma forma geométrica
def imprimir_informacoes(forma):
    print("Área:", forma.area())
    print("Perímetro:", forma.perimetro())

# Instanciando um círculo com raio 5 e um retângulo com largura 4 e altura 6
circulo1 = Circulo(5)
retangulo1 = Retangulo(4, 6)

# Imprimindo informações do círculo e retângulo criados
imprimir_informacoes(circulo1)
imprimir_informacoes(retangulo1)
