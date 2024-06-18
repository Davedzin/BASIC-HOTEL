import sqlite3

# Função para conectar ao banco de dados
def connect():
    conn = sqlite3.connect('hotel.db')
    return conn

# Função para inserir um novo quarto na tabela "quartos"
def insert_room(name, tipo, limite_pessoas):
    conn = connect()
    conn.execute("INSERT INTO quartos (name, tipo, limite_pessoas) VALUES (?, ?, ?)", (name, tipo, limite_pessoas))
    conn.commit()
    conn.close()

# Função para inserir um novo usuário na tabela "hospedes"
def insert_hosp(nome, sobrenome, endereco, email, telefone):
    conn = connect()
    conn.execute("INSERT INTO hospedes (nome, sobrenome, endereco, email, telefone) VALUES (?, ?, ?, ?, ?)", (nome, sobrenome, endereco, email, telefone))
    conn.commit()
    conn.close()

# Função para inserir um novo empréstimo na tabela "aluguel"
def insert_loan(id_quarto, id_hospede, data_chekin, data_chekout):
    conn = connect()
    conn.execute("INSERT INTO aluguel (id_quarto, id_hospede, data_chekin, data_chekout) VALUES (?, ?, ?, ?)", (id_quarto, id_hospede, data_chekin, data_chekout))
    conn.commit()
    conn.close()

# Função para recuperar todos os quartos emprestados no momento
def get_rooms_on_loan():
    conn = connect()
    result = conn.execute("SELECT quartos.name, hospedes.nome, hospedes.sobrenome, aluguel.data_chekin, aluguel.data_chekout \
                           FROM quartos \
                           INNER JOIN aluguel ON quartos.id = aluguel.id_quarto \
                           INNER JOIN hospedes ON hospedes.id = aluguel.id_hospede \
                           WHERE aluguel.data_chekout IS NULL").fetchall()
    conn.close()
    return result

# Função para atualizar a data de devolução de um empréstimo
def update_loan_return_date(id_chekin, data_chekout):
    conn = connect()
    conn.execute("UPDATE aluguel SET data_chekout = ? WHERE id = ?", (data_chekout, id_chekin))
    conn.commit()
    conn.close()

