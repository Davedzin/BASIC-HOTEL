import sqlite3

# Conectar ao banco de dados ou criar um novo
conn = sqlite3.connect('hotel.db')

# Criar uma tabela para os quartos
conn.execute('CREATE TABLE quartos (\
                id INTEGER PRIMARY KEY,\
                name TEXT,\
                tipo TEXT,\
                limite_pessoas TEXT)')

# Criar uma tabela para os hospedes
conn.execute('CREATE TABLE hospedes (\
                id INTEGER PRIMARY KEY,\
                nome TEXT,\
                sobrenome TEXT,\
                endereco TEXT,\
                email TEXT,\
                telefone TEXT)')

# Criar uma tabela para os aluguel
conn.execute('CREATE TABLE aluguel (\
                id INTEGER PRIMARY KEY,\
                id_quarto INTEGER,\
                id_hospede INTEGER,\
                data_chekin TEXT,\
                data_chekout TEXT,\
                FOREIGN KEY(id_quarto) REFERENCES quartos(id),\
                FOREIGN KEY(id_hospede) REFERENCES hospedes(id))')

# Fechar a conexao com o banco de dados
conn.close()