class Cliente:
    def __init__(self, nome, cpf, email, endereco):
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._endereco = endereco

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome

    def getCpf(self):
        return self._cpf

    def setCpf(self, cpf):
        self._cpf = cpf

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def getEndereco(self):
        return self._endereco

    def setEndereco(self, endereco):
        self._endereco = endereco
