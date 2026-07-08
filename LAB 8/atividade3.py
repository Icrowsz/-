class Carteira:
    def __init__(self, moeda, saldo):
        self.moeda = moeda
        self.saldo = saldo
    
    def converter_yuan(self, valor_yuan):
        if self.moeda == "USD":
            return valor_yuan * 0.14
        elif self.moeda == "BRL":
            return valor_yuan * 0.85
        else:
            return valor_yuan

    def __add__(self, valor_yuan):
        valor_convertido = self.converter_yuan(valor_yuan)
        return self.saldo + valor_convertido

    def __sub__(self, valor_yuan):
        valor_convertido = self.converter_yuan(valor_yuan)
        return self.saldo - valor_convertido

carteira_usd = Carteira("USD", 10.0)
print("USD + 50 CNY =", carteira_usd + 50.0)
print("USD - 50 CNY =", carteira_usd - 50.0)
print("☁")
carteira_brl = Carteira("BRL", 100.0)
print("BRL + 50 CNY =", carteira_brl + 50.0)
print("BRL - 50 CNY =", carteira_brl - 50.0)
print("☁")
carteira_cny = Carteira("CNY", 200.0)
print("CNY + 50 CNY =", carteira_cny + 50.0)
print("CNY - 50 CNY =", carteira_cny - 50.0)