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
    print(client.list_database_names())

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
    print(student_db.list_collection_names())

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
                'Branch': 'CSE'},{'Name':'Raj',
                'Roll No': 153,'Branch': 'CSE'},
                 {'Name':'Raj','Roll No': 153,
                'Branch': 'CSE'}]
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
    query = {"Name":"Raj"}
    print(collection.find_one(query))

    # No seguindo caso usamos o comando find_many()

if __name__ == "__main__":
    main()