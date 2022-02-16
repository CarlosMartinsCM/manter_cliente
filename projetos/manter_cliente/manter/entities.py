# mapear objeto para o banco de dados:
class Cliente:
    def __init__(self, nome, cpf, email):
        """ init eh o construtor """
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def exibir(self):
        print(self.nome, self.cpf, self.email)

if __name__ == '__main__':
    maria = Cliente("Maria", 939393, "test@org.com")
    julia = Cliente("Julia", 111111, "aaa@org.com")
    print(maria.cpf)
    maria.exibir()
    julia.exibir()

