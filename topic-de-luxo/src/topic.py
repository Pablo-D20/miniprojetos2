from src.passageiro import Passageiro


class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios):
        if qtdPrioritarios > capacidade:
            raise ValueError("tem mais assentos prioritarios que a capaciddade")

        self.capacidade = capacidade
        self.qtdPrioritarios = qtdPrioritarios
        self.assentosNormais = [None] * (self.capacidade - self.qtdPrioritarios)
        self.assentosPrioritarios = [None] * qtdPrioritarios
        self.vagas = capacidade


    def getAssentosPrioritarios(self):
        return len(self.assentosPrioritarios)

    def getAssentosNormais(self):
        return len(self.assentosNormais)

    def getPassageiroAssentoNormal(self, lugar):
        if lugar >= 0:
            if lugar < len(self.assentosNormais):
                return self.assentosNormais[lugar]
            else:
                return False
        else:
            return False

    def getPassageiroAssentoPrioritario(self, lugar):
        if lugar >= 0:
            if lugar < len(self.assentosPrioritarios):
                return self.assentosPrioritarios[lugar]
            else:
                return False
        else:
            return False

    def getVagas(self):
        return self.vagas

    def subir(self, passageiro: Passageiro):
        if self.vagas == 0:
            return False

        if passageiro.idade >= 65:
            if self.getAssentosPrioritarios() < self.qtdPrioritarios:
                self.assentosPrioritarios[self.getAssentosPrioritarios()] = passageiro
            else:
                self.assentosNormais[self.getAssentosNormais()] = passageiro
        else:
            if self.getAssentosNormais() > 0:
                self.assentosNormais[self.getAssentosNormais() - 1] = passageiro
            else:
                if self.getAssentosPrioritarios() < self.qtdPrioritarios:
                    self.assentosPrioritarios[self.getAssentosPrioritarios()] = passageiro
                else:
                    print("não há assentos")
                    return False
        self.vagas -= 1
        return True


    def descer(self, nome):
        for i in range(len(self.assentosPrioritarios)):
            if self.assentosPrioritarios[i] and self.assentosPrioritarios[i].nome == nome:
                self.assentosPrioritarios[i] = None
                self.vagas += 1
                return True
        for i in range(len(self.assentosNormais)):
            if self.assentosNormais[i] and self.assentosNormais[i].nome == nome:
                self.assentosNormais[i] = None
                self.vagas += 1
                return True
        return False


    def toString(self):
        status = f'avalie assentos: {self.vagas}\n'
        status += "Assentos preferenciais: "
        for passageiro in self.assentosPrioritarios:
            status += "@" if passageiro else "="
            status += "\n"
        return status