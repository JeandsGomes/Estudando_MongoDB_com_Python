'''
OBSERVAÇÃO: O material ainda esta em estagio de
desenvolvimento, justificando a falta de organização
momentania, kkkkkkk.
'''

import pymongo

def main():
    # Vamos definir uma variável chamada connection_url
    # para armazenar a URL de conexão do MongoDB
    connection_url = "mongodb://localhost:27017" # 27017 é o numero de porta padrão para o mongodb

    # Para se conectar com o MongoDB server, nos vammos
    # usar o MongoClient.
    client = pymongo.MongoClient(connection_url)

    # Usando o objeto cliente, nos podemos acessar as
    # bases de dados. Para isso usamos o
    # list_database_names().
    '''
    print(client.list_database_names())
    '''

    # Voce pode criar uma base de dados usando o comando
    # a baixo.
    database_name = "student_database"
    student_db = client[database_name]

    # A base de dados so podera ser visivel caso
    # voce adicione algum documento a ele.
    # Para criar um documento precisamos criar uma coleção
    #  onde vamos armazena o documento.
    collection_name = "computer science"
    collection = student_db[collection_name]

    # ?? É possivel ver a lista de collections na base de dados
    # usando o seguinte comando ??
    '''
    print(student_db.list_collection_names())
    '''

    # Inserir documentos nas coleções
    # Podemos fazer isso de duas formas
    # 1. Inserirndo apenas um documento na coleção
    # 2. Inserindo varios documentos na coleção

    # Para o 1° caso usamos o comando inser_one()
    '''
    document = {'Name':'Raj',
                'Roll No': 153,
                'Branch': 'CSE'}
    collection.insert_one(document)
    '''

    #Inserir varios
    '''
    documents = [{'Name':'Raj','Roll No': 153,
                'Branch': 'CSE'},{'Name':'Jeands',
                'Roll No': 50,'Branch': 'BRA'},
                 {'Name':'Folote','Roll No': 70,
                'Branch': 'EUA'}]
    collection.insert_many(documents)
    '''

    # Um usuario tambem pode dar um id_customizado ao
    # inserir o documento.

    # Recuperar dados de uma coleção

    # A recuperação de dados pode ser feita de duas
    # maneiras:
    # 1. Recuperando apenas um documento
    # 2. Recuperando varios documentos

    # No primeiro caso usamo o comando find_one(), e
    # fornecemos parametros paraconsultar do documento
    # esperado.
    '''
    query = {"Name":"Raj"}
    print(collection.find_one(query))
    '''

    # No seguindo caso usamos o comando find_many(), o
    # retorno dessa função é um objeto cursor, sendo assim
    # podemos usar um loop para acessar as informações:
    '''
    query = {"Branch":"CSE"}
    result = collection.find(query)
    for i in result:
        print(i)
    '''

    # VOce pode itilisar como filtro os operadores gt,
    # lt, eq e etc.

    #"$eq" = Valor iguala ao especificado
    '''
    query = {"Roll No":{"$eq":153}}
    print(collection.find_one(query))
    '''

    #"$gt" =  Maior que o valor especificado
    '''
    query = {"Roll No":{"$gt":50}}
    print(collection.find_one(query))
    '''

    #"$gte" =  Maior ou igual ao valor especificado
    '''
    query = {"Roll No":{"$gte":153}}
    print(collection.find_one(query))
    '''

    #"$lt" =  Menor que o valor especificado
    '''
    query = {"Roll No": {"$lt":70}}
    print(collection.find_one(query))
    '''

    #"$lte" =  Menor ou igual ao valor especificado
    '''
    query = {"Roll No": {"$lte":50}}
    #print(collection.find_one(query))
    '''

    #Atualizar o documento dentro da coleção
    # Podemos atualizar de duas foras
    # 1. Atualizando um unico documento
    # 2. Atualizando varios documentos

    # Um documento:
    # Para atualizar precisamos de 2 parametros, o
    # o primeiro parametro é o resultado da consulta
    # realizada do documento que deseja atualizar e o
    # segundo é o parametro de atualização.
    '''
    query = {"Roll No":{"$eq":153}}
    present_data = collection.find_one(query)
    new_data = {'$set':{"Name":'Jeronimo'}}
    collection.update_one(present_data,new_data)
    '''

    # Muitos documentos
    '''
    present_data = {"Branch":"CSE"}
    new_data = {"$set":{"Branch":'ECE'}}
    collection.update_many(present_data,new_data)
    '''

    # Remover um documento de uma coleção
    # Podemos remover um document de duas formas
    # 1. Removendo 1 documento
    # 2. Atualizando varios documentos

    #Remover um:
    '''
    query = {"Roll No": 153}
    collection.delete_one(query)
    '''

    # Revomer varios:
    '''
    query = {"Branch":"CSE"}
    collection.delete_many(query)
    '''

    # Removendo a coleção de dados
    # Basta apenas usar o comando .drop()
    '''
    collection.drop()
    '''

if __name__ == "__main__":
    main()