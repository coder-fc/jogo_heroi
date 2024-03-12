# Personagem: classe mae
# Heroi: controlado pelo usuário
# Inimigo: Adversário do usuário

class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
