from flask import Flask, render_template, url_for, request, redirect
import psycopg2
from config import DevelopmentConfig, ProductionConfig
import os



app = Flask(__name__)
app.config.from_object(ProductionConfig)

if os.environ.get('FLASK_ENV') == 'development':
    app.config.from_object(DevelopmentConfig)
@app.route('/')
def show_table():
    # Código para buscar dados da tabela no banco de dados
    conn = psycopg2.connect(
        host=app.config['DATABASE_HOST'],
        user=app.config['DATABASE_USER'],
        password=app.config['DATABASE_PASSWORD'],
        database=app.config['DATABASE_NAME']
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    # Renderizar o template HTML e passar os dados para a página
    return render_template('index.html', users=users)
@app.route('/adicionar_usuario', methods=['GET', 'POST'])
def adicionar_usuario():
    if request.method == 'POST':
        # Lógica para adicionar o novo usuário ao banco de dados
        nome = request.form.get('nome')
        email = request.form.get('email')


        # Conecta-se ao banco de dados e insere o novo usuário
        conn = psycopg2.connect(
            host=app.config['DATABASE_HOST'],
            user=app.config['DATABASE_USER'],
            password=app.config['DATABASE_PASSWORD'],
            database=app.config['DATABASE_NAME']
        )

        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (nome, email) VALUES (%s, %s)', (nome, email))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('show_table'))
    else:
        return render_template('new.html')

@app.route('/deletar_usuario/<int:id>', methods=['POST'])
def deletar_usuario(id):
    # Lógica para deletar o usuário com o ID fornecido

    conn = psycopg2.connect(
        host=app.config['DATABASE_HOST'],
        user=app.config['DATABASE_USER'],
        password=app.config['DATABASE_PASSWORD'],
        database=app.config['DATABASE_NAME']
    )

    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('show_table'))


@app.route('/editar_usuario/<int:id>', methods=['GET'])
def editar_usuario(id):
    # Lógica para buscar os dados do usuário com o ID fornecido
    conn = psycopg2.connect(
        host=app.config['DATABASE_HOST'],
        user=app.config['DATABASE_USER'],
        password=app.config['DATABASE_PASSWORD'],
        database=app.config['DATABASE_NAME']
    )

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

    conn = psycopg2.connect(
        host=app.config['DATABASE_HOST'],
        user=app.config['DATABASE_USER'],
        password=app.config['DATABASE_PASSWORD'],
        database=app.config['DATABASE_NAME']
    )

    cursor = conn.cursor()
    cursor.execute('UPDATE usuarios SET nome = %s, email = %s WHERE id = %s', (nome, email, id))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('show_table'))


if __name__ == '__main__':
    app.run(debug=True)
