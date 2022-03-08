
# Finalizar CRUD cliente
- [x] findall
- [ ] Save
- [ ] Update/editar
- [ ] findby nome

## Arquitetura MVC
- Model - entities.py (Cliente), Dao
- View - html + jinja
- Controller - routes.py

# Flask + SQLite
- database.py: abre uma conexão com o banco de dados
- dao.py: Interface CRUD para entidade Cliente
- schemas.sql: define a estrutura do banco de dados,
ou seja, as tabelas e as relações.

## Atividade CRUD Produto
Criar no script tabela
- id:  PK auto increment
- nome: text
- desc: text
- preco: FLOAT
- quantidade: INT

Implementar DaoProduto

Entity Produto

Criar a Route para listar todos produtos
/produto/findall

Redefinir cliente para:
/cliente/findall
