class Tamagotchi:

    def __init__(self, energiaMax: int, saciedadeMax: int, limpezaMax: int, idadeMax: int):
        self.energiaMax = energiaMax
        self.saciedadeMax = saciedadeMax
        self.limpezaMax = limpezaMax
        self.idadeMax = idadeMax
        self.energiaAtual = energiaMax
        self.limpezaAtual = limpezaMax
        self.saciedadeAtual = saciedadeMax
        self.idadeAtual = 0
        self.diamantes = 0

    def getEnergiaMax(self):
        return self.energiaMax

    def getSaciedadeMax(self):
        return self.saciedadeMax

    def getLimpezaMax(self):
        return self.limpezaMax

    def getIdadeMax(self):
        return self.idadeMax

    def getEnergiaAtual(self):
        return self.energiaAtual

    def getSaciedadeAtual(self):
        return self.saciedadeAtual

    def getLimpezaAtual(self):
        return self.limpezaAtual

    def getIdadeAtual(self):
        return self.idadeAtual

    def getDiamantes(self):
        return self.diamantes

    def getEstaVivo(self):
        if self.energiaAtual > 0 and self.limpezaAtual > 0 and self.saciedadeAtual > 0 and self.idadeAtual < self.idadeMax:
            return True
        elif self.energiaAtual < 0:
            self.energiaAtual = 0
        elif self.saciedadeAtual < 0:
            self.saciedadeAtual = 0
        elif self.limpezaAtual < 0:
            self.limpezaAtual = 0
        else:
            return print(
                f'Energia: {self.energiaAtual}\n'
                f'Saciedade: {self.saciedadeAtual}\n'
                f'Limpeza: {self.limpezaAtual}\n'
                f'Idade: {self.idadeAtual}\n'
                f'Diamantes: {self.diamantes}\n'
                f'INFELIZMENTE SEU TAMAGOSHI MORREU. SUA ENERGIA OU SACIEDADE OU LIMPEZA CHEGOU A ZERO. SEJA MAIS RESPONSAVEL DA PROXIMA VEZ. ;)')

    def brincar(self):
        if self.getEstaVivo():
            self.energiaAtual = max(self.energiaAtual - 2, 0)
            self.saciedadeAtual = max(self.saciedadeAtual - 1, 0)
            self.limpezaAtual = max(self.limpezaAtual - 3, 0)
            self.idadeAtual = min(self.idadeAtual + 1, self.idadeMax)
            self.diamantes += 1
            return True
        else:
            return False

    def comer(self):
        if self.getEstaVivo():
            self.energiaAtual = max(self.energiaAtual - 1, 0)
            self.saciedadeAtual = min(self.saciedadeAtual + 4, self.saciedadeMax)
            if self.saciedadeAtual > self.saciedadeMax:
                self.saciedadeAtual = self.saciedadeMax  # 10
            self.limpezaAtual = max(self.limpezaAtual - 2, 0)
            self.diamantes += 0
            self.idadeAtual = min(self.idadeAtual + 1, self.idadeMax)
            return True
        else:
            return False

    def dormir(self):
        if self.getEstaVivo():
            if self.energiaMax - 5 >= self.energiaAtual:
                turno = self.energiaMax - self.energiaAtual
                self.energiaAtual = self.energiaMax
                self.idadeAtual += turno
                self.saciedadeAtual = max(self.saciedadeAtual - 2, 0)
                return True
        else:
            return False

    def banhar(self):
        if self.getEstaVivo():
            self.energiaAtual = max(self.energiaAtual - 3, 0)
            self.saciedadeAtual = max(self.saciedadeAtual - 1, 0)
            self.limpezaAtual = self.limpezaMax
            self.diamantes += 0
            self.idadeAtual = min(self.idadeAtual + 2, self.idadeMax)
            return True
        else:
            return False
