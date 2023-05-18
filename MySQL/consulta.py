import mysql.connector

config = {
  'user': 'admin',
  'password': 'tarefabd',
  'host': 'tarefabd.ckv0zew8rjho.us-east-1.rds.amazonaws.com',
  'database': 'bd_brasil_africa_do_sul2'
}

try:
    cnx = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")
    
cursor = cnx.cursor()
cnx.commit()

def cadastrar_tribo():
    nome = input('Nome da tribo: ')
    habitantes = int(input('Número de habitantes: '))
    renda_media = float(input('Renda média mensal: '))
    escolaridade = input('Escolaridade (fundamental, médio ou superior): ')
    trabalho_assalariado = input('Possui trabalho assalariado (sim ou não): ')

    insert_query = '''
        INSERT INTO Tribos_nativas (nome, habitantes, renda_media, escolaridade, trabalho_assalariado)
        VALUES (%s, %s, %s, %s, %s)
    '''
    data = (nome, habitantes, renda_media, escolaridade, trabalho_assalariado)

    cursor.execute(insert_query, data)
    cnx.commit()

    print('Tribo cadastrada com sucesso!')

def listar_tribos():
    select_query = 'SELECT * FROM Tribos_nativas'
    cursor.execute(select_query)

    for (id, nome, habitantes, renda_media, escolaridade, trabalho_assalariado) in cursor:
        print(f'ID: {id}')
        print(f'Nome: {nome}')
        print(f'Habitantes: {habitantes}')
        print(f'Renda média mensal: {renda_media}')
        print(f'Escolaridade: {escolaridade}')
        print(f'Trabalho assalariado: {trabalho_assalariado}')
        print()

def editar_tribo():
    id_tribo = int(input('ID da tribo que deseja editar: '))

    select_query = 'SELECT * FROM Tribos_nativas WHERE id = %s'
    cursor.execute(select_query, (id_tribo,))
    result = cursor.fetchone()

    if result is None:
        print('Tribo não encontrada.')
        return

    print('Digite os novos dados para a tribo:')
    nome = input('Nome da tribo: ')
    habitantes = int(input('Número de habitantes: '))
    renda_media = float(input('Renda média mensal: '))
    escolaridade = input('Escolaridade (fundamental, médio ou superior): ')
    trabalho_assalariado = input('Possui trabalho assalariado (sim ou não): ')

    update_query = '''
        UPDATE Tribos_nativas
        SET nome = %s, habitantes = %s, renda_media = %s, escolaridade = %s, trabalho_assalariado = %s
        WHERE id = %s
    '''
    data = (nome, habitantes, renda_media, escolaridade, trabalho_assalariado, id_tribo)

    cursor.execute(update_query, data)
    cnx.commit()

    print('Tribo atualizada com sucesso!')

def excluir_tribo():
    id_tribo = int(input('ID da tribo que deseja excluir: '))

    delete_query = 'DELETE FROM Tribos_nativas WHERE id = %s'
    cursor.execute(delete_query, (id_tribo,))
    cnx.commit()

    print('Tribo excluída com sucesso!')

while True:
    print('Selecione uma opção:')
    print('1. Cadastrar tribo')
    print('2. Listar tribos')
    print('3. Editar tribo')
    print('4. Excluir tribo')
    print('0. Sair')

    opcao = int(input('Opção selecionada: '))

    if opcao == 1:
        cadastrar_tribo()
    elif opcao == 2:
        listar_tribos()
    elif opcao == 3:
        editar_tribo()
    elif opcao == 4:
        excluir_tribo()
    elif opcao == 0:
        break
    else:
        print('Opção inválida.')

cursor.close()
cnx.close()