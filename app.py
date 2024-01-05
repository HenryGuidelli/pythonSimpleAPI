from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Meu livro',
        'autor': 'henry'
    },
    {
        'id': 2,
        'título': 'Meu livro 2',
        'autor': 'henry 2'
    },
    {
        'id': 3,
        'título': 'Meu livro 3',
        'autor': 'henry 3'
    }
]

#Consultar(todos)
@app.route('/livros', methods=['GET'])

def get_livros():

    return jsonify(livros)

#Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def getId_livros(id):
    
    for livro in livros:
        
        if livro.get('id') == id:
            
            return jsonify(livro)
        
#Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_LivroId(id):

    livro_editado = request.get_json()

    for indice, livro in enumerate(livros):

        if livro.get('id') == id:
            livros[indice].update(livro_editado)
            
            return jsonify(livros[indice])

#Criar
@app.route('/livros', methods=['POST'])
def incluir_livro():

    novo_livro = request.get_json()

    livros.append(novo_livro)
    
    return jsonify(livros)


#Excluir
@app.route('/livros/<int:id>', methods=["DELETE"])
def excluir_livroId(id):

    for indice, livro in enumerate(livros):

        if livro.get("id") == id:
            del livros[indice]

            return jsonify(livros)

app.run(port=8080, host='localhost', debug=True)