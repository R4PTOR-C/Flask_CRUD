from config import DevelopmentConfig, ProductionConfig
from flask import Flask, render_template, request
import psycopg2


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)



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

        return 'Usuário adicionado com sucesso!'
    else:
        return render_template('new.html')


if __name__ == '__main__':
    app.run(debug=True)
