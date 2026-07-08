import Random

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
    
    def tomar_dano(self, valor):
        self.vida -= valor
        if self.vida < 0:
            self.vida = 0
    
class Mago(Personagem):
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self.mana = mana

    def __str__(self):
        return f"MAGO: {self.nome} / VIDA: {self.vida} / MANA: {self.mana}"

    def __add__(self, valor):
        self.mana += valor
        return self.mana

    def __sub__(self, valor):
        self.mana -= valor
        if self.mana < 0:
            self.mana = 0
        return self.mana

    def __mul__(self, fator):
        self.mana *= fator
        return self.mana
    
    def __truediv__(self, valor):
        self.mana /= valor
        return self.mana

class Barbaro(Personagem):
    def __init__(self, nome, vida, stamina):
        super().__init__(nome, vida)
        self.stamina = stamina
        self.furia = False

    def __str__(self):
        return f"BARBARO: {self.nome} / VIDA: {self.vida} / STAMINA: {self.stamina} / FURIA: {self.furia}"
    
    def __add__(self, valor):
        ganho = valor
        if self.furia:
            ganho *= 1.5
        
        self.stamina += ganho
        return self.stamina

    def __sub__(self, valor):
        self.stamina -= valor
        if self.stamina <= 0:
            self.stamina = 5

            if not self.furia:
                self.furia = True
        
        return self.stamina

    def __mul__(self, fator):
        self.stamina *= fator
        if self.furia:
            self.vida += 5

        return self.stamina
    
    def __truediv__(self, valor):
        self.stamina /= valor
        return self.stamina

tipo = input("ESCOLHA O PERSONAGEM (MAGO/BARBARO):").lower()

nome = input("NOME: ")
vida = int(input("VIDA: "))

if tipo 