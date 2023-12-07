class CadastroDeContatos:
    contatos = []

    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def adicionar_contato(self):
        contato = {'nome': self.nome, 'telefone': self.telefone, "email": self.email}
        CadastroDeContatos.contatos.append(contato)

    @staticmethod
    def visualizar_contatos():
        for contato in CadastroDeContatos.contatos:
            print(f'Nome: {contato["nome"]}, Telefone: {contato['telefone']} Email: {contato["email"]}')

    @staticmethod
    def apagar_contatos():
        CadastroDeContatos.contatos = []
        print('Agenda Vazia')
