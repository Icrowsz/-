class Onibus:
    def __init__(self, placa, nome_motorista, num_assentos):
        self.placa = placa
        self.nome_motorista = nome_motorista
        self.assentos = [False] * num_assentos

    def __len__(self):
        return len(self.assentos)

    def __getitem__(self, indice):
        if indice < - or inde

