# Importa as funções criadas anteriormente
from banco_de_dados import *

# Define a função para exibir o menu e receber a entrada do hospede
def show_menu():
    print("Selecione uma opção:")
    print("1. Inserir um novo quarto")
    print("2. Inserir um novo hospede")
    print("3. Realizar um aluguel")
    print("4. Atualizar a data de chekout de um aluguel")
    print("5. Exibir todos os quartos alugados no momento")
    print("0. Sair")

    choice = input("Digite o número da opção desejada: ")
    return choice

# Loop principal do programa
while True:
    choice = show_menu()

    if choice == "1":
        name = input("Digite o nome do quarto: ")
        tipo = input("Digite o tipo do quarto: ")
        limite_pessoas = input("Digite o limite de pessoas no quarto: ")
        

        insert_room(name, tipo, limite_pessoas)
        print("quarto inserido com sucesso!")

    elif choice == "2":
        nome = input("Digite o primeiro nome do hospede: ")
        sobrenome = input("Digite o sobrenome do hospede: ")
        endereco = input("Digite o endereço do hospede: ")
        email = input("Digite o endereço de e-mail do hospede: ")
        telefone = input("Digite o número de telefone do hospede: ")

        insert_hosp(nome, sobrenome, endereco, email, telefone)
        print("hospede inserido com sucesso!")

    elif choice == "3":
        hosp_id = input("Digite o ID do hospede: ")
        room_id = input("Digite o ID do quarto: ")
        data_chekin = input("Digite a data de entrada formato: DD-MM-AAAA: ")
        data_chekout = input("Digite a data de saída formato: DD-MM-AAAA: ")

        insert_loan(hosp_id, room_id, data_chekin, data_chekout)
        print("aluguel realizado com sucesso!")

    elif choice == "4":
        loan_id = input("Digite o ID do aluguel: ")
        return_date = input("Digite a nova data de chekout (formato: DD-MM-AAAA): ")

        update_loan_return_date(loan_id, return_date)
        print("Data de chekout atualizada com sucesso!")

    elif choice == "5":
        rooms_on_loan = get_rooms_on_loan()
        print("quartos alugados no momento:")
        for room_id, hops_id, data_chekin, data_chekout in rooms_on_loan:
            print(f"Quarto: {room_id}, Nome do hospede: {hosp_id}, Data do aluguel: {data_chekin}, Data da chekout: {data_chekout}")

    elif choice == "0":
        break

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")