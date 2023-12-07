from CadastroDeContatos import CadastroDeContatos

contato1 = CadastroDeContatos('Gustavo', '12423910', 'guerato.gustavo@gmail.com')
contato2 = CadastroDeContatos("Maria", "987654321", "maria@email.com")
contato3 = CadastroDeContatos("João", "123456789", "joao@email.com")

contato1.adicionar_contato()
contato2.adicionar_contato()
contato3.adicionar_contato()

CadastroDeContatos.visualizar_contatos()
