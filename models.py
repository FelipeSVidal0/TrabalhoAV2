from pony.orm import Database, Required, db_session, select

db = Database()

class Roupa(db.Entity):
    nome = Required(str)
    tamanho = Required(str)
    cor = Required(str)
    preco = Required(float)
    genero = Required(str)

# Conecta ao banco de dados SQLite
db.bind(provider='sqlite', filename='roupas.sqlite', create_db=True)
db.generate_mapping(create_tables=True)