from src.crianca import Crianca


class PulaPula:

    def __init__(self, limiteMax):
        self.limiteMax = limiteMax
        self.filaDeEspera = []
        self.criancasPulando = []
        self.caixa = 0
        self.conta = {}

    def getFilaDeEspera(self):
        return self.filaDeEspera

    def getCriancasPulando(self):
        return self.criancasPulando

    def getLimiteMax(self):
        return self.limiteMax

    def getCaixa(self):
        return self.caixa

    def getConta(self, nome):
        if self.conta[nome] == 0:
            return None
        else:
            return self.conta[nome]

    def entrarNaFila(self, crianca: Crianca):
        if crianca not in self.filaDeEspera:
            for kid in self.filaDeEspera:
                if kid.getNome() == crianca.getNome():
                    return False
            self.filaDeEspera.append(crianca)
            self.conta[crianca.getNome()] = 0
            return True

    def entrar(self):
        if self.filaDeEspera:
            if len(self.criancasPulando) >= self.getLimiteMax():
                return False
            else:
                tempo = self.filaDeEspera.pop(0)
                self.criancasPulando.append(tempo)
                if self.conta.get(tempo.getNome()):
                    self.conta[str(tempo.getNome())] += 2.5
                    return True
                else:
                    self.conta[tempo.getNome()] = 2.5
                    return True

    def sair(self):
        if self.criancasPulando:
            temp = self.criancasPulando.pop(0)
            self.filaDeEspera.append(temp)
            return True
        else:
            return False

    def papaiChegou(self, nome):
        if self.criancasPulando:
            for kid in self.criancasPulando:
                if kid.getNome() == nome:
                    self.caixa += self.conta[nome]
                    self.conta[nome] = 0
                    return True
        elif self.filaDeEspera:
            for kid in self.filaDeEspera:
                if kid.getNome() == nome:
                    self.caixa += self.conta[nome]
                    self.conta[nome] = 0
                    return True
        else:
            return False

    def fechar(self):
        if self.criancasPulando:
            for kid in self.criancasPulando:
                self.caixa += self.conta[kid.getNome()]
                self.conta[kid.getNome()] = 0
            self.criancasPulando = []
            if self.filaDeEspera:
                for crianc in self.filaDeEspera:
                    self.caixa += self.conta[crianc.getNome()]
                    self.conta[crianc.getNome()] = 0
                self.filaDeEspera = []
            return True