from flask import Flask, render_template, url_for, request, redirect
import psycopg2
from config import DevelopmentConfig, ProductionConfig

app = Flask(__name__)
app.config.from_object(ProductionConfig)

@app.route('/')
def show_table():
    # Código para buscar dados da tabela no banco de dados
    conn = psycopg2.connect(host='localhost', user='rafael', password='nova_senha', database='banco_de_dados')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Renderizar o template HTML e passar os dados para a página
    return render_template('index.html', data=data)

@app.route('/adicionar_usuario', methods=['GET', 'POST'])
def adicionar_usuario():
    if request.method == 'POST':
        # Lógica para adicionar o novo usuário ao banco de dados
        nome = request.form.get('nome')
        email = request.form.get('email')
        idade = request.form.get('idade')

        # Conecta-se ao banco de dados e insere o novo usuário
        conn = psycopg2.connect(host='localhost', user='rafael', password='nova_senha', database='banco_de_dados')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (nome, email, idade) VALUES (%s, %s, %s)', (nome, email, idade))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('show_table'))
    else:
        return render_template('new.html')

@app.route('/deletar_usuario/<int:id>', methods=['POST'])
def deletar_usuario(id):
    # Lógica para deletar o usuário com o ID fornecido

    conn = psycopg2.connect(host='localhost', user='rafael', password='nova_senha', database='banco_de_dados')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('show_table'))


@app.route('/editar_usuario/<int:id>', methods=['GET'])
def editar_usuario(id):
    # Lógica para buscar os dados do usuário com o ID fornecido
    conn = psycopg2.connect(host='localhost', user='rafael', password='nova_senha', database='banco_de_dados')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE id = %s', (id,))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()

    # Renderizar o template HTML do formulário de edição e passar os dados do usuário
    return render_template('edit.html', usuario=usuario)


@app.route('/atualizar_usuario/<int:id>', methods=['POST'])
def atualizar_usuario(id):
    # Lógica para atualizar os dados do usuário com o ID fornecido
    nome = request.form.get('nome')
    email = request.form.get('email')
    idade = request.form.get('idade')

    conn = psycopg2.connect(host='localhost', user='rafael', password='nova_senha', database='banco_de_dados')
    cursor = conn.cursor()
    cursor.execute('UPDATE usuarios SET nome = %s, email = %s, idade = %s WHERE id = %s', (nome, email, idade, id))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('show_table'))


if __name__ == '__main__':
    app.run(debug=True)
