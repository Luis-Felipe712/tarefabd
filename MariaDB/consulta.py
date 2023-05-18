import mysql.connector

config = {
  'user': 'usuarioremoto',
  'password': 'tarefabd',
  'host': '3.235.58.213',
  'database': 'bd_brasil_africa_do_sul'
}

try:
    cnx = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")

cursor = cnx.cursor()
cnx.commit()

def cadastrar_animal():
    raca = input('Raça do animal: ')
    quantidade = int(input('Quantidade: '))
    risco_extincao = input('Risco de extinção (sim ou não): ')
    area_encontrada = input('Área onde é encontrado (norte, sul, leste ou oeste): ')

    insert_query = '''
        INSERT INTO Animais_nativos (raca, quantidade, risco_extincao, area_encontrada)
        VALUES (%s, %s, %s, %s)
    '''
    data = (raca, quantidade, risco_extincao, area_encontrada)

    cursor.execute(insert_query, data)
    cnx.commit()

    print('Animal cadastrado com sucesso!')

def listar_animais():
    select_query = 'SELECT * FROM Animais_nativos'
    cursor.execute(select_query)

    for (id, raca, quantidade, risco_extincao, area_encontrada) in cursor:
        print(f'ID: {id}')
        print(f'Raça: {raca}')
        print(f'Quantidade: {quantidade}')
        print(f'Risco de extinção: {risco_extincao}')
        print(f'Área encontrada: {area_encontrada}')
        print()

def editar_animal():
    id_animal = int(input('ID do animal que deseja editar: '))

    select_query = 'SELECT * FROM Animais_nativos WHERE id = %s'
    cursor.execute(select_query, (id_animal,))
    result = cursor.fetchone()

    if result is None:
        print('Animal não encontrado.')
        return

    print('Digite os novos dados para o animal:')
    raca = input('Raça do animal: ')
    quantidade = int(input('Quantidade: '))
    risco_extincao = input('Risco de extinção (sim ou não): ')
    area_encontrada = input('Área onde é encontrado (norte, sul, leste ou oeste): ')

    update_query = '''
        UPDATE Animais_nativos
        SET raca = %s, quantidade = %s, risco_extincao = %s, area_encontrada = %s
        WHERE id = %s
    '''
    data = (raca, quantidade, risco_extincao, area_encontrada, id_animal)

    cursor.execute(update_query, data)
    cnx.commit()

    print('Animal atualizado com sucesso!')

def excluir_animal():
    id_animal = int(input('ID do animal que deseja excluir: '))

    delete_query = 'DELETE FROM Animais_nativos WHERE id = %s'
    cursor.execute(delete_query, (id_animal,))
    cnx.commit()

    print('Animal excluído com sucesso!')

while True:
    print('Selecione uma opção:')
    print('1. Cadastrar animal')
    print('2. Listar animais')
    print('3. Editar animal')
    print('4. Excluir animal')
    print('0. Sair')

    opcao = int(input('Opção selecionada: '))

    if opcao == 1:
        cadastrar_animal()
    elif opcao == 2:
        listar_animais()
    elif opcao == 3:
        editar_animal()
    elif opcao == 4:
        excluir_animal()
    elif opcao == 0:
        break
    else:
        print('Opção inválida.')

cursor.close()
cnx.close()