# Cadastro de Contatos

## Visão Geral

O **CadastroDeContatos** é uma simples classe em Python que permite a criação, visualização e exclusão de contatos. Essa classe mantém uma lista de contatos, cada um representado por um dicionário contendo informações como nome, número de telefone e email.

## Funcionalidades

### 1. Adicionar Contato

Para adicionar um novo contato, você pode criar uma instância da classe **CadastroDeContatos**, fornecer as informações necessárias (nome, número de telefone e email) e chamar o método `adicionar_contato()`. Isso adicionará o contato à lista de contatos.

Exemplo:
```python
agenda = CadastroDeContatos("John Doe", "123-456-7890", "john.doe@example.com")
agenda.adicionar_contato()
